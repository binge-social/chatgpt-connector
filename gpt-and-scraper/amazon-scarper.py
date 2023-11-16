from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time

def get_amazon_first_link(keyword):
    # Set up the webdriver (make sure you have the appropriate webdriver installed)
    driver = webdriver.Chrome()  # You can use other drivers like Firefox or Edge

    try:
        # Open Amazon website
        driver.get("https://www.amazon.com")

        # Find the search box and enter the keyword
        search_box = driver.find_element("id", "twotabsearchtextbox")
        search_box.send_keys(keyword)
        search_box.send_keys(Keys.RETURN)

        # Wait for some time to ensure the page is loaded
        time.sleep(3)

        # Get the HTML content of the page
        page_source = driver.page_source

        # Parse the HTML using BeautifulSoup
        soup = BeautifulSoup(page_source, 'html.parser')

        # Find the first search result link
        first_link = soup.find('a', {'class': 's-no-outline'})

        if first_link:
            return first_link.get('href')
        else:
            return "No results found"

    except Exception as e:
        print(f"An error occurred for {keyword}: {str(e)}")
    finally:
        # Close the webdriver
        driver.quit()

if __name__ == "__main__":
    # Input a list of keywords separated by newlines
    keywords_str = input("Enter a list of keywords separated by newlines:\n")
    user_provided_keywords = keywords_str.split('\n')

    # Use the user-provided keywords to search on Amazon
    for keyword in user_provided_keywords:
        result = get_amazon_first_link(keyword)
        print(f"The first link on Amazon for '{keyword}' is: amazon.com{result}")
