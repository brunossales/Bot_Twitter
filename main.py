import tweepy
import os
from dotenv import load_dotenv
import time

load_dotenv()

auth = tweepy.OAuthHandler("ZOhfkoiUKG7aifgoYPQisglmb", "ATlKadupbDyeP8hjB8ZdtsjIvKSSOfy3vGLPiRPzCej2QwIMEz")
auth.set_access_token("1619762473908707330-QuNFhh6DdWqh9MfGTZ4tlNgp11fVeS", "SJWubeAxx4yZXOQRRB1CoV0kXlYpqFa5Gp7ZRd9k9w8cT")

api = tweepy.API(auth)

search_word = "ssd"

# procure pelos tweets com a palavra "ssd"
tweets = tweepy.Cursor(api.search_tweets, q=search_word).items(4)

# Loop through the results and retweet each one
for tweet in tweets:
    try:
        # Retweet o tweet
        tweet.retweet()
        print(f"Retweeted tweet: {tweet.text}")
        
        # Colocando o meu texto no retweet
        custom_text = "SSD NVME M2 com entrega garantida e marca garantida no mercado você encontra aqui: https://lojadupovvo.com.br/collections/mais-vendidos/products/kingspec-m-2-ssd! #ssd #technology"
        api.update_status(f"{custom_text}", in_reply_to_status_id=tweet.id)
        print(f"Successfully added custom text to retweet.")
        
        time.sleep(5)
    except tweepy.TwitterServerError as error:
        print(f"Deu erro ao fazer o retweet: {error}")