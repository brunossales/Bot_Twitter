import tweepy
import os
from dotenv import load_dotenv
import time

load_dotenv()

auth = tweepy.OAuthHandler(os.environ['api_key'], os.environ['api_key_secret'])
auth.set_access_token(os.environ['acess_token'], ['acess_token_secret'])

api = tweepy.API(auth)

search_word = "ssd"

# procure pelos tweets com a palavra "ssd"
tweets = tweepy.Cursor(api.search_tweets, q=search_word).items(50)

for tweet in tweets:
    try:
        # Retweet o tweet
        tweet.retweet()
        print(f"Retweeted tweet: {tweet.text}")
        
        # Colocando o meu texto no retweet
        custom_text = "SSD NVME M2 com entrega garantida e marca garantida no mercado você encontra aqui: https://lojadupovvo.com.br/collections/mais-vendidos/products/kingspec-m-2-ssd! #ssd #technology"
        api.update_status(f"{custom_text}", in_reply_to_status_id=tweet.id)
        print(f"Retweerd adicionado com sucesso!.")
        
        time.sleep(5)
    except tweepy.TwitterServerError as error:
        print(f"Deu erro ao fazer o retweet: {error}")