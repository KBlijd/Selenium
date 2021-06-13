from selenium import webdriver                                      # import the web driver
from selenium.webdriver.common.action_chains import ActionChains    # import Action Chains

PATH = "/Users/Kevin/Downloads/Bots/chromedriver"                   # set the path to the chrome driver
driver = webdriver.Chrome(PATH)                                     # initialise the driver with path
SITE = "https://orteil.dashnet.org/cookieclicker/"                   # state the website

driver.get(SITE)                                                    # open the website

driver.implicitly_wait(5)                                           # wait for 5 seconds

cookie = driver.find_element_by_id("bigCookie")                     # find HTML element by ID
cookie_count = driver.find_element_by_id("cookies")                 # find HTML element by ID
items = [driver.find_element_by_id("productPrice" + str(i)) for i in range(1, -1, -1)]  # make list for possible products

actions = ActionChains(driver)                                      # specify Action Chains
actions.click(cookie)                                               # click where cursor is at that moment

for i in range(5000):                                               # loop for 5000 times
    actions.perform()                                               # perform Action Chains
    count = int(cookie_count.text.split(" ")[0])                    # check how many cookies we have
    for item in items:                                              # loop over items
        value = int(item.text)                                      # store value of the item as value
        if value <= count:                                          # if value smaller or equal to our count
            upgrade_actions = ActionChains(driver)                  # initialise upgrade actions
            upgrade_actions.move_to_element(item)                   # move cursor to HTML element
            upgrade_actions.click()                                 # click HTML element
            upgrade_actions.perform()                               # perform upgrade actions