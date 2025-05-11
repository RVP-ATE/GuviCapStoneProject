"""
This file contains all the static test data used across the automation test suite.
Keeping data centralized helps improve maintainability and reduces duplication.
"""

class Data:
    # Base URL of the application under test
    url = "https://www.saucedemo.com/"

    # Expected page title after successful login
    expected_title = "Swag Labs"

    # Expected URL after login redirects to inventory page
    expected_url = "https://www.saucedemo.com/inventory.html"

    # Standard login credentials for existing user
    username = "standard_user"
    password = "secret_sauce"

    # Sample credentials for a hypothetical new user (could be used for signup tests)
    new_user = "guvi_user"
    new_password = "Secret@123"

    # Checkout-related test data
    firstname = "PAVANKUMAR"
    lastname = "RV"
    zipcode = "577228"


