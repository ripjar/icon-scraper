# icon-scraper
Python script using selenium to scrape a webpage for glyphs.

## Requirements
You will need Python 3 to run the script. I specifically used 3.10.8, but any minor version should do.
  
At the moment, this only works with Chrome. Install the appropriate ChromeDriver for your operating system [here](https://chromedriver.chromium.org/downloads)

Also, you will need the following python packages:
* selenium 4.10
* webdriver-manager 3.9.1
* pyperclip 1.8.2

Once you have these dependencies installed you should be able to run the example:
```
    python font-awesome-scraper.py
```
The script will write the glyphs to a file in JSON format, along with an icon "id" and "label".
This can be pasted into the icons array of the font configuration block of a Labyrinth Investigations schema.