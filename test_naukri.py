from selenium import webdriver
from selenium.webdriver.support.select import Select


def test_navigate():
    dri = webdriver.Chrome()
    dri.get("https://www.naukri.com/account/createaccount?othersrcp=16201&err=1")
    dri.find_element_by_xpath('//button[@value="fresher"]').click()
    dri.find_element_by_xpath('//input[@id="fname"]').send_keys('amul')
    dri.find_element_by_id('email').send_keys('amul.kumar03@outlook.com')
    dri.find_element_by_name('password').send_keys('123456')
    dri.find_element_by_xpath('//input[contains(@name,"number")]').send_keys('9441615919')
    location = dri.find_element_by_name('city')
    s1= Select(location)
    s1.select_by_visible_text()



#test_navigate()
