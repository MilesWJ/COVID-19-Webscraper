from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PATH = "C:\Program Files (x86)\chromedriver.exe"
DRIVER = webdriver.Chrome(PATH)

DRIVER.set_window_position(-10000, 0)

DRIVER.get("https://www.cdc.gov/coronavirus/2019-ncov/index.html")

CASES = "status-cases-total"
DEATHS = "status-deaths-total"
VACCINES = "status-total-vaccines"


def retrieve_data(data):
    try:
        search = WebDriverWait(DRIVER, 10).until(
            EC.presence_of_element_located((By.ID, data))
        ).text
        return search
    except:
        DRIVER.quit()


def decide_data():
    while True:
        decide = abs(int(input("\n1. Total amount of COVID-19 cases in United States\n2. Total amount of COVID-19 related deaths in the United States\n3. Total amount of administered vaccines in the United States\nEnter the data number you would like to view: ")))
        if decide == 1:
            data = retrieve_data(CASES)
            print(f"\nUnited States COVID-19 case count: {data}")
            break
        elif decide == 2:
            data = retrieve_data(DEATHS)
            print(f"\nUnited States COVID-19 related death count: {data}")
            break
        elif decide == 3:
            data = retrieve_data(VACCINES)
            print(
                f"\nUnited States COVID-19 vaccine administration count: {data}")
            break
        else:
            print(f'Invalid data selector "{decide}". 1, 2, or 3.')
            continue


def display_data():
    print("\nNOTE: All data is from the CDC's website: https://www.cdc.gov/coronavirus/2019-ncov/index.html")
    decide_data()


display_data()
