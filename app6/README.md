# Weather Station Data API

This is a simple Flask application that provides an API for accessing weather station data. The data includes station information and temperature records for different dates and years.

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [File Structure](#file-structure)
- [Example Data](#example-data)

## Features

- **Home Page:** Displays a list of weather stations with links to their respective data.
- **Station Data API:** Provides temperature data for a specific station and date.
- **Station Data Table:** Displays all temperature records for a specific station.
- **Yearly Station Data:** Displays temperature records for a specific station and year.

## Requirements

- Python 3.x
- Flask
- pandas
- numpy

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/yourusername/weather-station-api.git
   cd weather-station-api
   ```

2. Install the required packages:

   ```bash
   pip install flask pandas numpy
   ```

3. Ensure the data files are in the `data_small` directory:

   ```kotlin
   data_small/
   ├── stations.txt
   ├── TG_STAID000001.txt
   ├── TG_STAID000002.txt
   └── ... (other station data files)
   ```

## Usage

- Unzip `data_small.zip` to `data_small` as the folder name.

1. Run the Flask application:

   ```bash
   python app.py
   ```

2. Open your web browser and navigate to `http://127.0.0.1:5000/` to view the home page with the list of stations.

## API Endpoints

### Home Page

- **URL:** `/`
- **Method:** GET
- **Description:** Displays a list of weather stations with links to their respective data.

### Station Data for Specific Date

- **URL:** `/api/v1/<station>/<date>/`
- **Method:** GET
- **Parameters:**
  - `station`: The ID of the station.
  - `date`: The date in `YYYY-MM-DD` format.
- **Response:** JSON object containing station ID, date, and temperature.

### Station Data Table

- **URL:** `/api/v1/<station>`
- **Method:** GET
- **Parameters:**
  - `station`: The ID of the station.
- **Description:** Displays all temperature records for the specified station.

### Yearly Station Data

- **URL:** `/api/v1/<station>/yearly/<year>`
- **Method:** GET
- **Parameters:**
  - `station`: The ID of the station.
  - `year`: The year in `YYYY` format.
- **Description:** Displays temperature records for the specified station and year.

## File Structure

```arduino
weather-station-api/
├── data_small/
│   ├── stations.txt
│   ├── TG_STAID000001.txt
│   ├── TG_STAID000002.txt
│   └── ... (other station data files)
├── templates/
│   └── home.html
└── app.py
```

## Example Data

- **stations.txt:** Contains station information.
- **TG_STAID000001.txt:** Contains temperature records for station ID 1.
- **TG_STAID000002.txt:** Contains temperature records for station ID 2.
- ... (other station data files)
