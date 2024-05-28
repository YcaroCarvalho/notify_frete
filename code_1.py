from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import telebot
import time
import pyautogui 


service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

URL = 'https://www.fretebras.com.br/fretes'
TOKEN = '7178561915:AAG-hO5uBNdo8JjbQj78cB6myuao2PKIbnU'
CHAT_ID = '-4197170094'
bot = telebot.TeleBot(TOKEN)
driver.get(URL)
ultimo_cod_link = [None]

while True:
    links = driver.find_elements(By.XPATH, '//*[@id="__next"]/main/div/fuel-grid-container/fuel-grid-item[2]/main/fuel-grid-item/div/a[1]' )
    href = [link.get_attribute('href') for link in links]
    cod_link = (href[0][-14:-1])
    

    if cod_link not in ultimo_cod_link:
        ultimo_link = href
        ultimo_cod_link.append(cod_link) 
        #ENTRARA COMANDO PARA O BOT E PARA COLETAR DADOS DO SITE
        time.sleep(4)
        print(ultimo_link)
        pyautogui.click(x=871, y=381)

        time.sleep(5)
        try:
            produto = driver.find_element(By.XPATH, '/html/body/div[3]/div/div[1]/div/div[4]/div[2]/span[1]').text
        except:
            produto = ('não encotrado')

        try:
            veiculo = driver.find_element(By.XPATH, '/html/body/div[3]/div/div[1]/div/div[5]/div[2]/div[1]/span/a').text
        except FileNotFoundError:                                      
            veiculo = driver.find_element(By.XPATH, '/html/body/div[3]/div/div[1]/div/div[6]/div[2]/div[1]/span/a').text
        except :
            veiculo = ('Não encontrado')
                                                                                                
                                                                                            
        try:
            carroceria = driver.find_element(By.XPATH, '/html/body/div[3]/div/div[1]/div/div[5]/div[2]/div[2]/span/a[1]').text
        except FileNotFoundError: 
            carroceria = driver.find_element(By.XPATH, '/html/body/div[3]/div/div[1]/div/div[6]/div[2]/div[2]/span/a[1]').text 
        except :                                              
            carroceria = ('Não encontrado')

        try:
            tipo_carga = driver.find_element(By.XPATH, '/html/body/div[3]/div/div[1]/div/div[5]/div[2]/div[5]/span[1]').text
        except FileNotFoundError: 
            tipo_carga = driver.find_element(By.XPATH, '/html/body/div[3]/div/div[1]/div/div[6]/div[2]/div[5]/span').text  
        except :
            tipo_carga = ('Não encontrado')  

        try:
            rastreamento = driver.find_element(By.XPATH, '/html/body/div[3]/div/div[1]/div/div[5]/div[2]/div[6]/span').text
        except FileNotFoundError: 
            rastreamento = driver.find_element(By.XPATH, '/html/body/div[3]/div/div[1]/div/div[6]/div[2]/div[6]/span').text
        except :
            rastreamento = ('Não encontrado')

        try:
            agenciamento = driver.find_element(By.XPATH, '/html/body/div[3]/div/div[1]/div/div[5]/div[2]/div[7]/span').text
        except FileNotFoundError: 
            agenciamento = driver.find_element(By.XPATH, '/html/body/div[3]/div/div[1]/div/div[6]/div[2]/div[7]/span').text
        except :
            agenciamento = ('Não encontrado')
        
        try:
            origem_city = driver.find_element(By.XPATH, '/html/body/div[3]/div/div[1]/div/div[3]/div[1]/span/a[1]').text
        except :
            origem_city= ('Não encontrado')                                            
        try:
            origem_estado = driver.find_element(By.XPATH, '/html/body/div[3]/div/div[1]/div/div[3]/div[1]/span/a[2]').text
        except :
            origem_estado= ('Não encontrado') 

        origem = (origem_city, origem_estado)

        try:
            destino_city = driver.find_element(By.XPATH, '/html/body/div[3]/div/div[1]/div/div[3]/div[3]/span/a[1]').text
        except :
            destino_city = ('Não encontrado') 

        try:
            destino_estado = driver.find_element(By.XPATH, '/html/body/div[3]/div/div[1]/div/div[3]/div[3]/span/a[2]').text
        except :
            destino_estado = ('Não encontrado') 
        destino = (destino_city , destino_estado)
       

        bot.send_message(CHAT_ID, text= f'Link: {ultimo_link}\n Produto: {produto}\n Veiculo: {veiculo}\n Origem: {origem} \n Destino: {destino}\n Carroceria:{carroceria}\n Tipo carga:{tipo_carga}')

        driver.back()

    else:
        time.sleep(2)
        driver.refresh()
        

        

    

