# Passo 1: Abrir o sistema da empresa.
#    https://dlp.hashtagtreinamentos.com/python/intensivao/login
# Passo 2:Fazer o login.
# Passo 3: Impotar a base de dados dos produtos.
# Passo 4: Cadastrar os produtos.

import pyautogui
import pandas as pd
import time

pyautogui.PAUSE = 2

# PASSO 1: Abrir o sistema da empresa

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


# PASSO 2: Fazer o login

#pyautogui.press("tab") # pressionar tab
pyautogui.click(x=447, y=406) # clicar no campo de usuário
pyautogui.write("isaac.produtos@gmail.com") # escrever o usuário

pyautogui.press("tab") # ir para o campo de senha
pyautogui.write("12345") #  escrever a senha
    
pyautogui.press("tab") # ir para o botão de logar
pyautogui.press('enter') # pressionar enter


# PASSO 3: Importar a base de dados dos produtos

tabela = pd.read_excel('produtos.csvisaac.produtos@gmail.comhttps://dlp.hashtagtreinamentos.com/python/intensivao/login') # importar a base de dados e salva na variável tabela
print(tabela) # exibir a tabela

time.sleep(2)

# PASSO 4: Cadastrar os produto
    
for i, produto in tabela.iterrows():
    pyautogui.click(x=345, y=300) # ir para o campo código do produto
    pyautogui.write(produto['Codigo'])

    pyautogui.click("tab") # ir para o campo marca do produto")
    pyautogui.write(str(produto['Marca']))

    pyautogui.click("tab") # ir para o campo tipo do produto
    pyautogui.write(str(produto['Tipo']))

    pyautogui.click("tab") # ir para o campo categoria do produto
    pyautogui.write(produto['Categoria'])

    pyautogui.click("tab") # ir para o campo preço unitário do produto
    pyautogui.write(str(produto['Preço Unitário']))

    pyautogui.click("tab") # ir para o campo custo do produto
    pyautogui.write(str(produto['Custo']))

    pyautogui.click("tab") # ir para o campo obs
    if pd.isna(produto['Obs']):
        pyautogui.write("")
    else:
        pyautogui.write(produto['Obs'])

    pyautogui.click("tab") # ir para o botão enviar
    pyautogui.press('enter') # pressionar enviar e salvar o cadastro

    time.sleep(2) # esperar 2 segundos para cadastrar o próximo produto

    if i < len(tabela) - 1:
        i += 1
        pyautogui.scroll(2000) # rolar a página para cima
        time.sleep(2) # esperar 2 segundos para cadastrar o próximo produto
    else:
        break
