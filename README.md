# astroGo_remote

## Configuration

To set up astroGo_remote on your machine, please ensure that Python and Google Chrome are installed
<br>

Then run `pip install selenium`

Create a `credentials.env` file in the same directory with the variable:
```
DIRECTORY=<USER_DATA_DIRECTORY>
```
Replace `<USER_DATA_DIRECTORY>` with your Google Chrome User Data Directory which can usually be found under `C:/Users/<YOUR_NAME>/AppData/Local/Google/Chrome/User Data`

## Initialization

To use astroGo_remote, first ensure that you have preiously logged in to Astro Go in your Google Chrome browser

Then, with your Google Chrome browser closed, simply run `python astroGo_browser.py` in the same directory as the repo

`astroGo_browser.py` will open up Astro Go in Google Chrome and begin pre-loading all the channels

Once completed, the console will output `completed pre-loading all channels`, after which you can enter a channel number to begin watching
