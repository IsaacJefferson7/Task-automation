# 🚀 Automação de Cadastro de Produtos

Este repositório contém um script em Python que automatiza o processo de login no sistema de uma empresa, importação de uma base de dados e cadastro de produtos. O script utiliza as bibliotecas `pyautogui` e `pandas` para realizar as operações de forma automatizada e eficiente.

## 💡 Funcionalidades

1. **Abrir o sistema da empresa**  
   O script abre o navegador e acessa o sistema da empresa na URL especificada.
   
2. **Login automático**  
   Realiza o login no sistema utilizando credenciais pré-definidas.

3. **Importação da base de dados**  
   Lê uma planilha Excel com as informações dos produtos a serem cadastrados.

4. **Cadastro automatizado de produtos**  
   Preenche os campos de cadastro de produtos no sistema com base nos dados da planilha.

## 💻 Pré-requisitos

- **Python 3.8 ou superior**  
  Certifique-se de ter o Python instalado no seu computador.

- **Bibliotecas necessárias**  
  Instale as bibliotecas utilizadas no projeto com o seguinte comando:
  ```bash
  pip install pyautogui pandas openpyxl

## 📈 Planilha Excel
    
O arquivo contendo os dados dos produtos deve estar no formato .csv e incluir as colunas:
   
   Codigo
    
   Marca
    
   Tipo
    
   Categoria
    
   Preço Unitário
    
   Custo
    
   Obs (opcional)


## 🔎 Como usar

   Clone o repositório:
```bash
git clone https://github.com/seu-usuario/automacao-cadastro-produtos.git
```

Navegue até o diretório do projeto:
```bash
cd automacao-cadastro-produtos
```
Certifique-se de ajustar as coordenadas dos cliques (x, y) no script conforme a resolução da tela e o layout do sistema da empresa.
Salve a planilha Excel no mesmo diretório do script, renomeada como produtos.xlsx.

Execute o script:
```bash
python cadastro_produtos.py
```

## 📝 Observações

   O script foi desenvolvido e testado para sistemas específicos com base em coordenadas fixas de tela. Certifique-se de ajustar as coordenadas para o seu ambiente.
    A funcionalidade de automação depende da resolução e do layout da interface gráfica do sistema.

## 🔧 Tecnologias Utilizadas

⚙ pyautogui: Automação de interações com a interface gráfica, como cliques, pressionamento de teclas e movimentação do mouse

⚙ pandas: Manipulação e leitura de dados estruturados, como planilhas Excel.

## 🏷 Licença

Este projeto é de uso livre para fins educacionais e profissionais. Contribuições são bem-vindas!

Se precisar de ajustes ou desejar incluir mais detalhes, me avise!
