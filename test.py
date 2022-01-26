from msilib.schema import File
from time import sleep

from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests
import json
def findemail(name,domain):

    data = {"full_name": name,'domain': domain}
    headers = {'X-Api-Key': 'x7DRpUQ2gPDVMgqjprviBW6g'}

    resp = requests.post('https://api.anymailfinder.com/v4.0/search/person.json', data=data, headers=headers)

    data = json.loads(resp.content)
    return data['email']

def verify(Name,email):
    import requests

    response = requests.get(
        "https://emailvalidation.abstractapi.com/v1/"+
        "?api_key=5bb2efb9013f4583b954971e1e867f55"+
        "&email="+email)

    k=response.json()
    if k['autocorrect']:
        return k['autocorrect']
    elif k['deliverability'] == 'DELIVERABLE':
        return email
    else:
        return  findemail(Name,email[email('@') + 1 : ]);

class Hosttest(LiveServerTestCase):


    def testhomepage(self):
        options = Options()
        #options.headless = True
        options.add_extension('addb.crx')
        driver = webdriver.Chrome('./chromedriver',options=options)
        driver.execute_script("window.stop();")
        driver.get('https://cxoreach.com/contacts/')
        original_window = driver.current_window_handle
        """print(len(driver.window_handles))
        #driver.switch_to.window(original_window)
        sleep(10)
        driver.switch_to.window(driver.window_handles[1])
        driver.close()
        driver.switch_to.window(original_window)"""
        element = driver.find_elements(By.CLASS_NAME, 'card')
        for row in element:
            col4 = row.find_element(By.CLASS_NAME, 'col-sm-4')
            Name = col4.find_element(By.TAG_NAME,'a').text
            Designation = col4.find_element(By.TAG_NAME,'span').text
            Company = row.find_element(By.CLASS_NAME, 'text-decoration-none').text
            col3 = row.find_element(By.CLASS_NAME, 'col-sm-3')
            col3.find_element(By.CSS_SELECTOR, "a").send_keys(Keys.CONTROL+Keys.SHIFT+Keys.RETURN)
            driver.switch_to.window(driver.window_handles[2])
            emailad=driver.find_element(By.CSS_SELECTOR,"body > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > p:nth-child(8) > a:nth-child(1)").text
            #driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL+'W')
            driver.close()
            driver.switch_to.window(original_window)
            #Email=verify(emailad,Name)
            print({"Name":Name,
                   "Designation":Designation,
                   "Company":Company,
                   "E":emailad})












