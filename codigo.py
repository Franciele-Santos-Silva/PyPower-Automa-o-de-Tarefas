import pyautogui
import time
import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()        
EMAIL = os.getenv("EMAIL")
SENHA = os.getenv("SENHA")

pyautogui.PAUSE = 1 

def abrir_navegador(url: str):
    pyautogui.press('win')      

    pyautogui.write('chrome')   
    pyautogui.press('enter')   
    time.sleep(2)
    pyautogui.write(url)       
    pyautogui.press('enter')    
    time.sleep(3)               

def fazer_login(email: str, senha: str):
    pyautogui.click(x=685, y=451) 
    pyautogui.write(email)          
    pyautogui.press('tab')          
    pyautogui.write(senha)          
    pyautogui.click(x=955, y=638) 
    time.sleep(3)

def importar_base(caminho_csv: str) -> pd.DataFrame:
    tabela = pd.read_csv(caminho_csv)
    print(tabela)
    return tabela

def cadastrar_produto(linha):
    pyautogui.click(x=653, y=294)  
    pyautogui.write(str(linha["codigo"]))
    pyautogui.press('tab')
    pyautogui.write(str(linha["marca"]))
    pyautogui.press('tab')
    pyautogui.write(str(linha["tipo"]))
    pyautogui.press('tab')
    pyautogui.write(str(linha["categoria"]))
    pyautogui.press('tab')
    pyautogui.write(str(linha["preco_unitario"]))
    pyautogui.press('tab')
    pyautogui.write(str(linha["custo"]))
    pyautogui.press('tab')
    
    if not pd.isna(linha.get("obs")):
        pyautogui.write(str(linha["obs"]))
    pyautogui.press('tab')
    pyautogui.press('enter') 
    pyautogui.scroll(5000)    

def cadastrar_todos_produtos(tabela: pd.DataFrame):
    for _, linha in tabela.iterrows():
        cadastrar_produto(linha)

URL_SISTEMA = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
CSV_PRODUTOS = "produtos.csv"

abrir_navegador(URL_SISTEMA)
fazer_login(EMAIL, SENHA)
tabela_produtos = importar_base(CSV_PRODUTOS)
cadastrar_todos_produtos(tabela_produtos)
