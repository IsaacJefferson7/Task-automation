# Passo 1: Abrir o sistema da empresa.
#    https://dlp.hashtagtreinamentos.com/python/intensivao/login
# Passo 2:Fazer o login.
# Passo 3: Impotar a base de dados dos produtos.
# Passo 4: Cadastrar um novo produto.
# Passo 5: Repetir o passo 4 até acabar todos os produtos.

import pyautogui
import time

pyautogui.PAUSE = 0.5

# PASSO 1:

  # Abrir o navegador
  pyautogui.press('win') # tecla do windows

  pyautogui.write('firefox') # escrever firefox

  pyautogui.press('enter') # pressionar enter


  # Acessar o sistema da empresa
  pyautogui.hotkey("ctrl", "t") # abre uma nova aba

  pyautogui.hotkey("ctrl", "l") # selecionar a barra de endereço

  pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')

  pyautogui.press('enter')

  time.sleep(3)


# PASSO 2:
  #Fazer o login
  pyautogui.press("tab") # pressionar tab

  pyautogui.write("isaac") # escrever o usuário

  pyautogui.press("tab") # pressionar tab

  pyautogui.write("12345") #  escrever a senha

  pyautogui.press('enter') # pressionar enter


# PASSO 3:

