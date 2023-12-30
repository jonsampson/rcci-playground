from unittest.mock import Mock
from rcci_playground.scraper.scraper import get_price

def test_get_price(mocker):
    # Mock the WebDriver
    mock_driver = Mock()
    mock_driver.get.return_value = None

    # Mock the elements
    mock_balcony_element = Mock()
    mock_date_element = Mock()
    mock_quote_element = Mock()
    mock_price_element = Mock()

    # Set up the text of the final price element
    mock_price_element.text = '1000'

    # Set up the mock elements to return each other in the correct sequence
    mock_driver.find_element.return_value = mock_balcony_element
    mock_balcony_element.click.return_value = None
    mocker.patch('selenium.webdriver.support.ui.WebDriverWait.until', return_value=mock_date_element)
    mock_date_element.find_element.return_value = mock_quote_element
    mock_quote_element.find_element.return_value = mock_price_element

    # Call the get_price function
    price = get_price(mock_driver)

    # Assert that the returned price is correct
    assert price == '1000'
