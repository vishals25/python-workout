# Diary Tone Analysis Project

This project analyzes the sentiment of diary entries over time using the NLTK SentimentIntensityAnalyzer and visualizes the results with Streamlit and Plotly.

## Table of Contents

- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)

## Requirements

- Python 3.x
- Streamlit
- NLTK
- Plotly
- glob
- SentimentIntensityAnalyzer from NLTK

## Installation

1. Install the required Python packages using pip:
   ```sh
   pip install streamlit nltk plotly
   ```
2. Download the NLTK data:
   ```python
   import nltk
   nltk.download('vader_lexicon')
   ```

## Usage

1. Clone the repository or download the code.
2. Ensure you have diary entries in `.txt` format in a directory named `diary`. Each file should be named with the date of the entry (e.g., `2024-01-01.txt`).
3. Run the Streamlit app:

   ```sh
   streamlit run diary_tone_analysis.py
   ```

---

# Book Analysis Project

This project analyzes the text of the book "Miracle in the Andes" to perform various textual and sentiment analyses. The code processes the book to find the number of chapters, word frequencies, and sentiment scores.

## Table of Contents

- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [pratice](#pratice)

## Requirements

- Python 3.x
- OpenCV (if using video capture functionality)
- NLTK
- re (regular expressions)
- SentimentIntensityAnalyzer from NLTK

---

## pratice

- The Practice to use regex in python has been included as `Book_analysis.ipynb`

  ## Installation

  1. Install the required Python packages using pip:

  ```sh
  pip install opencv-python nltk
  ```

  2. Download the NLTK data:

  ```python
  import nltk
  nltk.download('stopwords')
  nltk.download('vader_lexicon')
  ```

  ## Usage

  1. Clone the repository or download the code.
  2. Place the book file `miracle_in_the_andes.txt` in the same directory as the script.
  3. Run the script:

  ```sh
  python book_analysis.py
  ```

---
