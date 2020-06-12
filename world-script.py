from pathlib import Path

# setup environment
from dotenv import load_dotenv
load_dotenv()

# Selenium Block
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
    driver.get(WEBSITE)
    img_tag = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "img")))
    with open(os.path.join(END_FOLDER, 'filename.png'), 'wb') as file:
        file.write(img_tag.screenshot_as_png)
finally:
    driver.quit()
