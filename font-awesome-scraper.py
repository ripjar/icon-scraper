from selenium import webdriver
import time
import pyperclip
import string
import os

driver = webdriver.Chrome()

# The file to save the icons to
output_file = 'fontawesome_output.txt'

# Set the URL of the website you want to scrape from

# page 1, alphabetical
url = 'https://fontawesome.com/search?o=a&m=free&new=yes'

# page 2, alphabetical
# url = 'https://fontawesome.com/search?p=2&o=a&m=free&new=yes'

# TODO: Make it so that if there is already content in the output file, the script can pick up where it left off scraping the webpage.
if os.path.isfile(output_file):
    f = open(output_file, "r")
    n_lines = len(f.readlines())
    print("num lines=" + str(n_lines))
    f.close()

driver.get(url)

# Wait for the page to load
time.sleep(10)

# Open the output file for writing and reading in "append" mode
f = open(output_file, "a+")

for x in range (1, 181): 
    # Find the element you want to click and click on it
    element_to_click = driver.find_element('xpath', f'/html/body/div[1]/div/main/div/div/div/div/div[2]/div[3]/article[{x}]/button')
    element_to_click.click()

    # Wait for the modal to load
    time.sleep(1)

    # Get the name of the icon
    icon_name = driver.find_element('xpath', '/html/body/div[1]/div/main/div/div/div/div/div[2]/div[4]/article/div/div/div[1]/div[1]/div/button[1]').text
    icon_name = icon_name.replace("Copy\n", "")

    # Find the "Copy Glyph" button and click on it
    button_to_copy = driver.find_element('xpath', '/html/body/div[1]/div/main/div/div/div/div/div[2]/div[4]/article/div/div/div[1]/div[2]/dl[2]/dd/button')
    button_to_copy.click()

    # Wait for the button action to complete
    time.sleep(1)

    f.write('{ "id": "' + icon_name + '", "glyph": "')

    f.write(pyperclip.paste())

    f.write('", "label": "' + string.capwords(icon_name.replace("-", " ")) + '" },\n')

    close_button_to_click = driver.find_element('xpath', '/html/body/div[1]/div/main/div/div/div/div/div[2]/div[4]/article/button')
    close_button_to_click.click()

    # Wait for the button action to complete
    time.sleep(1)

f.close()

# Close the browser
driver.quit()