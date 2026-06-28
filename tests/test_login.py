from pages.login_page import LoginPage

def test_successful_login(driver):
    driver.get("https://practicetestautomation.com/practice-test-login/")
    
    login_page = LoginPage(driver)
    login_page.enter_username("student")
    login_page.enter_password("Password123")
    login_page.click_login()  
    
    # Verify successful login by checking for a specific element or URL change
    assert "Logged In Successfully" in driver.page_source  # Checks if the success message is present in the page source after login