# E-Commerce Regression Test Automation Suite
This project implements an automated regression test suite for an e-commerce platform that sells electronics (TVs, radios, cameras). The test suite is built using **Selenium and Python**, and follows best practices in test structure, data management, and error handling.

## Tech Stack
**Language**: Python 3.x  
**Automation Tool**: Selenium WebDriver  
**Data Format**: JSON  
**Design Pattern**: Page Object Model (POM)

## Test Scenarios Automated
1. User Registration and Login
2. Browse Products
   - Navigate to categories
   - View product details
3. Add Product to Cart
   - Verify product is visible in the cart

## Project Structure

## Running Tests
### Run all tests (default to `dev`):
```bash
pytest tests/ test_name.py --env={dev/stage}
pytest tests/test_cart.py --env=stage --html=reports/test_report.html --self-contained-html
