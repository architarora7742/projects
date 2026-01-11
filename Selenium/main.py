from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
# driver.get("https://www.amazon.in/Spigen-Passport-Documents-Organizer-Passports/dp/B0CX3LKDCH/ref=sr_1_4?crid=146B11YW437NW&dib=eyJ2IjoiMSJ9.At61DZq38TEiYnmI5kWRGyxewN28_ECHn-oFRnOreJunLb1CM_XW1I8SvpPPf4qAfBuaZ3TVEPd4VXot3TRpp5-XvAOkpSDGVMhBIQjHkxoU96V-3AhOyL1JyXnYxwwECyBrHSYJ2nzmRGpzlzuP1Cu8m6M4l2aPZAn8UhhMlFSN9cp9kemx547UwjhmkBCH09zqYeeEUP9GEpJ1Yhi01v_mYcbQJSmF31YTGKayyaU.VrWHOtpA_u82eaj39oDiIyWJPrpsFZBm0l0YKpcPgxk&dib_tag=se&keywords=spigen&qid=1758115723&sprefix=spigen%2Caps%2C311&sr=8-4")
#
#
# price_dollar = driver.find_element(By.CLASS_NAME, value="a-price-whole")
# print(f'The Price is {price_dollar.text}')

driver.get("https://www.python.org")

search_bar = driver.find_element(By.NAME, value="q")
print(search_bar)
# It will give you the selenium element or selenium object

print(search_bar.tag_name)
print(search_bar.get_attribute("placeholder"))
# The most commonly used selenium function is find element by name, and it is really useful while filling out web forms because most forms will have elements that are organized by NAME because when the form is submitted, the name is carried along with the value of the inputs.

button = driver.find_element(By.ID, value="submit")
print(button.size)

# ! Selenium is really powerful and the ability to use their helper methods to find element by id, name or class name allows us to pretty much reach into any website that we want.

documentation_link = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")
print(documentation_link.text)

# If all of these methods fail, then we have one more method of selecting elements by using XPATH
# The XPATH is a way of locating an HTML element by a path structure.

books_link = driver.find_element(By.XPATH, value='//*[@id="container"]/li[3]/ul/li[8]/a')
print(books_link.text)



driver.quit()

# driver.close()
# driver.quit()
# driver.close() well closes a single tab, the active tag where you have opened up a particular page.
# driver.quit() is going to close the entire browser and all the tabs along with it.
