# icon-scraper
Python script using selenium to scrape a webpage for glyphs. This particular example connects to the font-awesome website's icon library and simulates the action of clicking and copy-pasting icons into a file.  
You will have to leave the script running and not do anything else until it's completed otherwise it will interrupt the automated clicking actions. Not ideal, but still better than having to do all the copy-pasting manually!  

You can use this script as a guide or template for connecting to a website of your choosing and scraping icons from there. It's likely you'll have to modify the code to work with the HTML structure of the webpage you are automating actions on, but the example script may be good as a starting point.

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
  
The file example_fontawesome_output.txt shows what the output file contents looks like.