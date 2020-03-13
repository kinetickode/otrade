
# Sample Project

A 3 hour project to demonstrate python package development process.

## Design

Like any great genius I believe I can write a program to beat the stock market.  
And, like any student of economics and life in general, I know I am NOT a genius, 
and that the Efficient Market Hypothesis generally holds true, so these types of 
programs are a waste of time, except for the value of the programming exercise.

One thing I love about Python is the iterative development process which allows the
development of smaller working components that can be assembled into a larger whole.
So starting with some simple functions that return values:

```bash
get_quote
get_news
get_price_direction
```

assemble various values into vectors, and apply various strategies to the vectors
to return a buy, sell, or do nothing signal.


## Installation

This package requires a [Python 3](https://www.python.org/downloads/) environment.
Install latest python 3 then create a virtual environment.

```bash
python3 -m venv LoseMoney
cd LoseMoney
source ./bin/activate
```

Then install the otrade package.

```bash
git clone https://github.com/Kinetickode/otrade.git
cd otrade
./install.sh
```

## Testing

```bash
cd otrade
py.test
```

## Environment Variables

This package uses a .env file to hold variables for keys and ids
for each target environment Currently it holds the robinhood 
account username and password. The env/ directory containing sample 
env.dev, env.staging, env.demo, and env.prod.  After installation 
copy the appropriate env file to the directory containing the package.
The env directory should be encrypted if this was a real package.

```bash
cp env/env.<TYPE> ../.env
```
where TYPE is one of dev, staging, demo, or prod.

## Usage

To get a stock quote:

```bash
get_quote <Stock Symbol>
```

To get recent news articles for a stock:

```bash
get_news <Stock Symbol>
```

To get recent recent price direction for a stock:

```bash
get_price_direction <Stock Symbol>
```

For my own protection I am no-op'ing the Robinhood functions that either execute 
trades or changes any account data.  I am doing this in the otrade package to save 
time, though a better strategy would be to fork the robin-stocks package and remove 
the functions.


## Helpful Articles
http://www.robin-stocks.com/en/latest/functions.html


