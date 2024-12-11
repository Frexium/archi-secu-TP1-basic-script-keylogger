from pynput.keyboard import Key, Listener

def processkeys(key):
    print(f'{key} pressed')

# 6. Utilisation de `pynput.keyboard.Listener`
keyboard_listener = Listener(on_press=processkeys)

# 7. Lignes de code pour démarrer l'écoute
with keyboard_listener:
    keyboard_listener.join()