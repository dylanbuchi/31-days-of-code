import os
import ctypes
import urllib.request

from selenium import webdriver

FIREFOX_DRIVER_PATH = r"C:\Users\crypt\development\geckodriver\geckodriver.exe"
IMAGE_PATH = os.path.join(os.getcwd(), "src/day_31/images/bg.png")


def change_background_image():
    ctypes.windll.user32.SystemParametersInfoW(
        20, 0, f"{os.path.abspath(IMAGE_PATH)}", 0)


def get_web_driver_for(url):
    driver = webdriver.Firefox(executable_path=FIREFOX_DRIVER_PATH)
    driver.get(url)
    driver.fullscreen_window()
    return driver


def get_target_from(data, target):
    result = None
    for item in data:
        if item.text == target:
            result = item
            break
    return result


def main():
    url = "https://wallpaperscraft.com/"
    driver = get_web_driver_for(url)

    image = driver.find_element_by_class_name("wallpapers__image")
    image.click()

    resolutions = driver.find_elements_by_class_name("resolutions__link")
    resolution_1920x1200 = get_target_from(resolutions, "1920x1200")
    resolution_1920x1200.click()

    a_tags = driver.find_elements_by_tag_name("a")
    download_button = get_target_from(a_tags, "Download wallpaper 1920x1200")
    download_button.click()

    url = driver.find_element_by_tag_name("img").get_attribute("src")
    urllib.request.urlretrieve(url, IMAGE_PATH)
    change_background_image()
    driver.quit()


if __name__ == "__main__":
    main()
