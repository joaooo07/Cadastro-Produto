#PASSO 1 - ENTRAR NO SISTEMA DA EMPRESA. 
#PASSO 2 - FAZER LOGIN 
#PASSO 3 - IMPORTAR A BASE DE DADOS
#PASSO 4 - CADASTRAR UM PRODUTO
#PASSO 5 - REPETIR PASSO 4 ATÉ O CADASTRO DE TODOS OS PRODUTOS. 
import pandas 
import pyautogui
import time 
#time Controla o Tempo 
#pyautogui.click - permite clicar com o mouse. utilizando posição x- horizontal e y- vertical 
#pyautogui.write - permite escrever um texto.
#pyautogui.press - permite pressionar uma tecla.
#pyautogui.hotkey - combinação de tecla (ctrl + C).
#pyautogui.scroll - Rolar a Tela para cima ou para baixo.
#numero positivo vai pra cima, negativo para baixo
#pyautogui.PAUSE = 0.5 (Demora 0.5 entre uma excução e outra)
pyautogui.PAUSE = 1 # a cada comando do pyautogui demora 0.5

pyautogui.press("win")
pyautogui.write("microsoft")
pyautogui.press("enter")
pyautogui.press("enter")
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
#Dependendo da velocidade da internet, 0.5 pode ser rapido demais para carregar o site,
#por isso utiizamos o time.
#para nao dar conflito.
time.sleep(5) # depois do enter, aguardar 5 segundos antes do proximo comando 
pyautogui.click(x=682, y=395) #posição encontrada utilizando a pasta auxiliar.py
# descobrindo a posição utilizando o pyautogui.position
pyautogui.hotkey("ctrl", "a") #Caso seu campo de e-mail esteja preenchido. ctrl A seleciona tudo
pyautogui.write("pythonimpressionador@gmail.com")
#pyautogui.click(x=563, y=491)
#utilizando o tab ao inves do mouse
pyautogui.press("tab")
pyautogui.write("123456")
pyautogui.click(x=706, y=556)
time.sleep(5)
tabela = pandas.read_csv("produtos.csv") #ler a base de dados no formato csv. (nome da base)
#necessita estar na mesma pagina do codigo
#caso contrario tem que pegar o caminho inteiro da pasta ("c://Users...    ")

for linha in tabela.index: #Para cada linha da tabela
    pyautogui.click(x=613, y=272)
    #codigo
    codigo = str(tabela.loc[linha, "codigo"])
    #define uma variavel. transforma em string. usa um dos comandos pandas para localizar o item
    #da tabela, especificando a linha e o nome da coluna
    pyautogui.write(codigo)
    pyautogui.press("tab")
    #marca
    marca = str(tabela.loc[linha, "marca"])
    pyautogui.write(marca)
    pyautogui.press("tab")
    #tipo
    tipo = str(tabela.loc[linha, "tipo"])
    pyautogui.write(tipo)
    pyautogui.press("tab")
    #categoria
    categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.write(categoria)
    pyautogui.press("tab")
    #preço unitario
    preco = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.write(preco)
    pyautogui.press("tab")
    #custo
    custo = str(tabela.loc[linha, "custo"])
    pyautogui.write(custo)
    pyautogui.press("tab")
    #obs
    obs = str(tabela.loc[linha, "obs"])
    if obs != "nan": 
        #Se a obs for diferente de nan (vazia)
        pyautogui.write(obs)
    pyautogui.press("tab")
    #enviar
    pyautogui.press("enter")
    pyautogui.scroll(1000)
