# FIRST

1. Run `pip install`. You're also gonna need a `.env` file
2. Download a chromedriver for your OS type [here](https://chromedriver.chromium.org/downloads)
    - Make sure it matches your Chrome's version in the Chrome menu > Help > About Google Chrome
    - Remember the **path** of where you put the `chromedriver.exe` executable, unzipped
    - Yes, I'm keeping this hinging on Chrome, hate me later

## SECOND

B. Put the appropriate variables in your `.env` file (variables with example values below):

- You'll put that **path** for `chromedriver.exe` in place of the example `CHROME_DRIVER` value
- If you peek at the code, you'll notice it too has defaults -- Windows, vs the below Linux for Windows

```python
WEBSITE=http://topps.diku.dk/torbenm/maps.msp
ZOOM=10
HORIZ_STEP=10
VERT_STEP=10
MAX_SAMPLE=10
END_FOLDER=./exports/
CHROME_DRIVER="/mnt/c/Program Files (x86)/Google/Chrome/Application/chromedriver.exe"
```

### THIRD

III. Pretend like I'm not decrementing these headers

# FOURTH

- Just... just run the script. It'll use the configs, and step as appropriate

  - world-script.py
