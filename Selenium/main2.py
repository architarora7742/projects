from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.python.org")


time_list = driver.find_elements(By.CSS_SELECTOR, value=".last .menu time")
print(time_list)
for i in time_list:
    print(i.text)


event_info_list = driver.find_elements(By.CSS_SELECTOR, value=".event-widget .shrubbery .menu a")
for i in event_info_list:
    print(i.text)

# time_data = driver.find_elements(By.CLASS_NAME, value="menu")
# for i in time_data:
#     print(i.text)

dict = {time_list.index(key): {key.text: value.text} for key, value in zip(time_list, event_info_list)}
print(dict)

due = {time_list.index(key): {"time": key.text, "name": value.text} for key, value in zip(time_list, event_info_list)}
print(due)
duck = {}
for n in range(len(event_info_list)):
    duck[n] = {
        "time": time_list[n].text,
        "name": event_info_list[n].text
    }
print(duck)
# no code should be written after driver.quit()
driver.quit()
