import twint

c = twint.Config()

c.Search = ['Cisco']                     # topic
c.Lang = 'en'
c.Limit = 10                            # number of Tweets to scrape
c.Store_csv = True                       # store tweets in a csv file
c.Output = "Cisco_tweets.csv"            # path to csv file

print('Starting Search')

twint.run.Search(c) 

print('Search complete.  Printing results')

import pandas as pd 
# pd.set_option('column.display.width', -1)

df = pd.read_csv('Cisco_tweets.csv', header=0)
df.head()
print(df['tweet']) 

print('Print complete. Program ends.')
