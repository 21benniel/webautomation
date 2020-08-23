from selenium import webdriver
browser=webdriver.Chrome('C:\\chromed\\chromedriver.exe')
browser.get('https://www.facebook.com/')
mail_id="*****"
password="******"
name=browser.find_element_by_id("email")
name.send_keys(mail_id)
p=browser.find_element_by_id("pass")
p.send_keys(password)
login=browser.find_element_by_id("u_0_b")

login.click()