import requests
from PIL import Image
import easyocr
import io
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Initialize the WebDriver (assuming Chrome)
driver = webdriver.Chrome()

try:
    driver.get("https://tmrsearch.ipindia.gov.in/eregister/")
    wait = WebDriverWait(driver, 20)
    
    # Switch to "eregoptions" frame
    wait.until(EC.frame_to_be_available_and_switch_to_it((By.NAME, "eregoptions")))
    
    # Click "Trade Mark Application" button
    trade_mark_application_button = wait.until(
        EC.element_to_be_clickable((By.ID, "btnviewdetails"))
    )
    driver.execute_script("arguments[0].click();", trade_mark_application_button)
    driver.switch_to.default_content()
    
    # Switch to "showframe" frame and click radio button
    wait.until(EC.frame_to_be_available_and_switch_to_it((By.NAME, "showframe")))
    radio_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/form/div[3]/table[2]/tbody/tr/td/table/tbody/tr/td[1]/input"))
    )
    radio_button.click()
    
    # Enter application number
    application_number_field = wait.until(
        EC.presence_of_element_located((By.XPATH, "/html/body/form/div[3]/table/tbody/tr[2]/td[2]/input"))
    )
    application_number_field.send_keys("6712975")
    
    # Capture and process CAPTCHA image
    img_element = wait.until(EC.presence_of_element_located((By.ID, "ImageCaptcha")))
    img_element.screenshot("captcha.png")
    reader = easyocr.Reader(['en'])
    result = reader.readtext("captcha.png")
    captcha_text = " ".join([text[1] for text in result])
    print("Extracted CAPTCHA Text:", captcha_text)
    
    # Enter CAPTCHA text
    captcha_input_field = wait.until(
        EC.presence_of_element_located((By.XPATH, "/html/body/form/div[3]/table/tbody/tr[5]/td[2]/input"))
    )
    captcha_input_field.send_keys(captcha_text)
    
    # Click on the view button
    view_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/form/div[3]/table/tbody/tr[6]/td[2]/input[1]"))
    )
    view_button.click()
    time.sleep(30)
except Exception as e:
    print("Error:", e)
finally:
    pass
