from selenium import webdriver
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("user-data-dir=C:/Users/kishe/AppData/Local/Google/Chrome/User Data") 
driver = webdriver.Chrome(options=chrome_options)
actions = webdriver.ActionChains(driver)

def homepage():
    url = 'https://astrogo.astro.com.my/hubGuide' # astro channel list url
    driver.get(url)

    time.sleep(5) # wait 10 seconds

    container = driver.find_element_by_xpath('/html/body/section/div/div[3]/div/div/div[2]/div[2]/div[1]/div[1]/div')

    channels = container.find_elements_by_tag_name('div')
    latest_channel = 0
    while latest_channel != channels[-1]: # keep running till the last channel is end of the list
        actions.move_to_element(channels[-1]).perform() # scroll till last loaded channel to load all available channels
        latest_channel = channels[-1]
        channels = container.find_elements_by_tag_name('div') # refresh list with newly loaded channels
    print('completed pre-loading all channels')

def readyState():
    channelNum = input()
    if driver.title != 'Home | Astro':
        homepage()
    watchingState(channelNum)

def watchingState(channelNum):
    container = driver.find_element_by_xpath('/html/body/section/div/div[3]/div/div/div[2]/div[2]/div[1]/div[1]/div')
    channels = container.find_elements_by_tag_name('div')

    i = 0
    for channel in channels:
        i += 1
        selectedChannel = driver.find_element_by_xpath('/html/body/section/div/div[3]/div/div/div[2]/div[2]/div[1]/div[1]/div/div[%2d]/div/div' % (i))
        if channelNum == selectedChannel.text:
            print(selectedChannel.text)
            actions.click(selectedChannel).perform()
            time.sleep(1)
            channelPage = driver.find_element_by_xpath('/html/body/section/div/div[3]/div/div/div[2]/div[2]/div[1]/div[1]/div/ul/li[1]')
            actions.click(channelPage).perform()
            while (driver.title == 'Home | Astro'):
                # wait until the page navigates away from 'Home | Astro'
                pass
            watchLive = driver.find_element_by_xpath('/html/body/section/div/div[3]/div/div/div[2]/div[1]/div[3]/div[2]/div[1]/div/div[1]')
            actions.click(watchLive).perform()
            time.sleep(2) # wait 2 seconds for load
            fullscreen = driver.find_element_by_xpath('/html/body/section/div/div[4]/div/div/div/div[2]/div[1]/div/span/div[1]/div/div[3]/div[2]/div[2]/div[3]/div')
            actions.click(fullscreen).perform()
            break
    readyState()

homepage()
readyState()

# TODO: switch case for closest channel to be selected if entered channel Number is not available