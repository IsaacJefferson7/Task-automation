# Passo 1: Abrir o sistema da empresa.
#    https://dlp.hashtagtreinamentos.com/python/intensivao/login
# Passo 2:Fazer o login.
# Passo 3: Impotar a base de dados dos produtos.
# Passo 4: Cadastrar um novo produto.
# Passo 5: Repetir o passo 4 até acabar todos os produtos.

# Passo 1:
import pyautogui
import time

pyautogui.press('win') # tecla do windows
time.sleep(1)

pyautogui.write('firefox') # escrever firefox
time.sleep(1)

pyautogui.press('enter') # pressionar enter
time.sleep(5)  # Aumentar o tempo de espera para garantir que o Firefox esteja totalmente carregado

pyautogui.hotkey("ctrl", "t") # abre uma nova aba
time.sleep(2)

# Selecionar a barra de endereço da aba atual
pyautogui.hotkey("ctrl", "l") # selecionar a barra de endereço
time.sleep(2)
pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')  
time.sleep(2)

pyautogui.press('enter')
time.sleep(5)