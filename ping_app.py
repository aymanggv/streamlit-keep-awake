from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

url = "https://aymang.streamlit.app"

options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
driver.get(url)

time.sleep(10)  # Let the page load

try:
    # Attempt to click the "wake up" button if it exists
    button = driver.find_element(By.XPATH, "//button[contains(text(), 'Yes')]")
    button.click()
    print("Wake-up button clicked.")
except:
    print("No wake-up button found — app is already awake.")

driver.quit()
