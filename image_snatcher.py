# Varun Gande

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import urllib.request
import time
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")

# driver = webdriver.Chrome(chrome_options=chrome_options)
PATH = "C:\Program Files (x86)\chromedriver.exe" # Location of chromedriver

url_prefix = "https://www.google.com/search?q="
url_postfix = "&tbm=isch&sxsrf=ALeKk0074FKz_Mz0SZVT6n0YcgcMhQ4Ndg%3A1618266585722&source=hp&biw=1600&bih=774&ei=2cl0YIKnJ824sQXP2I_4Bw&oq=dog&gs_lcp=CgNpbWcQAzIECCMQJzIFCAAQsQMyBQgAELEDMgIIADIFCAAQsQMyAggAMgUIABCxAzIFCAAQsQMyAggAMgUIABCxAzoICAAQsQMQgwE6BAgAEANQ7gxYog5g3xJoAHAAeACAAUqIAc4BkgEBM5gBAKABAaoBC2d3cy13aXotaW1n&sclient=img&ved=0ahUKEwjC9_Tn4PnvAhVNXKwKHU_sA38Q4dUDCAc&uact=5"



folder = "Image Scrape Pictures"

def download_images():
    search_item = input("Enter the item you want to search for: ")
    num_pics = int(input("Enter the number of pictures you want: "))

    driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=PATH)  
    search_url = f"{url_prefix}{search_item}{url_postfix}"
    driver.get(search_url) # Opens the user's search request in a chrome tab

     
    # Scrolls 3 times in the user's search tab
    value = 0
    for i in range(3):
        driver.execute_script("scrollBy("+ str(value) + ",+1000);") # Selenium executes JavaScript scrollBy function through python
        value += 100
        time.sleep(1)
    
    # All images in google are within a div with the id = islmp
    element = driver.find_element_by_id("islmp")
    sub = element.find_elements_by_tag_name("img") # Finds all elements with the tag img within the div

    # Loops over the images and finds the 'src' attribute of the images whose assigned index is less than num_pics
    for i,tag in enumerate(sub):
        if i < num_pics:
            src = tag.get_attribute("src")
            try:
                if src != None:
                    src = str(src)
                    urllib.request.urlretrieve(src, os.path.join(folder, search_item+str(i)+".jpg")) # Uses urllib to download the url in the given path
                else:
                    raise TypeError
            except Exception as e:
                print("Fail", e)

    driver.close()

def main():
    if not os.path.exists(folder):
        os.mkdir(folder)
    download_images()
    
main()


 