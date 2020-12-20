from selenium import webdriver
import time
import sys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import pandas as pd
import time

def par_impar(num):
    if num%2 == 0:
        return True
    else:
        return False

driver = webdriver.Chrome('driver/chromedriver.exe')

#Login
driver.get('https://www.instagram.com/accounts/login/')
time.sleep(3)

driver.maximize_window()
driver.find_element_by_name("username").send_keys('usuario')
driver.find_element_by_name('password').send_keys('contraseña', Keys.ENTER)
time.sleep(5)
driver.get(sys.argv[1])
time.sleep(3)


horaActual = time.time()
while True:
    try:
        WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.XPATH, '//button[@class="dCJp8 afkep"]')))
        cargar_mas_comentarios = driver.find_element_by_xpath('//button[@class="dCJp8 afkep"]')
        driver.execute_script("arguments[0].scrollIntoView();", cargar_mas_comentarios)
        
        driver.execute_script("arguments[0].click();", cargar_mas_comentarios)
    except Exception as ex:
        print(ex)
        break

soup = BeautifulSoup(driver.page_source,'html.parser')
comentarios = soup.find_all('div',attrs={'class':'C4VMK'})
soup2 = BeautifulSoup(str(comentarios),'html.parser')
spans = soup2.find_all('span')
comments = [i.text.strip() for i in spans if i != '']

count = 0

usuarios =[]
comentarios =[]



for c in comments:
    if par_impar(count):
        usuarios.append(c)
    else:
        comentarios.append(c)
    if c != 'Verificado':
        count+=1
    else:
        comentarios.remove('Verificado')

lista = []

for u, c in zip(usuarios, comentarios):

    lista.append({f'{u}':f'{c}'})
    print(f'Usuario: {u}\n Comentario: {c}')

print(f'Cantidad de Comentarios: {len(lista)}')
print(f'Ejecutado en {time.time() - horaActual}')

data = {'nombre': usuarios, 'comentario': comentarios}

df = pd.DataFrame(data, columns=['nombre', 'comentario'])
df.to_excel('Comentarios.xlsx', sheet_name='Comentarios')

