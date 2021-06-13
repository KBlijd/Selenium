from selenium import webdriver  # import the web driver
from selenium.webdriver.common.by import By  # Import By
from selenium.webdriver.support import expected_conditions as EC  # Import expected conditions
from selenium.webdriver.support.ui import WebDriverWait  # Import WebDriverWait

PATH = "/Users/Kevin/Downloads/Bots/chromedriver"  # set the path to the chrome driver
driver = webdriver.Chrome(PATH)  # initialise the driver with path
SITE = "https://www.techwithtim.net/"  # state the website

driver.get(SITE)  # open the website

link = driver.find_element_by_link_text("Python Programming")  # find HTML element by link text
link.click()  # click the link

try:
    element = WebDriverWait(driver, 10).until(  # wait for 10 seconds
        EC.presence_of_element_located((By.LINK_TEXT, "Beginner Python Tutorials"))  # find HTML element by LINK TEXT
    )
    element.clear()  # clear keys which might already be filled in
    element.click()  # click element

    element = WebDriverWait(driver, 10).until(  # wait for 10 seconds
        EC.presence_of_element_located((By.ID, "sow-button-19310003"))  # find HTML element by ID
    )
    element.click()  # click the element

    driver.back()  # go back 1 page
    driver.forward()  # go forward 1 page

except:
    driver.quit()  # quit the entire browser
