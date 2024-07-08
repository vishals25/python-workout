# Tesla News Emailer using NewsApi

This project fetches the latest news articles about Tesla from the News API and sends an email with the fetched news using the SMTP protocol.

## Prerequisites

- Python 3.x
- `requests` library

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/tesla-news-emailer.git
   cd tesla-news-emailer
   ```

2. Install required Python packages:

   ```bash
   pip install requests
   ```

## Setup

**API Key**: - You need a News API key to fetch news articles. Replace the placeholder with `your actual API key`.

## Usage

1. Run the script:

   ```bash
   python main.py
   ```

2. The script will:
   - Fetch the latest Tesla news articles.
   - Compile the articles into a formatted string.
   - Send an email with the compiled news to the specified email address.
   - Print a success message upon completion.

## File Structure

> [Title] :
>
> - [description of title]
>
> [Title] :
>
> - [description of title]

## To get Binary data Through Api:

- Get the url for an images for testing
- Using request get the binary Coding of that images.

````sh
request.content```
````

- Write it into a file with needed Extensions such as `.jpg` or `.png`

```python
with open("image_name.jpg","wb")as file:
     file.write(request.content)

```

---
