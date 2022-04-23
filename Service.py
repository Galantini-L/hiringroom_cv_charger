from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time

XPATH_PERSONAL_INFORMATION = [
    '//*[@id="txtNome"]',
    '//*[@id="txtSobreNome"]',
    '//*[@id="txtEmail"]',
    '//*[@id="select_postul_country"]',
    '//*[@id="select_postul_zona"]',
    '//*[@id="select_postul_local"]',
    '/html/body/div[1]/section/div/div[3]/form/div[1]/div/div[2]/div[2]/div/div[9]/div/input',
    '//*[@id="select_postul_nationality"]',
    '//*[@id="txtTelefone"]',
    '//*[@id="birthdayPicker"]/fieldset/select[1]',
    '//*[@id="birthdayPicker"]/fieldset/select[2]',
    '//*[@id="birthdayPicker"]/fieldset/select[3]',
    '//*[@id="generoPostulante_h"]'
]
'//*[@id="language_fields"]/div/div[2]/div/a/span'
XPATH_LEGUAGES = [
    '//*[@id="language_fields"]/div/div[1]/div/div[2]/div/select',
    '//*[@id="language_fields"]/div/div[1]/div/div[3]/div/select',
    '//*[@id="language_fields"]/div/div[1]/div/div[4]/div/select'
]

def insert(xpath_list:list, user_data:list):
    for i in range(len(xpath_list)):
        try:
            driver.find_element(by=By.XPATH, value= xpath_list[i]).send_keys(str(user_data[i]))
            #time.sleep(1)
            print(f'Possition {xpath_list[i]} sussesfuly ---> data type {type(user_data[i])}')
        except:
            print(f'failed{xpath_list[i]}, for data {user_data[i]}---> data type {type(user_data[i])}')
def get_cv_data(sheet:str):
    data=[]
    cv_info = pd.read_excel("cv_data.ods", engine="odf", sheet_name=sheet)
    da =cv_info.head()
    #print(da)
    for i, d in da.items():
        print(f'series of da.item {d}')
        data.append(d[0])
        print(f'section 0 of series of da.item {d[0]}')
    return data

if __name__ == '__main__':
    #page = 'https://hiringroom.com/jobs/get_vacancy/624efc869a926355a29df9f6/candidates/new?source=linkedinjobs'
    #chromeDriver = 'webDriver/chromedriver'
    #driver = webdriver.Chrome(chromeDriver)
    #driver.get(page)
    personal_info = get_cv_data('Idiomas')
    #insert(personal_info)
    