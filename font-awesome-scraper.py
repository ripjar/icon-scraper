from selenium import webdriver
import time
import pyperclip
import string

driver = webdriver.Chrome()

# Replace 'https://www.example.com' with the URL of the website you want to automate
url = 'https://fontawesome.com/search?o=r&m=free&new=yes'
driver.get(url)

# Wait for the page to load (you can adjust the sleep time as needed)
time.sleep(10)

output_file = 'fontawesome_output.txt'

f = open(output_file, "w")

for x in range (1, 100): 
    # Find the element you want to click and click on it
    element_to_click = driver.find_element('xpath', f'/html/body/div[1]/div/main/div/div/div/div/div[2]/div[3]/article[{x}]/button')
    element_to_click.click()

    # Wait for the clicked element to load (you can adjust the sleep time as needed)
    time.sleep(1)

    # Get the name of the icon
    icon_name = driver.find_element('xpath', '/html/body/div[1]/div/main/div/div/div/div/div[2]/div[4]/article/div/div/div[1]/div[1]/div/button[1]').text
    icon_name = icon_name.replace("Copy\n", "")#.rstrip()

    # Find the "Copy" button you want to click and click on it
    button_to_copy = driver.find_element('xpath', '/html/body/div[1]/div/main/div/div/div/div/div[2]/div[4]/article/div/div/div[1]/div[2]/dl[2]/dd/button')
    button_to_copy.click()

    # Wait for the button action to complete (you can adjust the sleep time as needed)
    time.sleep(1)

    f.write('{ "id": "' + icon_name + '", "glyph": "')

    f.write(pyperclip.paste())

    f.write('", "label": "' + string.capwords(icon_name.replace("-", " ")) + '" },\n')

    close_button_to_click = driver.find_element('xpath', '/html/body/div[1]/div/main/div/div/div/div/div[2]/div[4]/article/button')
    close_button_to_click.click()

f.close()

# Close the browser
driver.quit()