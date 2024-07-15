# Event Scraper and Notifier

This project is a Python-based event scraper and notifier that fetches event data from a specified URL, stores it in a SQLite database, and sends email notifications for new events.

## Features

- Scrapes event data from a specified URL.
- Extracts relevant event information using `selectorlib`.
- Stores event data in a SQLite database.
- Sends email notifications for new events.
- Handles storing and reading event data efficiently.

## Requirements

- Python 3.x
- Requests
- Selectorlib
- SQLite3
- smtplib
- ssl
- os

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/event-scraper-notifier.git
   cd event-scraper-notifier
   ```

2. Install the required Python packages:

   ```bash
   pip install requests selectorlib
   ```

3. Set up the SQLite database:

   ```bash
   sqlite3 data.db < schema.sql
   ```

4. Create an `extract.yaml` file with the necessary extraction rules. Example:
   ```yaml
   tours:
     css: "div.tour"
   ```

## Usage

1. Update the `url` variable in the script to point to the event data source:

   ```python
   url = "https://programmer100.pythonanywhere.com/tours/"
   ```

2. Ensure that the email credentials and recipient details are correctly set:

   ```python
   username = 'your_email@gmail.com'
   password = os.getenv("password1")
   receiver = 'receiver_email@gmail.com'
   ```

3. Run the script:
   ```bash
   python main.py
   ```

## Functions

- **scrape(url)**: Fetches the source HTML from the specified URL.
- **extract(source)**: Extracts event data from the HTML using `selectorlib`.
- **send_mail(message)**: Sends an email notification with the specified message.
- **store(value)**: Stores the extracted event data in the SQLite database.
- **read(value)**: Reads the event data from the SQLite database to check for duplicates.
