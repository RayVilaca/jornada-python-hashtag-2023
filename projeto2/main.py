# Passo a passo do projeto
# Passo 1: Entrar no sistema da empresa 
import pyautogui
import time

pyautogui.PAUSE = 0.3

# abrir o navegador (chrome)
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

# entrar no link 
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(3)

# Passo 2: Fazer login
# selecionar o campo de email
pyautogui.click(x=685, y=451)
# escrever o seu email
pyautogui.write("pythonimpressionador@gmail.com")
pyautogui.press("tab") # passando pro próximo campo
pyautogui.write("sua senha")
pyautogui.click(x=955, y=638) # clique no botao de login
time.sleep(3)

# Passo 3: Importar a base de produtos pra cadastrar
import pandas as pd

tabela = pd.read_csv("produtos.csv")

# Passo 4: Cadastrar um produto
for linha in tabela.index:
    # clicar no campo de código
    pyautogui.click(x=653, y=294)
    
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(str(codigo))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    
    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        pyautogui.write(str(obs))
    
    pyautogui.press("tab")
    pyautogui.press("enter")
    
    # dar scroll de tudo pra cima
    pyautogui.scroll(5000)
