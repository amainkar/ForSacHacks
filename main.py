from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import webbrowser


PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://www.depts.ttu.edu/communications/emergency/coronavirus/")

tech_COVID_Data = driver.find_element_by_xpath("//table")
print(tech_COVID_Data.text + "\n")
driver.get("https://www.depts.ttu.edu/recsports/facilities/hours.php")
TTU_Rec_Hours =driver.find_element_by_xpath("//*[@id='calendar']")
print(TTU_Rec_Hours.text)
driver.close()