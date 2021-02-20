from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import webbrowser

'''
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://www.depts.ttu.edu/communications/emergency/coronavirus/")
tech_COVID_Data = driver.find_element_by_xpath("//table")
print(tech_COVID_Data.text + "\n")


driver.get("https://www.depts.ttu.edu/recsports/facilities/hours.php")
TTU_Rec_Hours =driver.find_element_by_xpath("//*[@id='calendar']")
print(TTU_Rec_Hours.text + "\n")

driver.get("https://cal.library.ttu.edu/hours/")
TTU_library_Hours = driver.find_element_by_xpath("//*[@id='s-lc-box-14040-container-tab0']/div")
print(TTU_library_Hours.text)
'''


def get_news():
    PATH1 = "C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome(PATH1)

    driver.get("https://www.google.com/")
    news_things = driver.find_element_by_xpath("/html/body/div[1]/div[3]/form/div[2]/div[1]/div[1]/div/div[2]/input")
    news_things.send_keys("ttu news")
    news_things.send_keys(Keys.RETURN)

    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='hdtb-msb']/div[1]/div/div[2]/a")))
    element.click()

    first_News_link = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='rso']/div[1]/g-card/div/div/div[2]/a")))
    print(first_News_link.get_attribute("href"))
    first_News = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='rso']/div[1]/g-card/div/div/div[2]/a/div/div[2]/div[2]")))
    print(first_News.text + '\n')

    second_News_link = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='rso']/div[2]/g-card/div/div/div[2]/a")))
    print(second_News_link.get_attribute("href"))
    second_News = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,"//*[@id='rso']/div[2]/g-card/div/div/div[2]/a/div/div[2]/div[2]")))
    print(second_News.text + '\n')

    third_News_link = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='rso']/div[3]/g-card/div/div/div[2]/a")))
    print(third_News_link.get_attribute("href"))
    third_News = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,"//*[@id='rso']/div[3]/g-card/div/div/div[2]/a/div/div[2]/div[2]")))
    print(third_News.text)
    driver.close()


def get_covid_stats():
    PATH = "C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome(PATH)

    driver.get("https://www.depts.ttu.edu/communications/emergency/coronavirus/")
    tech_COVID_Data = driver.find_element_by_xpath("//table")
    print(tech_COVID_Data.text + "\n")
    driver.close()


def get_rec_times():
    PATH = "C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome(PATH)

    driver.get("https://www.depts.ttu.edu/recsports/facilities/hours.php")
    TTU_Rec_Hours =driver.find_element_by_xpath("//*[@id='calendar']")
    print(TTU_Rec_Hours.text + "\n")
    driver.close()


def get_lib_times():
    PATH1 = "C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome(PATH1)

    driver.get("https://cal.library.ttu.edu/hours/")
    TTU_library_Hours = driver.find_element_by_xpath("//*[@id='s-lc-box-14040-container-tab0']/div")
    print(TTU_library_Hours.text)
    driver.close()


get_news()
get_lib_times()
get_rec_times()
get_covid_stats()