import pyautogui

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from webdriver_manager.firefox import GeckoDriverManager
from time import sleep


WALLPAPERS_URL = "https://dailydevbytes.com/channel/wallpapers"

 
class Keys:
    DOWN = "down"
    ENTER = "enter"


def get_web_driver_for(url):
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    driver.get(url)
    return driver


def press_key(key, press_count=1):
    for _ in range(press_count):
        pyautogui.press(key)



def set_wallpaper(driver):
    first_image = driver.find_element(By.TAG_NAME, "img")

    action_chains = ActionChains(driver)
    action_chains.context_click(first_image).perform()

    press_key(Keys.DOWN, 13)
    press_key(Keys.ENTER)

    sleep(2.5)

    press_key(Keys.DOWN, 6)
    press_key(Keys.ENTER)


def main():
    driver = get_web_driver_for(WALLPAPERS_URL)
    set_wallpaper(driver)

    driver.quit()


if __name__ == "__main__":
    main()

