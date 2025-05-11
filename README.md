🧪 SauceProject - Automated Testing using Python Selenium & Pytest

Capstone Project for PAT | Author: PAVAN KUMAR RV

🔍 Project Overview
This project focuses on automating end-to-end testing of the e-commerce demo website SauceDemo using Python Selenium, Pytest, and the Page Object Model (POM). The system ensures both functional correctness and UI behavior verification via automated test scripts.

The goal is to build a robust automation framework that supports:

Cross-browser compatibility

OOP design principles

Hybrid Testing (Data-Driven + Keyword-Driven)

Detailed Pytest HTML Reports

✅ Test Objectives
Automate the login, product selection, cart, and checkout functionalities.

Validate both positive and negative test scenarios.

Use Explicit Waits, Exception Handling, and Cross-browser execution.

Incorporate DDTF (Excel/CSV) and KDTF (YAML) into the test workflow.

Ensure all tests produce HTML reports with Pytest.

🧰 Tech Stack & Tools
Tool/Library	Purpose
Python 3.x	Programming Language
Selenium	Web Browser Automation
Pytest	Test Framework + HTML Reporting
POM	Code Structure & Reusability
DDTF (CSV/Excel)	Data-Driven Testing
WebDrivers	Chrome, Firefox, Edge, Safari

📂 Project Structure
graphql
Copy
Edit
SauceProject/
│
├── config/
│   
│
├── data/
│  
│
├── pages/
│   
│
├── tests/
│   
│
├── utils/
│   
│
├── reports/
│   
│
├── screenshots/│   
│
├── requirements.txt              # Python dependencies
|
├── conftest.py                   # Pytest fixtures
├── 
└── README.md                     # Project documentation
📋 Test Case Coverage
Test Case	Description
TC-1	Login with multiple users + cookie-based login
TC-2	Login with custom user credentials
TC-3	Logout functionality & button visibility
TC-4	Cart button visibility
TC-5	Random product selection + fetch names & prices
TC-6	Add selected products to cart + verify cart count
TC-7	Validate product details in the cart
TC-8	Complete checkout flow + screenshot + validation

⚙️ Setup Instructions
Clone the Repository


Copy
Edit
git clone https://github.com/basil-hameed/SauceProject.git
cd SauceProject
Install Dependencies

bash
Copy
Edit
pip install -r requirements.txt
Run Tests with HTML Report

bash
Copy
Edit
pytest tests/ --html=reports/report.html
View Report
Open reports/report.html in your browser.

📌 Key Features
✅ Cross-browser Testing Support

✅ Page Object Model (POM)

✅ Data-Driven Testing (xlsx)

✅ Randomized Product Selection

✅ Explicit Waits + Exception Handling

✅ Visual Evidence via Screenshots

✅ Compliance with PyLint Standards

📖 Best Practices Followed
POM design for modular & scalable code

Exception handling for stability

Explicit waits for synchronization

Comments and docstrings for clarity

📸 Sample Screenshot
Checkout Overview Page screenshot is auto-saved during TC-8 in the screenshots/ directory.

🧼 Cleanup
All tests ensure the browser is automatically closed after execution using teardown logic in Pytest fixtures (conftest.py).
