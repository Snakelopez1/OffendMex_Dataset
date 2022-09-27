import tweepy
import pandas as pd

consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""
bearer_token = ""

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token,access_token_secret)

API = tweepy.API (auth)

twts=[]
preclas_agre=[]
preclas_ofen=[]
preclas_vul=[]

fi= "palabrasss.csv"
fs = "OFFENDMEX_Dataset_3.csv"
df = pd.DataFrame()
da = pd.DataFrame()
start = 0
last_word = ""
print("Cargando datos del archivo " + fi)
palabras = pd.read_csv(fi) 
for i in palabras["palabra"]:
    try:
        if last_word == i or last_word == "":
            start = 1;
        if start == 1:
            print("Cargando tweets con la frase o palabra: " + i)
            tweets = API.search_tweets(q=i, lang='es', geocode='19.432608,-99.133209,1000km' ,count="60", tweet_mode='extended')
            for tweet in tweets:
                if 'retweeted_status' in tweet._json:
                    twts.append(tweet._json['retweeted_status']['full_text'])
                else:
                    twts.append(tweet.full_text)
                preclas_ofen.append("0")
                preclas_agre.append("0")
                preclas_vul.append("0")
    except:
        print("Creación interrumpida por limite, la ultima palabra fue: " + i)
        df["Groserias"] = pd.DataFrame(twts)
        df["Agresivo"] = pd.DataFrame(preclas_ofen)
        df["Ofensivo"] = pd.DataFrame(preclas_agre)
        df["Vulgar"] = pd.DataFrame(preclas_vul)
        print("Cargando datos al archivo " + fs)
        df.to_csv(fs,encoding= "UTF-8")
        exit()
df["Groserias"] = pd.DataFrame(twts)
df["Agresivo"] = pd.DataFrame(preclas_ofen)
df["Ofensivo"] = pd.DataFrame(preclas_agre)
df["Vulgar"] = pd.DataFrame(preclas_vul)
print("Cargando datos al archivo " + fs)
df.to_csv(fs,encoding= "UTF-8")
print("Todo Listo")