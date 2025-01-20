# Automação de Cadastro de Produtos

Este repositório contém um script em Python que automatiza o processo de login no sistema de uma empresa, importação de uma base de dados e cadastro de produtos. O script utiliza as bibliotecas `pyautogui` e `pandas` para realizar as operações de forma automatizada e eficiente.

## Funcionalidades

1. **Abrir o sistema da empresa**  
   O script abre o navegador e acessa o sistema da empresa na URL especificada.
   
2. **Login automático**  
   Realiza o login no sistema utilizando credenciais pré-definidas.

3. **Importação da base de dados**  
   Lê uma planilha Excel com as informações dos produtos a serem cadastrados.

4. **Cadastro automatizado de produtos**  
   Preenche os campos de cadastro de produtos no sistema com base nos dados da planilha.

## Pré-requisitos

- **Python 3.8 ou superior**  
  Certifique-se de ter o Python instalado no seu computador.

- **Bibliotecas necessárias**  
  Instale as bibliotecas utilizadas no projeto com o seguinte comando:
  ```bash
  pip install pyautogui pandas openpyxl
