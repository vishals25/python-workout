# Weather Forecast App

This is a Streamlit application that provides weather forecasts for a specified location and number of days. The app allows users to view temperature or sky condition forecasts.

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)

## Features

- **User Input:** Enter the place and select the number of days for the forecast.
- **Data View:** Choose between temperature or sky conditions.
- **Temperature Forecast:** Displays a line chart of temperature data for the next specified days.
- **Sky Condition Forecast:** Displays images and descriptions of sky conditions at different times of the day.

<img src="images/WEATHER FORECAST_page-0001.jpg" style="width: 900px;" alt="Weather Forecast">

<img src="images/WEATHER FORECAST-tem_page-0001.jpg" style="width: 900px;" alt="Weather Forecast Template">

## Requirements

- Python 3.x
- Streamlit
- Plotly
- Backend data fetching module (backend.py)

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/yourusername/weather-forecast-app.git
   cd weather-forecast-app
   ```

2. Install the required packages:

   ```bash
   pip install streamlit plotly
   ```

3. Ensure the `backend.py` module is present in the root directory:

   ```kotlin
   weather-forecast-app/
   ├── backend.py
   ├── app.py
   └── ...
   ```

## Usage

1. Run the Streamlit application:

   ```bash
   streamlit run app.py
   ```

2. Open your web browser and navigate to `http://localhost:8501` to view the app.
