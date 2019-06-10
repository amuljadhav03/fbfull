from selenium import webdriver
from selenium.webdriver.support.select import Select

bro = 'chrome'
if(bro =='chrome'):
    driver = webdriver.Chrome()
elif(bro =='firefox'):
    driver = webdriver.Firefox()
else:
    print("no browser path")
driver.implicitly_wait(30)
driver.get('https://www.facebook.com')
driver.find_element_by_name("firstname").send_keys("Amul")
driver.find_element_by_xpath('//input[contains(@aria-label,"Surname")]').send_keys('Jadhav')
driver.find_element_by_xpath('//*[@id="u_0_q"]').send_keys('7842474596')
driver.find_element_by_name("reg_passwd__").send_keys('1234')
a = driver.find_element_by_xpath('//*[@id="day"]')
day=Select(a)
day.select_by_value('15')
b = driver.find_element_by_id('month')
month = Select(b)
month.select_by_visible_text('Sept')
c =driver.find_element_by_id('year')
year = Select(c)
year.select_by_value('1991')
driver.find_element_by_xpath('//input[@value=2]').click()
driver.find_element_by_name('websubmit').click()



