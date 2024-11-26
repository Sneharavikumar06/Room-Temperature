from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from openpyxl import Workbook

# Set up the WebDriver with Service (for Selenium v4)
service = Service('C:/Users/sneha/Downloads/chromedriver-win64/chromedriver-win64')
driver = webdriver.Chrome(service=service)

# Open the local HTML file (make sure to provide the correct file path)
driver.get('file:///C:/Users/sneha/OneDrive/Desktop/Sneha_ELGiInternshipTest/index.html')  # Use raw string or forward slashes

# Function to verify if temperature is displayed correctly
def verify_temperature_display(room_name):
    try:
        # Click on the room in the list
        room_element = driver.find_element(By.XPATH, f"//li[text()='{room_name}']")
        room_element.click()

        # Wait for the data to load
        time.sleep(2)

        # Check if the temperature data is displayed
        temperature_output = driver.find_element(By.ID, 'temperature-output')
        if f"Current temperature of {room_name}" in temperature_output.text:
            return "Passed"
        else:
            return "Failed"
    except Exception as e:
        return f"Failed: {str(e)}"

# Create an Excel workbook to store test results
workbook = Workbook()
sheet = workbook.active
sheet.title = "Acceptance Criteria Results"

# Add headers to the Excel sheet
sheet.append(["Test Case", "Room", "Result"])

# Test each room's temperature display
rooms = ["Room 101", "Room 102", "Room 103"]
for room in rooms:
    result = verify_temperature_display(room)
    sheet.append([f"Verify Temperature for {room}", room, result])

# Save the Excel report
workbook.save("acceptance_criteria_results.xlsx")
print("Test completed, results saved to 'acceptance_criteria_results.xlsx'.")

# Close the web driver
driver.quit()
