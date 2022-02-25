import twint

c = twint.Config()

c.Search = ['Cisco']                     # topic
c.Lang = 'en'
c.Limit = 100                            # number of Tweets to scrape
c.Store_csv = True                       # store tweets in a csv file
c.Output = "Cisco_tweets.csv"            # path to csv file

twint.run.Search(c) 

import pandas as pd
df = pd.read_csv('Cisco_tweets.csv') 

df['tweet']
