# **Parallelized Web Scraping System**

## Overview

The **Parallelized Web Scraping System** is a Python-based tool that allows you to scrape multiple websites in parallel. It uses Parsl to run scraping tasks concurrently, extracts the webpage titles from the provided URLs, and stores the results in a MySQL database. The system is equipped with a retry mechanism for network errors (with exponential backoff) and robust error logging.

## Features

- **Parallel Web Scraping**: Uses Parsl to scrape multiple websites simultaneously.
- **Retry Mechanism**: Retries failed requests up to 3 times with exponential backoff.
- **Error Logging**: Logs errors related to web scraping and database operations into a file for future reference.
- **MySQL Database Storage**: Scraped data (URL and title) is stored in a MySQL database.

## Technologies Used

- **Python**: The main programming language for the project.
- **Parsl**: Used for parallelizing the web scraping tasks.
- **BeautifulSoup**: Used for parsing the HTML and extracting information.
- **Requests**: Used for making HTTP requests.
- **MySQL**: Used for storing scraped data.
- **pymysql**: Python library for interacting with MySQL databases.
