from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def chrome_instance():
    options = Options()
    options.add_argument("--start-maximized")
    #options.add_argument("--headless")  # Executa o Chrome sem abrir a janela
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    return driver
