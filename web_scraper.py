import requests
from bs4 import BeautifulSoup
from parsl.app.app import python_app

from database import store_data_in_db
from parsl_config import load_parsl_config


# Scraper function
def scraper(url):
    try:
        # If the url does not contain http protocol info, concatenate it
        if not url.startswith("http://") and not url.startswith("https://"):
            url = "http://" + url
        response = requests.get(
            url
        )  # Sending a request to the passed url into .get function

        response.raise_for_status()  # check the success of the response
        soup = BeautifulSoup(response.text, "html.parser")
        title = soup.title.string if soup.title else "No Title"

        return {"url": url, "title": title}  # returning a dictionary with the info
    except Exception as error:  # Throws the exception
        return f"Error: {error}"


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
    urls = ["www.google.com", "www.example.com", "www.wikipedia.org", "www.github.com"]

    multiple_url_scraper(urls)  # Calling the function with the list of URLs
