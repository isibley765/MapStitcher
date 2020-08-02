from pathlib import Path

# setup environment
from dotenv import load_dotenv
load_dotenv()

# Selenium Block
from selenium import webdriver

from selenium.webdriver.remote.webelement import WebElement

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import cv2
import os

def getEnvVariable(var, default=None):
    res = None
    if (type(var) == str):
        print(var)
        res = os.getenv(var)
    
    return res if res != None else default

WEBSITE = getEnvVariable("WEBSITE", "http://topps.diku.dk/torbenm/maps.msp")
ZOOM = int(getEnvVariable("ZOOM", 15))
HORIZ_STEP = int(getEnvVariable("HORIZ_STEP", 10))
VERT_STEP = int(getEnvVariable("VERT_STEP", 10))
MAX_SAMPLE = int(getEnvVariable("MAX_SAMPLE", 10))
END_FOLDER = getEnvVariable("END_FOLDER", "./exports/")
Path(END_FOLDER).mkdir(parents=True, exist_ok=True)
CHROME_DRIVER = getEnvVariable("CHROME_DRIVER", r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe")

driver = webdriver.Chrome(CHROME_DRIVER)

try:

    driver.maximize_window()
    driver.get(WEBSITE)

    # set initial perameters

    seed = driver.find_element_by_name('seed')
    seed.clear()
    seed.send_keys('12971253')

    projection = driver.find_element_by_xpath("//select[@name='projection']/option[@value='q']").click()

    width = driver.find_element_by_name('width')
    width.clear()
    width.send_keys('500')

    color = driver.find_element_by_xpath("//select[@name='colourmap']/option[@value='greyscale.col']").click()

    height = driver.find_element_by_name('height')
    height.clear()
    height.send_keys('500')

    zoom = driver.find_element_by_name('zoom')
    zoom.clear()
    zoom.send_keys('360')

    water = driver.find_element_by_name('water')
    water.clear()
    water.send_keys('-0.035')

    # loop through coordinates

    Loop = 3
    filename = 'Etaros'
    imgArray = []

    for y in range(Loop):
        centLat = driver.find_element_by_name('longi')
        centLat.clear()
        centLat.send_keys(str(-2.5 - y))

        if y != 0:
            img = cv2.vconcat(imgArray)
            cv2.imwrite(END_FOLDER + 'vertical' + str(x) + '.png', img)
            imgArray.clear()

        for x in range(Loop):

            centerLong = driver.find_element_by_name('lati')
            centerLong.clear()
            centerLong.send_keys(str(-102.5 + x))

            submitButton = driver.find_element_by_xpath("//input[@type='submit' and @value='Make map']")
            submitButton.submit()

            img_tag = WebDriverWait(driver, 10).until(
                 EC.presence_of_element_located((By.TAG_NAME, "img")))

            with open(os.path.join(END_FOLDER, filename + '_' + str(x) + '_' + str(y) + '.png'), 'wb') as file:
                file.write(img_tag.screenshot_as_png)

            image = cv2.imread(END_FOLDER + filename + '_' + str(x) + '_' + str(y) + '.png')

            imgArray.append(image)
finally:
    driver.quit()
