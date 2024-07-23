# Machine Learning Project: Recommender Systems

This project demonstrates three different types of recommender systems using Jupyter notebooks. The notebooks included are:

1. **Popularity Based Filtering**
2. **Content Based Filtering**
3. **Collaborative Based Filtering**

## Requirements

- Python 3.12
- Jupyter Notebook
- pandas
- numpy
- scikit-learn
- matplotlib
- seaborn

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/recommender-systems.git
    cd recommender-systems
    ```

2. Create and activate a virtual environment:

    ```bash
    python -m venv env
    source env/bin/activate   # On Windows use `env\Scripts\activate`
    ```

3. Install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Start Jupyter Notebook:

    ```bash
    jupyter notebook
    ```

5. Open the notebooks in your browser:

    - `notebook1.ipynb`
    - `notebook2.ipynb`
    - `notebook3.ipynb`

## Notebooks Overview

### Notebook 1: Popularity Based Filtering

This notebook demonstrates how to build a simple popularity-based recommender system. It recommends items based on their popularity among all users.

### Notebook 2: Content Based Filtering

This notebook shows how to create a content-based recommender system. It recommends items similar to those the user has liked in the past based on item features.

### Notebook 3: Collaborative Based Filtering

This notebook explains collaborative filtering techniques, both user-based and item-based, to recommend items based on the preferences of similar users.

## Usage

1. **Popularity Based Filtering**: Run `notebook1.ipynb` to see how items are recommended based on their popularity.
2. **Content Based Filtering**: Run `notebook2.ipynb` to see how recommendations are made based on item features.
3. **Collaborative Based Filtering**: Run `notebook3.ipynb` to explore user-based and item-based collaborative filtering methods.

## Additional Notes

- Ensure you have the correct version of Python (3.12) installed.
- The datasets used in the notebooks should be placed in the `data` directory.
- The visualizations created using `matplotlib` and `seaborn` will help you understand the data and the performance of the models.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.
