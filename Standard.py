from selenium import webdriver                                      # import the web driver
from selenium.webdriver.common.keys import Keys                     # import Keys to use enter for example
from selenium.webdriver.common.by import By                         # Import By
from selenium.webdriver.support.ui import WebDriverWait             # Import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC    # Import expected conditions
import time                                                         # import time module

PATH = "/Users/Kevin/Downloads/Bots/chromedriver"                   # set the path to the chrome driver
driver = webdriver.Chrome(PATH)                                     # initialise the driver with path
SITE = "https://www.techwithtim.net/"                               # state the website

driver.get(SITE)                                                    # open the website
title = driver.title                                                # get the title of the webpage
time.sleep(5)                                                       # wait for 5 seconds
source_code = driver.page_source                                    # source code of the webpage

# hierarchy for accessing HTML elements: 1. ID 2. Name 3. Class

search = driver.find_element_by_name("s")                           # find HTML element by name
search.send_keys("test")                                            # enter "test" in search HTML element
search.send_keys(Keys.RETURN)                                       # press return = enter key

try:
    main = WebDriverWait(driver, 10).until(                         # wait 10 seconds
        EC.presence_of_element_located((By.ID, "main"))             # find HTML element by ID, Name or Class
    )

    articles = main.find_elements_by_tag_name("article")            # find HTML element by tag name
    for article in articles:                                        # loop over found articles
        header = article.find_element_by_class_name("entry-summary")
        print(header.text)

finally:
    driver.quit()                                                   # close the entire browser

driver.close()                                                      # close the tab (not the browser)
driver.quit()                                                       # close the entire browser
