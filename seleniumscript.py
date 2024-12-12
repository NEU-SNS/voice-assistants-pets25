from seleniumbase import SB
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# Your Gmail login credentials
mail_address = "USERNAME" # Replace with your actual email address
password = "PASSWORD"  # Replace with your actual password

# Replace the list with your own queries
questions = ["LIST",
             "OF",
             "QUERIES"]

with SB(uc=True) as sb:
    sb.open("https://accounts.google.com/")

    # Wait for email input to be present
    sb.wait_for_element_present('input[type="email"]', timeout=10)
    sb.type('input[type="email"]', mail_address)
    sb.click('button:contains("Next")')

    # Wait for password input to be present
    sb.wait_for_element_present('input[type="password"]', timeout=10)
    sb.sleep(5)
    sb.type('input[type="password"]', password)
    sb.click('button:contains("Next")')

    # Redirect to Google after logging in to Gmail
    sb.open("https://www.google.com/")
    
    # Wait for search input to be present before the loop
    try:
        search_input = WebDriverWait(sb.driver, 10).until(
            EC.presence_of_element_located((By.NAME, "q"))
        )
    except TimeoutException:
        print("Search input element not found within the specified time.")

    # Automatically search queries based on the list
    for query in questions:
        try:
            # Wait for search input inside the loop
            search_input = WebDriverWait(sb.driver, 10).until(
                EC.presence_of_element_located((By.NAME, "q"))
            )
            search_input.clear()
            search_input.send_keys(query)
            search_input.submit()
            sb.sleep(1)
        except TimeoutException:
            print(f"Element 'input[name=\"q\"]' not found. Retrying...")
