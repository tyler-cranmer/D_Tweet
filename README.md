# Discord Twitter Tweet Bot
This is a twitter bot that streams a specific users tweets into our discord server. Follow the directions to get set up. 


### Make sure python3 is installed.
#### Create and Activate Virtual Environment
python3 -m venv venv

source venv/bin/activate 

#### Install tweepy 
pip install tweepy

### Create a Twitter Developer Account
https://developer.twitter.com/en/support/twitter-api/developer-account

### create .env file to store environment variables. 
BEARER_TOKEN = 'Some access string given to you from your twitter developer account'
WebHookApi = 'web hook url from discord server'

