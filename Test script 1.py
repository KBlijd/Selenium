from selenium import webdriver                                      # import the web driver
from selenium.webdriver.common.keys import Keys                     # import Keys to use enter for example
from selenium.webdriver.common.by import By                         # Import By
from selenium.webdriver.support.ui import WebDriverWait             # Import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC    # Import expected conditions
import time                                                         # import time module
from selenium.webdriver.common.action_chains import ActionChains    # import Action Chains

PATH = "/Users/Kevin/Downloads/Bots/chromedriver"                   # set the path to the chrome driver
driver = webdriver.Chrome(PATH)                                     # initialise the driver with path
SITE = "https://www.spellenrijk.nl/artikel/25416/pokemon-sword-shield-sleeved-boosterpack.html"  # state the website

driver.get(SITE)                                                    # open the website
time.sleep(5)                                                       # wait for 5 seconds

# hierarchy for accessing HTML elements: 1. ID 2. Name 3. Class

ID = driver.find_element_by_id("ContentPlaceHolder1_btnAddToCart")  # find HTML element by ID

actions = ActionChains(driver)                                      # specify Action Chains
actions.move_to_element(ID)                                         # move cursor to HTML element
actions.click(ID)                                                   # click where cursor is at that moment
actions.perform()                                                   # execute the actions

time.sleep(3)                                                       # wait for 5 seconds
actions = ActionChains(driver)                                      # specify Action Chains
ID = driver.find_element_by_class_name("buypop-orderbutton")        # find HTML element by class
actions.move_to_element(ID)                                         # move cursor to HTML element
actions.click(ID)                                                          # wait for 5 seconds
actions = ActionChains(driver)                                      # specify Action Chains
ID = driver.find_element_by_id("txt_row_id_6916321")                # find HTML element by ID
actions.move_to_element(ID)                                         # move cursor to HTML element
ID.clear()
actions.click(ID)                                                   # click where cursor is at that moment
ID.send_keys("10")
actions.perform()                                                   # execute the actions



