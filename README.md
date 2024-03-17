# Web Scraper

This is a Python script that uses Selenium to scrape data from a website and stores the data in an Excel file.

## Prerequisites

Before you begin, ensure you have met the following requirements:

* You have installed the latest version of [Python](https://www.python.org/downloads/).
* You have a Windows machine. This code may work on other operating systems but it was developed and tested on Windows.
* You have installed the Selenium Python package. You can install it with pip:   pip install selenium*
* You have installed the webdriver_manager Python package. You can install it with pip: pip install webdriver-manager*

* You have installed the [Chrome browser](https://www.google.com/chrome/). The script uses the Chrome browser for web scraping.

## Setting up ChromeDriver

The script uses ChromeDriver to interact with the Chrome browser. Here's how to set it up:

1. Visit the [ChromeDriver download page](https://sites.google.com/a/chromium.org/chromedriver/downloads).
2. Download the version of ChromeDriver that matches the version of your installed Chrome browser.
3. Extract the downloaded file to retrieve `chromedriver.exe`.
4. Add the location of `chromedriver.exe` to your system's PATH.

### Adding ChromeDriver to PATH on Windows

1. Right-click on 'This PC' or 'My Computer' and click on 'Properties'.
2. Click on 'Advanced system settings'.
3. Click on 'Environment Variables...'.
4. In the 'System variables' section, find the 'Path' variable, select it and click on 'Edit...'.
5. In the 'Variable value' field, append the path to the `chromedriver.exe` file. Make sure to separate it from the existing paths with a semicolon (;).
6. Click 'OK' to close all dialog boxes.

Now, your script should be able to use ChromeDriver to control the Chrome browser.

## Using Web Scraper

To use the web scraper, follow these steps:

1. Open your terminal.
2. Navigate to the directory where `scraper.py` is located.
3. Run the script with the command `python scraper.py`.
4. When prompted, enter your search query.
5. The script will scrape the data and store it in an Excel file in the same directory.

## Contact

If you want to contact me you can reach me at `rajamuhammadwajahat2003@gmail.com`.