from cmath import nan
from distutils.log import error
from numpy import nan_to_num
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time
"""
author: Lautaro Galantini

Auntomatizacion para carga de información de cv en el portal "hiringroom"
"""

SHEETS = ['personal information','languages']

XPATH_PERSONAL_INFORMATION = [
    '/html/body/div[1]/section/div/div[3]/form/div[1]/div/div[2]/div[2]/div/div[1]/div/input',
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
XPATH_LEGUAGES = [
    '/html/body/div[1]/section/div/div[3]/form/div[2]/div/div[2]/div/div/div[1]/div/div[2]/div/select',
    '/html/body/div[1]/section/div/div[3]/form/div[2]/div/div[2]/div/div/div[1]/div/div[3]/div/select',
    '/html/body/div[1]/section/div/div[3]/form/div[2]/div/div[2]/div/div/div[1]/div/div[4]/div/select'
]
XPATH_WORK_EXPERIENCE= [
    '/html/body/div[1]/section/div/div[3]/form/div[3]/div/div[2]/div[5]/div/div[1]/div/div[2]/div/input',
    '/html/body/div[1]/section/div/div[3]/form/div[3]/div/div[2]/div[5]/div/div[1]/div/div[3]/div/select',
    '/html/body/div[1]/section/div/div[3]/form/div[3]/div/div[2]/div[5]/div/div[1]/div/div[4]/div/input',
    '/html/body/div[1]/section/div/div[3]/form/div[3]/div/div[2]/div[5]/div/div[1]/div/div[5]/div/select',
    '/html/body/div[1]/section/div/div[3]/form/div[3]/div/div[2]/div[5]/div/div[1]/div/div[6]/div/select',
    '/html/body/div[1]/section/div/div[3]/form/div[3]/div/div[2]/div[5]/div/div[1]/div/div[7]/div/select',
    '/html/body/div[1]/section/div/div[3]/form/div[3]/div/div[2]/div[5]/div/div[1]/div/div[8]/div/select',
    '/html/body/div[1]/section/div/div[3]/form/div[3]/div/div[2]/div[5]/div/div[1]/div/div[9]/div/p/input',
    '/html/body/div[1]/section/div/div[3]/form/div[3]/div/div[2]/div[5]/div/div[1]/div/div[10]/div/select[1]',
    '/html/body/div[1]/section/div/div[3]/form/div[3]/div/div[2]/div[5]/div/div[1]/div/div[10]/div/select[2]',
    '/html/body/div[1]/section/div/div[3]/form/div[3]/div/div[2]/div[5]/div/div[1]/div/div[10]/div/select[3]',
    '/html/body/div[1]/section/div/div[3]/form/div[3]/div/div[2]/div[5]/div/div[1]/div/div[10]/div/select[4]',
    '/html/body/div[1]/section/div/div[3]/form/div[3]/div/div[2]/div[5]/div/div[1]/div/div[11]/div/textarea'
]

def insert(xpath_list:list, user_data:list):
    # click to deploy
    if xpath_list == XPATH_LEGUAGES:
        try:
        # languague
            driver.find_element(by=By.XPATH, value='/html/body/div[1]/section/div/div[3]/form/div[2]/div/div[2]/div/div/div[2]/div/a/span').click()
        except:
            print(f'cant press button language')
#    elif xpath_list == XPATH_WORK_EXPERIENCE:
#        try:
           # work experience
#           driver.find_element(by=By.XPATH, value='/html/body/div[1]/section/div/div[3]/form/div[3]/div/div[2]/div[5]/div/div[2]/div/a/span').click()
#        except:
#            print(f'cant press button')

    for xp, ud in zip(xpath_list,user_data):
        try:
            driver.find_element(by=By.XPATH, value=xp).send_keys(str(ud))
            time.sleep(0.2)
            #print(f'Possition {xp} sussesfuly ---> data {ud}')
        except:
            print(f'failed{xp}, for data {ud}---> data type {type(ud)}')


def get_cv_data(sheet:str):
    data=[]
    cv_info = pd.read_excel("cv_data.ods", engine="odf", sheet_name=sheet)
    da =cv_info.head()
    #print(da)
    for i, d in da.items():
        if str(d[0]) == 'nan':
            print(f'campo {i} en blanco')
        data.append(str(d[0]))
    return data

if __name__ == '__main__':
    page = input('Insert URL: \n')
    chromeDriver = 'webDriver/chromedriver'
    driver = webdriver.Chrome(chromeDriver)
    driver.get(page)
    xpath = [XPATH_PERSONAL_INFORMATION, XPATH_LEGUAGES]
    for i in range(len(SHEETS)):
        personal_info = get_cv_data(SHEETS[i])
        print(f'data table {personal_info}')
        insert(xpath[i],personal_info)