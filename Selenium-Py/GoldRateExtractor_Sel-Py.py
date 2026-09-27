from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from openpyxl import Workbook

from datetime import date, timedelta
import time


# ==========================================
# STEP 1: Launch Firefox Browser
# ==========================================

driver = webdriver.Chrome()
driver.maximize_window()

wait = WebDriverWait(driver, 10)

# Open Gold Rate website
driver.get("https://www.goodreturns.in/gold-rates/chennai.html")

print("Step 1: Site has been opened")


# ==========================================
# STEP 2: Create Excel Workbook & Sheet
# ==========================================

workbook = Workbook()

sheet = workbook.active
sheet.title = "Gold Rates"

# Create headers
sheet.append([
    "Date",
    "24K Gold (₹/g)",
    "22K Gold (₹/g)",
    "18K Gold (₹/g)"
])

print("Step 2: Excel has been created")


# ==========================================
# STEP 3: Define Date Range
# Last 30 days
# ==========================================

end_date = date.today()
start_date = end_date - timedelta(days=5)

print("Step 3: Date range defined")


# ==========================================
# STEP 4: Loop Through Each Date
# ==========================================

current_date = start_date

while current_date <= end_date:

    try:

        # ==================================
        # STEP 4.1: Find Calendar
        # ==================================

        calendar_icon = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//input[@id='gold-date-picker']")
            )
        )

        calendar_icon.click()

        print("Step 4.1: Calendar clicked")


        # ==================================
        # STEP 4.2: Select Date using JS
        # ==================================

        picker_date = current_date.strftime("%Y-%m-%d")

        driver.execute_script(
            """
            arguments[0].value = arguments[1];
            arguments[0].dispatchEvent(
                new Event('change', {bubbles:true})
            );
            """,
            calendar_icon,
            picker_date
        )

        time.sleep(2)

        print("Step 4.2: Date selected ->", picker_date)


        # ==================================
        # STEP 4.3: Fetch Gold Prices
        # ==================================

        gold_24k_price = driver.find_element(
            By.XPATH,
            '//*[@id="24K-price"]'
        ).text

        gold_22k_price = driver.find_element(
            By.XPATH,
            '//*[@id="22K-price"]'
        ).text

        gold_18k_price = driver.find_element(
            By.XPATH,
            '//*[@id="18K-price"]'
        ).text

        print("Step 4.3: Gold rate fetched successfully")


        # ==================================
        # STEP 4.4: Write Data to Excel
        # ==================================

        display_date = current_date.strftime("%d-%m-%Y")

        sheet.append([
            display_date,
            gold_24k_price,
            gold_22k_price,
            gold_18k_price
        ])

        print("Fetched data for:", display_date)


    except Exception as e:

        print(
            "Failed for date:",
            current_date,
            "| Reason:",
            str(e)
        )


    # Move to next date
    current_date += timedelta(days=1)


print("Step 4.4: Data stored in Excel")


# ==========================================
# STEP 5: Save Excel File
# ==========================================

workbook.save("Chennai_Gold_Rates.xlsx")

print("Step 5: Excel file saved")


# ==========================================
# STEP 6: Close Browser
# ==========================================

driver.quit()

print("Gold rate extraction completed successfully!")