import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
import time

def unifran():    

    #abrir o navegador
    s = Service('C:\\Users\\Eduardo\Documents\\GitHub\\bot-loginSites\\chromedriver.exe')
    driver = webdriver.Chrome(service=s)
    driver.get("https://novoportal.cruzeirodosul.edu.br/?empresa=unifran&blackboard=false")
    driver.maximize_window()

    time.sleep(3)
    #Colocar o CPF e a senha
    actions = ActionChains(driver) 
    actions.send_keys(Keys.TAB, '15684409601', Keys.TAB, '98842')
    actions.perform()

    #Apertar o botão para acessar a área do aluno
    actions.send_keys(Keys.TAB * 2, Keys.ENTER)
    actions.perform()
    input()
    
unifran()