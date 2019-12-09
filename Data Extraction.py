from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import csv
import pdb
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
driver = webdriver.Firefox(executable_path = r'C:\Users\user\geckodriver')
url = ('https://www.3gpp.org/')
driver.get(url)
window_before = driver.window_handles[0]
print (window_before)
time.sleep(5)
while True:
    mainmenu = driver.find_element_by_class_name('topmainmenu')
    li2 = mainmenu.find_element_by_id('nav')
    li3 = li2.find_element_by_link_text('Specifications Groups')
    li3.click()
    ran1 = driver.find_element_by_class_name('title_org')
    ran2 = ran1.find_element_by_link_text('RAN WG1')
    ran2.click()
    time.sleep(10)
    tableclass = driver.find_element_by_tag_name('table')
    table1= tableclass.find_element_by_tag_name('tbody')
    meet =table1.find_element_by_xpath('//tbody/tr[5]/td[2]/a')
    meet.click()
    time.sleep(10)
    window_after = driver.window_handles[1]
    driver.switch_to.window(window_after)
    print(driver.current_url)
    time.sleep(10)
    t_body = driver.find_element_by_class_name('column-three-thirds')
    xlxx = t_body.find_element_by_tag_name('table')
    xlxx2 = xlxx.find_element_by_tag_name('tbody')
    xlxx3 = xlxx2.find_elements_by_xpath('//tbody/tr[]/td[6]/a[1]')
    for i in xlxx3:
        if xlxx3 != "-":
            xlxx3.click()
    time.sleep(10)
    window_after1 = driver.window_handles[2]
    driver.switch_to.window(window_after1)
    print (driver.current_url)
    parent = driver.find_element_by_tag_name('body')
    parent1 = driver.find_element_by_link_text('[To Parent Directory]').click()
    rep1 = driver.find_element_by_link_text('Report').click()
    body =driver.find_element_by_tag_name('body')
    pre = body.find_element_by_tag_name('pre')
    links = pre.find_elements_by_tag_name('a')
    for i in links:
        print(i.get_attribute('href'))
    i.click()
    driver.switch_to.window(window_before)
