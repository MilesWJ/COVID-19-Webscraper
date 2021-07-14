from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PATH = "/Users/milesjames/Documents/Programming/Code Projects/COVID-19 Webscraper/chromedriver"
DRIVER = webdriver.Chrome(PATH)

DRIVER.set_window_position(-10000, 0)

DRIVER.get("https://www.cdc.gov/coronavirus/2019-ncov/index.html")

CASES_ELEMENT = "status-cases-total"
DEATHS_ELEMENT = "status-deaths-total"
VACCINES_ELEMENT = "status-total-vaccines"


def data_selection():
    print("\n1. Total amount of COVID-19 cases in United States")
    print("2. Total amount of COVID-19 related deaths in the United States")
    print("3. Total amount of administered vaccines in the United States")

    while True:
        number = input("\nWhich set of data would you like to view? ")

        if number.isdigit() and 1 <= int(number) <= 3:
            return int(number)

        else:
            print(
                f"Invalid selection input: {number}. Must be a number between 1 and 3.")
            continue


def retrieve_data(data):
    try:
        search = WebDriverWait(DRIVER, 10).until(
            EC.presence_of_element_located((By.ID, data))
        ).text
        return search
    except:
        if data == "status-cases-total":
            print(
                f"\nAn error has occurred while searching for total cases! HTML ELEMENT: {data}.")
        elif data == "status-deaths-total":
            print(
                f"\nAn error has occurred while searching for total cases! HTML ELEMENT: {data}.")
        else:
            print(
                f"\nAn error has occurred while searching for total administered vaccines! HTML ELEMENT: {data}.")

        DRIVER.quit()


def view_data():
    print("\nNOTE: All data is from the CDC's website: https://www.cdc.gov/coronavirus/2019-ncov/index.html")

    if data_selection() == 1:
        data = retrieve_data(CASES_ELEMENT)
        print(f"\nUnited States COVID-19 case count: {data}.")
        DRIVER.quit()

    elif data_selection() == 2:
        data = retrieve_data(DEATHS_ELEMENT)
        print(f"\nUnited States COVID-19 related death count: {data}.")
        DRIVER.quit()

    else:
        data = retrieve_data(VACCINES_ELEMENT)
        print(
            f"\nUnited States COVID-19 vaccine administration count: {data}.")
        DRIVER.quit()


if __name__ == "__main__":
    view_data()
