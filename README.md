<br />
<p align="center">
  <h3 align="center">Predict whether a company's stock will rise or fall the next day!</h3>

  <p align="center">
    Prediction with LSTM!
    <br />
    <br />
    <a href="https://github.com/SasaIA/Trading">View Demo</a>
</p>

<!-- TABLE OF CONTENTS -->
## Table of Contents

- [Table of Contents](#table-of-contents)
- [About The Project](#about-the-project)
  - [Built With](#built-with)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)

<!-- ABOUT THE PROJECT -->
## About The Project

![App Page](appPage.png)

This project aims to predict whether a company's stock price will rise or fall the next day to find out whether we can buy a stock or not. We selected three companies and collected data from 1999 to present.

### Built With
We coded this project using Python, its packages, a Database and an API :

* [Python](https://www.python.org)
* [Pymongo](https://pymongo.readthedocs.io/en/stable/)
* [Darts](https://unit8co.github.io/darts/)
* [Pandas](https://pandas.pydata.org/)
* [Numpy](https://numpy.org/)
* [Matplotlib](https://matplotlib.org/)
* [Plotly](https://plotly.com/python/)
* [Alpha Vantage](https://www.alphavantage.co/)
* [MongoDB](https://docs.mongodb.com/)

<!-- GETTING STARTED -->
## Getting Started

To get started, you are going to need :

### Prerequisites

You need to install Python from [here](https://www.python.org/downloads/) first then download the file [get-pip.py](https://bootstrap.pypa.io/get-pip.py). In the terminal, go to the folder where the file was downloaded and type the following command :

```sh
python get-pip.py
```

### Installation

Now create a folder, open it on an IDE and follow the instructions :

1. Get a free API Key at [Alpha Vantage](https://www.alphavantage.co)

      - Create an `apiKey.txt` file in the root of the Trading folder and put your API key there.
      - To connect to MongoDB Atlas: Create a `mongoKey.txt` file at the root of the Trading folder and put in each line your username, password and the rest of the MongoDB Atlas link after the '@'.

2. Open terminal and clone the repository
```sh
git clone https://github.com/SasaIA/Trading.git
```
3. Install Python packages using pip
```sh
pip install -r requirements.txt
```
4. Make sure to install MongoDB on your computer
5. To launch a file, you must start the terminal and navigate to the folder that contains that file
5. Open the terminal and type :
```sh
python api.py
python lstm.py
```
5. Thats it you have the latest stock price for each company and the prediction for tomorrow.
6. Every night, launch the `updatesPrice.py` file to update the database with the last stock price.
7. To launch the app, type in the terminal
```sh
streamlit run app.py
 ```

<!-- USAGE EXAMPLES -->
## Usage

There are different files in this project:
- The first `api.py` allows to retrieve the data via the API and to store the data in a JSON file and then to send them to a database.
- The second `lstm.py` predicts whether the stock will rise or fall the next day.
- The third `updatesPrice.py`, allows us to update our database with the last known stock price.
- The fourth `dataviz.ipynb` allows you to analyze data with different graphs.
- The fifth `app.py` file is used to launch the application and have a visual on the latest stock prices, to have an overview of the graphs and predictions.