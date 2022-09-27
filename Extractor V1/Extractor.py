import tweepy
import pandas as pd

consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""
bearer_token = ""

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API (auth)

fi = "Groserias.txt"
fs = "OFFENDMEX_Dataset.csv"
twts=[]
preclas=[]
tweet_b=["#musica","#noticias","#peliculas","#México","#politica","#videojuegos","#comida","#mascotas","#juegos","#series"]
df = pd.DataFrame()
print("Cargando datos del archivo " + fi)
Malpals = pd.read_csv(fi,sep='-')
print("Buscando tweets conforme a la lista de palabras del archivo " + fi)

for i in range(len(Malpals)):
    print("Cargando tweets con la palabra: " + Malpals["Groserias"][i])
    tweets = api.search_tweets(q=Malpals["Groserias"][i], geocode='19.432608,-99.133209,1000km' ,count="5")
    for tweet in tweets:
        twts.append(tweet.text)
        if Malpals["Preclas"][i] == 1:
           preclas.append("1")
        else:
            preclas.append("SP")
for i in range(len(tweet_b)):
    print("Cargando tweets con la frase o palabra: " + tweet_b[i])
    tweets = api.search_tweets(q=tweet_b[i], geocode='19.432608,-99.133209,1000km' ,count="60")
    for tweet in tweets:
       twts.append(tweet.text)
       preclas.append("SP")
   
df["Groserias"] = pd.DataFrame(twts)
df["Ofensivo"] = pd.DataFrame(preclas)
print("Cargando datos al archivo " + fs)
df.to_csv(fs,encoding= "UTF-8")
print("Todo Listo")