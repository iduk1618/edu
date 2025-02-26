from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

def start_browser(url):
    driver = webdriver.Chrome(options=Options(),service=Service())
    driver.get(url)
    driver.maximize_window()
    sleep(1)
    return driver

def test_osnovni_kolacici_iframe():
    driver = start_browser("https://www.skysports.com/")
    iframe = driver.find_element(By.XPATH, "//iframe[@id='sp_message_iframe_1223386']")
    driver.switch_to.frame(iframe)
    driver.find_element(By.XPATH,"//button[@title='Essential cookies only']").click()
    sleep(1)
    assert "Sky Sports - Sports News, Transfers, Scores | Watch Live Sport" in driver.title, "Stranica nije ucitana"
    close_browser(driver)

def test_pocetna_stranica():
    driver = start_browser("https://www.skysports.com/")
    assert "Sky Sports - Sports News, Transfers, Scores | Watch Live Sport" in driver.title, "Stranica nije ucitana"
    close_browser(driver)

def test_score_tabela_scroll():
    driver = start_browser("https://www.skysports.com/")
    actions = ActionChains(driver)
    iframe = driver.find_element(By.XPATH, "//iframe[@id='sp_message_iframe_1223386']")
    driver.switch_to.frame(iframe)
    driver.find_element(By.XPATH, "//button[@title='Essential cookies only']").click()
    driver.switch_to.default_content()
    sleep(1)
    driver.find_element(By.XPATH,"//a[.='Scores']").click()
    actions.move_to_element(driver.find_element(By.XPATH, "//div[@class='vidiprinter__items']")).perform()
    sleep(1)
    driver.execute_script("window.scrollBy(0,200);")
    sleep(1)
    driver.find_element(By.XPATH,"//div[@class='vidiprinter__item' and contains(.,'Ellis Iandolo (Colchester) ')]").click()
    sleep(1)
    assert "Swindon 3 - 2 Colchester - Matc" in driver.title, "Utaknmica nije ucitana"
    close_browser(driver)
def close_browser(driver):
    driver.minimize_window()
    driver.close()