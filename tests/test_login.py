from pages.login_page import LoginPage

def test_successful_login(driver, base_url):
    driver.get(base_url)
    
    login_page = LoginPage(driver)
    login_page.enter_username("standard_user")
    login_page.enter_password("secret_sauce")
    login_page.click_login()  
    
    # Verify successful login by checking for a specific element or URL change
    assert "inventory.html" in driver.current_url  # Checks if the user is redirected to the inventory page after successful login

def test_incorrect_username(driver, base_url):
    driver.get(base_url)

    login_page = LoginPage(driver)
    login_page.enter_username("wrong_user")
    login_page.enter_password("secret_sauce")
    login_page.click_login()
    
    # Verify incorrect username by checking for an error message
    error_warning = login_page.get_error_message()
    assert error_warning is not None  # Checks if an error message is displayed
    assert "Username and password do not match any user in this service" in error_warning  # Validates the specific error message for incorrect username

def test_incorrect_password(driver, base_url):
    driver.get(base_url)
    login_page = LoginPage(driver)
    login_page.enter_username("standard_user")
    login_page.enter_password("wrong_password")
    login_page.click_login()
    
    # Verify incorrect login by checking for an error message
    error_warning = login_page.get_error_message()
    assert error_warning is not None  # Checks if an error message is displayed
    assert "Username and password do not match any user in this service" in error_warning  # Validates the specific error message for incorrect paswsword