from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
import requests

driver = webdriver.PhantomJS()
driver.delete_all_cookies()
driver.set_window_size(1024, 768)
driver.get('https://web.archive.org/web/*/gothamist.com/*')
time.sleep(60)
driver.find_element_by_id('positionTable').find_element_by_tag_name('input').clear()
driver.find_element_by_id('positionTable').find_element_by_tag_name('input').send_keys('php')
for foo in driver.find_element_by_id('positionTable').find_elements_by_tag_name('th'):
    if foo.get_attribute('class').strip()=="dateTo sorting":
        foo.click()
        foo.click()

print("Sorted...")
with open('output.txt',"w+") as f:
    for i in range(1,1700):
        print("Examining page "+str(i))
        for link in driver.find_element_by_id('positionTable').find_element_by_id('resultsUrl').find_element_by_tag_name('tbody').find_elements_by_tag_name('tr'):
            f.write(link.find_element_by_tag_name('a').get_attribute('href'))
            f.write('\n')

        driver.find_element_by_id('resultsUrl_next').click()

driver.save_screenshot('screen.png')
driver.quit()