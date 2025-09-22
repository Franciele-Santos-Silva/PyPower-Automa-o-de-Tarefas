import pyautogui 
#Passo 1: Entrar no sistema da empresa - https://dlp.hashtagtreinamentos.com/python/intensivao/login .
#abrir o navegador (chrome) .
pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')

#digitar o site
pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pyautogui.press('enter')






#Passo 2: Fazer login .
#Passo 3: Importar a base de dados de produtos pra cadastrar .
#Passo 4: Cadastrar um produto .
#Passo 5: Repetir o cadastro para todos os produtos .

#pyautogui -> faz automaçoes em python(controla mouse,teclado e tela do computador)

# pyautogui.click -> clicar em algum lugar da tela
# pyautogui.press -> apertar 1 tecla
# pyautogui.write -> escrever um texto
# pyautogui.hotkey -> apertar combinação de teclas 