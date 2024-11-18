import requests
import time
from bs4 import BeautifulSoup
from parsl.app.app import python_app
from database import store_data_in_db
from parsl_config import load_parsl_config
import logging


# Logging configuration
logging.basicConfig(filename="scraping_errors.log", level=logging.ERROR)


def log_error(message):
    logging.error(message)


# Scraper function
def scraper(url, retries=3):
    for i in range(retries):
        try:
            # If the URL doesn't have a protocol, add it
            if not url.startswith("http://") and not url.startswith("https://"):
                url = "http://" + url
            response = requests.get(url, timeout=10)  # Timeout added for long requests
            response.raise_for_status()  # Check if the request was successful
            soup = BeautifulSoup(response.text, "html.parser")
            title = soup.title.string if soup.title else "No Title"
            return {"url": url, "title": title}
        except requests.RequestException as error:
            log_error(f"Attempt {i + 1} failed for {url}: {error}")
            time.sleep(2**i)  # Exponential backoff for retries
        except Exception as error:
            log_error(f"An unexpected error occurred for {url}: {error}")
            return {"url": url, "error": str(error)}
    log_error(f"Failed after {retries} retries for {url}")
    return {"url": url, "error": "Failed after retries"}


@python_app
def parallel_parsl_scrape(url):
    return scraper(url)


def multiple_url_scraper(urls):
    futures = [parallel_parsl_scrape(url) for url in urls]
    results = [future.result() for future in futures]
    for result in results:
        print(result)
        store_data_in_db(result)


if __name__ == "__main__":

    load_parsl_config()

    # Website List
    urls = [
        "https://www.google.com",
        "https://www.example.com",
        "https://www.wikipedia.org",
        "https://www.github.com",
        "https://stackoverflow.com",
        "https://www.python.org",
        "https://www.bbc.com/news",
        "https://www.nytimes.com",
        "https://techcrunch.com",
        "https://www.cnn.com",
        "https://www.theverge.com",
        "https://www.nasa.gov",
        "https://developer.mozilla.org",
        "https://www.nationalgeographic.com",
        "https://www.theguardian.com/international",
        "https://www.reuters.com",
        "https://www.bloomberg.com",
        "https://www.youtube.com",
        "https://www.amazon.com",
        "https://www.ebay.com",
    ]

    multiple_url_scraper(urls)  # Calling the function with the list of URLs
