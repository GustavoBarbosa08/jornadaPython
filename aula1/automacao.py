# passo a passo do projeto

# entrar no sistema 

import pyautogui
import time
import pandas

#pyautogui.click
#pyautogui.write        
#pyautogui.press
#pyautogui.hotkey("ctrl", "c")

pyautogui.PAUSE = 0.5 #feito para um comando não atropelar o outro

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

# entrar no link: https://dlp.hashtagtreinamentos.com/python/intensivao/login
time.sleep(2)
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")


#esperar o site carregar

time.sleep(3)

# fazer login
#pyautogui.click(x=1033, y=450, clikes=2)
#pyautogui.click(x=1033, y=450, button="right")

pyautogui.click(x=1033, y=450)
pyautogui.write("jornadapython@gmail.com")

#poderia dar um pyautogui.click("tab"), pois quando se clica no tab em todos os sistemas ele desce para o campo de baixo

pyautogui.click(x=962, y=571)
pyautogui.write("000000")

pyautogui.press("enter")

# importar a base de dados
#PANDAS pacote de código que trabalha com base de dados de modo eficiente

tabela = pandas.read_csv("D:\Visual Studio Code\python\jornada_python\produtos.csv")
#print(tabela)


for linha in tabela.index:
     # cadastrar o primeiro produto
     pyautogui.click(x=940, y=319)

     codigo = tabela.loc[linha, "codigo"]
     pyautogui.write(str(codigo))
     pyautogui.press("tab")

     marca = tabela.loc[linha, "marca"]
     pyautogui.write(str(marca))
     pyautogui.press("tab")

     tipo = tabela.loc[linha, "tipo"]
     pyautogui.write(str(tipo))
     pyautogui.press("tab")

     categoria = tabela.loc[linha, "categoria"]
     pyautogui.write(str(categoria))
     pyautogui.press("tab")

     preco_unitario = tabela.loc[linha, "preco_unitario"]
     pyautogui.write(str(preco_unitario))
     pyautogui.press("tab")

     custo = tabela.loc[linha, "custo"]
     pyautogui.write(str(custo))
     pyautogui.press("tab")

     obs = tabela.loc[linha, "obs"]
     if not pandas.isna(obs): #se o obs não é vazio(NaN) ele preenche, se não ele vai embora sem fazer nada
          pyautogui.write(str(obs))

     #enter para cadastro

     pyautogui.press("enter")

# repetir isso pra todos os produtos  


