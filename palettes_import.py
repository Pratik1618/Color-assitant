from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.action_chains import ActionChains
import time

PART_SIZE = 4
URL = "https://colorhunt.co/palettes/popular"
CHROME_DRIVER_PATH = "/home/jayesh/drivers/chromedriver"


# l = [1, 2, 3, 4, 5, 6, 7, 8] -> [[1, 2, 3, 4], [5, 6, 7, 8]]
def separate_colors_codes(colors_codes_list):
    separated_colors_codes_list = []
    j = 0
    for i in range(0, int(len(colors_codes_list)/PART_SIZE)):
        separated_colors_codes_list.append(colors_codes_list[j:j+4])
        j += 4
    return separated_colors_codes_list

# will remove span tags and only return text
def remove_span_tag(colors_codes_list_span):
    colors_codes_list = []
    for i in range(4, len(colors_codes_list_span)):
        colors_codes_list.append(colors_codes_list_span[i].text)
    return colors_codes_list


# return all time popular colors codes in list
def all_time_data():
    
    all_time_button = driver.find_element_by_xpath(
        '/html/body/div[4]/div[1]/div[1]/div[3]')
    action_chain = ActionChains(driver) #for double click the button
    ActionChains(driver).double_click(all_time_button).perform()
    time.sleep(10)
    soup = BeautifulSoup(driver.page_source, "html.parser")
    colors_codes_list_span = soup.select('.place span')
    return remove_span_tag(colors_codes_list_span)
    

# return monthly popular colors codes in list
def month_data():
    time.sleep(10)
    soup = BeautifulSoup(driver.page_source, "html.parser")
    colors_codes_list_span = soup.select('.place span')
    return remove_span_tag(colors_codes_list_span)


# return yearly popular colors codes in list
def year_data():
    all_time_button = driver.find_element_by_xpath(
        '/html/body/div[4]/div[1]/div[1]/div[2]')
    action_chain = ActionChains(driver) #for double click the button
    ActionChains(driver).double_click(all_time_button).perform()
    time.sleep(10)
    soup = BeautifulSoup(driver.page_source, "html.parser")
    colors_codes_list_span = soup.select('.place span')
    return remove_span_tag(colors_codes_list_span)


try:
    option = ChromeOptions()
    option.headless = True
    driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH, options= option)
    driver.get(URL)
except:
    print("Exception")
else:
    month_data_list = separate_colors_codes(month_data())
    year_data_list = [i for i in separate_colors_codes(year_data()) if i not in month_data_list ] #remove duplicated data
    all_time_data_list = [i for i in separate_colors_codes(all_time_data()) if i not in month_data_list ] #remove dup data
    all_time_data_list = [i for i in all_time_data_list if i not in year_data_list ] #remove dup data

finally:
    driver.quit()
