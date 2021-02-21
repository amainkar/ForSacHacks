from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urllib.parse import unquote
import json
import requests

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

    news_obj = {"article1_link": unquote(first_News_link.get_attribute("href")),
                "article1_text": first_News.text,
                "article2_link": unquote(second_News_link.get_attribute("href")),
                "article2_text": second_News.text,
                "article3_link": unquote(third_News_link.get_attribute("href")),
                "article3_text": third_News.text,
                }
    driver.close()
    return news_obj


def get_covid_stats():
    PATH = "C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome(PATH)

    driver.get("https://www.depts.ttu.edu/communications/emergency/coronavirus/")
    tech_covid_data = driver.find_element_by_xpath("//table")
    print(tech_covid_data.text + "\n")

    tech_covid_data_list = tech_covid_data.text.split('\n')
    header = tech_covid_data_list[0]
    date_of_report = tech_covid_data_list[1]
    students = list()
    employees = list ()
    total = list()

    for x in range(0, len(tech_covid_data_list)):
        if x > 2:
            students.append(tech_covid_data_list[x].split(" ")[2])
            employees.append(tech_covid_data_list[x].split(" ")[3])
            total.append(tech_covid_data_list[x].split(" ")[4])

    print(students, employees, total)

    covid_data_JSON = {"students": [{"total_reported": students[0],
                                     "new_recovered": students[1],
                                     "total_recovered": students[2],
                                     "new_active": students[3],
                                     "total_active": students[4]}],
                       "employees": [{"total_reported": employees[0],
                                      "new_recovered": employees[1],
                                      "total_recovered": employees[2],
                                      "new_active": employees[3],
                                      "total_active": employees[4]}],
                       "total": [{"total_reported": total[0],
                                  "new_recovered": total[1],
                                  "total_recovered": total[2],
                                  "new_active": total[3],
                                  "total_active": total[4]}]
                       }

    print(json.dumps(covid_data_JSON, indent = 1))

    driver.close()
    return covid_data_JSON


def get_rec_times():
    PATH = "C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome(PATH)

    driver.get("https://www.depts.ttu.edu/recsports/facilities/hours.php")
    TTU_Rec_Hours =driver.find_element_by_xpath("//*[@id='calendar']")
    print(TTU_Rec_Hours.text + "\n")

    ttu_rec_text_list = TTU_Rec_Hours.text.split('\n')
    print(ttu_rec_text_list)
    ttu_rec_info = list()

    for x in range(0, len(ttu_rec_text_list)):
        print(x)
        if x == 3:
            rec_date = ttu_rec_text_list[x] + " " + ttu_rec_text_list[0]
        if x > 3:
            ttu_rec_info.append(ttu_rec_text_list[x])

    ttu_rec_info_dict = dict()
    ttu_rec_info_dict.update({"given_date": rec_date})

    for x in range(0, len(ttu_rec_info)):
        ttu_rec_info_dict.update({("line" + str(x)): ttu_rec_info[x]})

    print(ttu_rec_info_dict)
    driver.close()
    return ttu_rec_info_dict

