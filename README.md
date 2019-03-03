# CheapFlightBot
Uses Python and Selenium to search for cheap flights and then tweets the good deals. Currently not active.

Link: [https://twitter.com/CheapFlightBot](https://twitter.com/CheapFlightBot)

## Getting Started

#### Installing Selenium

Selenium for Python is used by the data collection portion of the bot. Selenium is an automated/programmable web browser. The browser opens up, goes to the URL where the flight data is contained, and then finds the HTML classes that contain the prices. For detailed instructions on installing Selenium, go to the [Selenium website](http://selenium-python.readthedocs.io/installation.html)

1. Install [Python 2.7](https://www.python.org/downloads/) if you don't already have it
2. Run `pip install selenium`
3. Download a [FireFox Driver](https://github.com/mozilla/geckodriver/releases)
4. Add the driver executable to your system's `PATH` environment variable

#### Installing Tweepy and Getting Twitter API Credentials

[Tweepy](https://github.com/tweepy/tweepy) is a Python library that is used to easily use the Twitter API through Python. You will notice that I have a private `tweepyKeys.py` file that is imported. This is not necessary and just used so that I don't accidentally upload my private keys to GitHub. You can just copy your keys in directly.
1. Run `pip install tweepy`
2. Make a Twitter account or sign in
3. Go to the [Twitter Application Manager](https://apps.twitter.com/app/new) to create a new application
4. Fill out the requested info. The website and callback URL are unnecessary
5. Once created, you can look at you application's details by clicking its link on the Application Manager home page. Navigate to the "Keys and Access Tokens" tab. There, you will find your keys and access tokens
6. Copy the keys and tokens into their respective places in the `twitter.py` file (ex: replace `keys.CONSUMER_SECRET` with the "Consumer Secret (API Secret)" key)
