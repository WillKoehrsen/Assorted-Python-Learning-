import selenium
from selenium import webdriver
import time

url = 'http://www.phptravels.net/login'

username = "user@phptravels.com"
password = "demouser"

# initilize Chrome, webdriver allows program to manipulate a webpage
driver = webdriver.Chrome()
if __name__ == "__main__":

    # go to the url
    driver.get(url)
    
    # find the username box on webpage
    uname = driver.find_element_by_name('username')
    # input the username into the box
    uname.send_keys(username)

    #find the password box on webpage
    passwd = driver.find_element_by_name('password')
    # input the password into the box
    passwd.send_keys(password)

    submit_button = driver.find_element_by_class_name('loginbtn').click()

    

    WebDriverWait(driver, 100).until(lambda driver: driver.find_element_by_id('bookings'))
    divs = driver.find_element_by_id('bookings')
    rows = driver.find_elements_by_class_name('row')

    print ('---------------------------------------')
    for row in rows:
        name = row.find_element_by_tag_name('a')
        print(name.text)