def get_lib_times():
    PATH1 = "C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome(PATH1)

    driver.get("https://cal.library.ttu.edu/hours/")

    TTU_library_sun = driver.find_element_by_xpath("//*[@id='s-lc-w-w1-14514']/table/thead/tr/th[2]").text.replace("\n", ", ")
    TTU_library_mon = driver.find_element_by_xpath("//*[@id='s-lc-w-w1-14514']/table/thead/tr/th[3]").text.replace("\n", ", ")
    TTU_library_tues = driver.find_element_by_xpath("//*[@id='s-lc-w-w1-14514']/table/thead/tr/th[4]").text.replace("\n", ", ")
    TTU_library_wed = driver.find_element_by_xpath("//*[@id='s-lc-w-w1-14514']/table/thead/tr/th[5]").text.replace("\n", ", ")
    TTU_library_thur = driver.find_element_by_xpath("//*[@id='s-lc-w-w1-14514']/table/thead/tr/th[6]").text.replace("\n",", ")
    TTU_library_fri = driver.find_element_by_xpath("//*[@id='s-lc-w-w1-14514']/table/thead/tr/th[7]").text.replace("\n", ", ")
    TTU_library_sat = driver.find_element_by_xpath("//*[@id='s-lc-w-w1-14514']/table/thead/tr/th[8]").text.replace("\n", ", ")

    univ_lib_stat_sun = driver.find_element_by_xpath("//*[@id='s-lc-w-w1-14514']/table/tbody/tr[1]/td[2]/span").text
    univ_lib_stat_mon = driver.find_element_by_xpath("//*[@id='s-lc-w-w1-14514']/table/tbody/tr[1]/td[3]/span").text
    univ_lib_stat_tues = driver.find_element_by_xpath("//*[@id='s-lc-w-w1-14514']/table/tbody/tr[1]/td[4]/span").text
    univ_lib_stat_wed = driver.find_element_by_xpath("//*[@id='s-lc-w-w1-14514']/table/tbody/tr[1]/td[5]/span").text
    univ_lib_stat_thur = driver.find_element_by_xpath("//*[@id='s-lc-w-w1-14514']/table/tbody/tr[1]/td[6]/span").text
    univ_lib_stat_fri = driver.find_element_by_xpath("//*[@id='s-lc-w-w1-14514']/table/tbody/tr[1]/td[7]/span").text
    univ_lib_stat_sat = driver.find_element_by_xpath("//*[@id='s-lc-w-w1-14514']/table/tbody/tr[1]/td[8]/span").text

    arch_lib_stat_sun = driver.find_element_by_xpath("//*[@id='s-lc-w-w1-14514']/table/tbody/tr[2]/td[2]/span").text
    arch_lib_stat_mon = driver.find_element_by_xpath("//*[@id='s-lc-w-w1-14514']/table/tbody/tr[2]/td[3]/span").text
    arch_lib_stat_tues = driver.find_element_by_xpath("//*[@id='s-lc-w-w1-14514']/table/tbody/tr[2]/td[4]/span").text
    arch_lib_stat_wed = driver.find_element_by_xpath("//*[@id='s-lc-w-w1-14514']/table/tbody/tr[2]/td[5]/span").text
    arch_lib_stat_thur = driver.find_element_by_xpath("//*[@id='s-lc-w-w1-14514']/table/tbody/tr[2]/td[6]/span").text
    arch_lib_stat_fri = driver.find_element_by_xpath("//*[@id='s-lc-w-w1-14514']/table/tbody/tr[2]/td[7]/span").text
    arch_lib_stat_sat = driver.find_element_by_xpath("//*[@id='s-lc-w-w1-14514']/table/tbody/tr[2]/td[8]/span").text

    sth_lib_stat_sun = driver.find_element_by_xpath("//*[@id='s-lc-w-w1-14514']/table/tbody/tr[3]/td[2]/span").text
    sth_lib_stat_mon = driver.find_element_by_xpath("//*[@id='s-lc-w-w1-14514']/table/tbody/tr[3]/td[3]/span").text
    sth_lib_stat_tues = driver.find_element_by_xpath("//*[@id='s-lc-w-w1-14514']/table/tbody/tr[3]/td[4]/span").text
    sth_lib_stat_wed = driver.find_element_by_xpath("//*[@id='s-lc-w-w1-14514']/table/tbody/tr[3]/td[5]/span").text
    sth_lib_stat_thur = driver.find_element_by_xpath("//*[@id='s-lc-w-w1-14514']/table/tbody/tr[3]/td[6]/span").text
    sth_lib_stat_fri = driver.find_element_by_xpath("//*[@id='s-lc-w-w1-14514']/table/tbody/tr[3]/td[7]/span").text
    sth_lib_stat_sat = driver.find_element_by_xpath("//*[@id='s-lc-w-w1-14514']/table/tbody/tr[3]/td[8]/span").text

    law_lib_stat_sun = driver.find_element_by_xpath("//*[@id='s-lc-w-w1-14514']/table/tbody/tr[4]/td[2]/span").text
    law_lib_stat_mon = driver.find_element_by_xpath("//*[@id='s-lc-w-w1-14514']/table/tbody/tr[4]/td[3]/span").text
    law_lib_stat_tues = driver.find_element_by_xpath("//*[@id='s-lc-w-w1-14514']/table/tbody/tr[4]/td[4]/span").text
    law_lib_stat_wed = driver.find_element_by_xpath("//*[@id='s-lc-w-w1-14514']/table/tbody/tr[4]/td[5]/span").text
    law_lib_stat_thur = driver.find_element_by_xpath("//*[@id='s-lc-w-w1-14514']/table/tbody/tr[4]/td[6]/span").text
    law_lib_stat_fri = driver.find_element_by_xpath("//*[@id='s-lc-w-w1-14514']/table/tbody/tr[4]/td[7]/span").text
    law_lib_stat_sat = driver.find_element_by_xpath("//*[@id='s-lc-w-w1-14514']/table/tbody/tr[4]/td[8]/span").text


    lib_data_JSON = {
        "dates":[{
            "sun": TTU_library_sun,
            "mon": TTU_library_mon,
            "tues": TTU_library_tues,
            "wed": TTU_library_wed,
            "thur": TTU_library_thur,
            "fri": TTU_library_fri,
            "sat": TTU_library_sat
        }],
        "univ_lib":[{
            "sun": univ_lib_stat_sun,
            "mon": univ_lib_stat_mon,
            "tues": univ_lib_stat_tues,
            "wed": univ_lib_stat_wed,
            "thur": univ_lib_stat_thur,
            "fri": univ_lib_stat_fri,
            "sat": univ_lib_stat_sat
        }],
        "arch_lib": [{
            "sun": arch_lib_stat_sun,
            "mon": arch_lib_stat_mon,
            "tues": arch_lib_stat_tues,
            "wed": arch_lib_stat_wed,
            "thur": arch_lib_stat_thur,
            "fri": arch_lib_stat_fri,
            "sat": arch_lib_stat_sat
        }],
        "sth_lib": [{
            "sun": sth_lib_stat_sun,
            "mon": sth_lib_stat_mon,
            "tues": sth_lib_stat_tues,
            "wed": sth_lib_stat_wed,
            "thur": sth_lib_stat_thur,
            "fri": sth_lib_stat_fri,
            "sat": sth_lib_stat_sat
        }],
        "law_lib": [{
            "sun": law_lib_stat_sun,
            "mon": law_lib_stat_mon,
            "tues": law_lib_stat_tues,
            "wed": law_lib_stat_wed,
            "thur": law_lib_stat_thur,
            "fri": law_lib_stat_fri,
            "sat": law_lib_stat_sat
        }]
    }
    print(json.loads(json.dumps(lib_data_JSON)))
    driver.close()
    return lib_data_JSON

#get_news()
#get_lib_times()
#get_rec_times()
#get_covid_stats()