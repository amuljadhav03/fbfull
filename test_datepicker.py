

from selenium import webdriver
from selenium.webdriver.support.select import Select
def test_datepic():
 driver = webdriver.Chrome()
 driver.implicitly_wait(30)
 driver.get('https://jqueryui.com/datepicker/#dropdown-month-year')
 dpicker = driver.find_element_by_xpath("//iframe['@class=demo-frame']")
 driver.switch_to.frame(dpicker)
 driver.find_element_by_xpath("//input['@class=hasDatepicker']").click()
 month = driver.find_element_by_class_name('ui-datepicker-month')
 s = Select(month)
 s.select_by_visible_text('Sep')
 year = driver.find_element_by_class_name('ui-datepicker-year')
 s1 = Select(year)
 s1.select_by_value('2015')
 driver.find_element_by_xpath("//*[@id='ui-datepicker-div']/table/tbody/tr[3]/td[7]/a").click()