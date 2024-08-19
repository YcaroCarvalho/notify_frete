from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import telebot
import time
import pyautogui

service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

URL = 'https://www.fretebras.com.br/fretes/carga-de-pr/carga-para-mg'
TOKEN = '7178561915:AAG-hO5uBNdo8JjbQj78cB6myuao2PKIbnU'
CHAT_ID = '-4197170094'
bot = telebot.TeleBot(TOKEN)
driver.get(URL)
ultimo_cod_link = [None]

while True:
    links = driver.find_elements(By.XPATH,  '//*[@id="__next"]/main/div/fuel-grid-container/fuel-grid-item[2]/main/fuel-grid-item/div/a[1]')
    href = [link.get_attribute('href') for link in links]
    cod_link = (href[0][-14:-1])

    if cod_link not in ultimo_cod_link:
        ultimo_link = href
        ultimo_cod_link.append(cod_link)
        #ENTRARA COMANDO PARA O BOT E PARA COLETAR DADOS DO SITE
        time.sleep(1)
        print(ultimo_link)
        pyautogui.click(x=871, y=381)


        def search_xpaths(xpaths):
            for xpath in xpaths:
                try:
                    informacao = driver.find_element(By.XPATH, xpath).text
                    return informacao
                except NoSuchElementException:
                    pass


        #COLETA INFORMAÇÕES DO PRODUTO
        xpaths = [
            "/html/body/div[3]/div/div[1]/div/div[3]/div[2]/span[1]",
            "/html/body/div[3]/div/div[1]/div/div[4]/div[2]/span[1]",
            '/html/body/div[3]/div/div[1]/div/div[5]/div[2]/span[1]',
            '/html/body/div[3]/div/div[1]/div/div[6]/div[2]/span[1]',
            '/html/body/div[3]/div/div[1]/div/div[7]/div[2]/span[1]', ]

        produto = search_xpaths(xpaths)

        #COLETA INFORMAÇÕES DO VEICULO

        xpaths = ['/html/body/div[3]/div/div[1]/div/div[3]/div[2]/div[1]/span/a'
                  '/html/body/div[3]/div/div[1]/div/div[4]/div[2]/div[1]/span/a',
                  '/html/body/div[3]/div/div[1]/div/div[5]/div[2]/div[1]/span/a',
                  '/html/body/div[3]/div/div[1]/div/div[6]/div[2]/div[1]/span/a',
                  '/html/body/div[3]/div/div[1]/div/div[7]/div[2]/div[1]/span/a'
                  ]
        veiculo = search_xpaths(xpaths)

        # COLETA INFORMAÇÕES DA CARROCERIA
        xpaths = ['/html/body/div[3]/div/div[1]/div/div[3]/div[2]/div[2]/span/a',
                  '/html/body/div[3]/div/div[1]/div/div[4]/div[2]/div[2]/span/a',
                  '/html/body/div[3]/div/div[1]/div/div[5]/div[2]/div[2]/span/a',
                  '/html/body/div[3]/div/div[1]/div/div[6]/div[2]/div[2]/span/a',
                  '/html/body/div[3]/div/div[1]/div/div[7]/div[2]/div[2]/span/a'
                  ]
        carroceria = search_xpaths(xpaths)

        # COLETA INFORMAÇÕES DO TIPO DA CARGA
        xpaths = ['/html/body/div[3]/div/div[1]/div/div[3]/div[2]/div[5]/span',
                  '/html/body/div[3]/div/div[1]/div/div[4]/div[2]/div[5]/span',
                  '/html/body/div[3]/div/div[1]/div/div[5]/div[2]/div[5]/span',
                  '/html/body/div[3]/div/div[1]/div/div[6]/div[2]/div[5]/span',
                  '/html/body/div[3]/div/div[1]/div/div[7]/div[2]/div[5]/span'
                  ]
        tipo_carga = search_xpaths(xpaths)

        # COLETA INFORMAÇÕES DO RASTREIO
        xpaths = ['/html/body/div[3]/div/div[1]/div/div[3]/div[2]/div[6]/span',
                  '/html/body/div[3]/div/div[1]/div/div[4]/div[2]/div[6]/span',
                  '/html/body/div[3]/div/div[1]/div/div[5]/div[2]/div[6]/span',
                  '/html/body/div[3]/div/div[1]/div/div[6]/div[2]/div[6]/span',
                  '/html/body/div[3]/div/div[1]/div/div[7]/div[2]/div[6]/span'
                  ]
        search_xpaths(xpaths)

        #INFORMAÇÕES SOBRE O AGENCIAMENTO
        xpaths = ['/html/body/div[3]/div/div[1]/div/div[3]/div[2]/div[7]/span',
                  '/html/body/div[3]/div/div[1]/div/div[4]/div[2]/div[7]/span',
                  '/html/body/div[3]/div/div[1]/div/div[5]/div[2]/div[7]/span',
                  '/html/body/div[3]/div/div[1]/div/div[6]/div[2]/div[7]/span',
                  '/html/body/div[3]/div/div[1]/div/div[7]/div[2]/div[7]/span',
                  ]
        search_xpaths(xpaths)

        #ORIGEM E DESTINO
        origem_city = driver.find_element(By.XPATH, '/html/body/div[3]/div/div[1]/div/div[3]/div[1]/span/a[1]').text
        origem_estado = driver.find_element(By.XPATH, '/html/body/div[3]/div/div[1]/div/div[3]/div[1]/span/a[2]').text
        origem = f'{origem_city} - {origem_estado}'
        origem = ('').join(origem)

        destino_city = driver.find_element(By.XPATH, '/html/body/div[3]/div/div[1]/div/div[3]/div[3]/span/a[1]').text
        destino_estado = driver.find_element(By.XPATH, '/html/body/div[3]/div/div[1]/div/div[3]/div[3]/span/a[2]').text
        destino = f'{destino_city} - {destino_estado}'
        destino = ('').join(destino)

        bot.send_message(CHAT_ID, text=f'Link: {ultimo_link}\n Produto: {produto}\n Veiculo: {veiculo}\n Origem: {origem} \n Destino: {destino}\n Carroceria: {carroceria}\n Tipo carga: {tipo_carga}')

        driver.back()

    else:
        time.sleep(0.5)
        driver.refresh()