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

fs = "Prueba.csv"
tweet_b=["#musica","#noticias","#peliculas","#México","#politica","#videojuegos","#comida","#mascotas","#juegos","#series"]
df = pd.DataFrame()
aux = API.closest_trends(lat='19.432608', long='-99.133209')
aux1 = API.get_place_trends(id='23424900')
trends = set([trend['name'] for trend in aux1[0]['trends']])
for i in trends:
    print("Cargando tweets con la frase o palabra: " + i)
    tweets = API.search_tweets(q=i, lang='es', geocode='19.432608,-99.133209,1000km' ,count="380", tweet_mode='extended')
    for tweet in tweets:
        if 'retweeted_status' in tweet._json:
            twts.append(tweet._json['retweeted_status']['full_text'])
        else:
            twts.append(tweet.full_text)
        preclas_ofen.append("0")
        preclas_agre.append("0")
        preclas_vul.append("0")
for i in tweet_b:
    print("Cargando tweets con la frase o palabra: " + i)
    tweets = API.search_tweets(q=i, lang='es', geocode='19.432608,-99.133209,1000km' ,count="380", tweet_mode='extended')
    for tweet in tweets:
        if 'retweeted_status' in tweet._json:
            twts.append(tweet._json['retweeted_status']['full_text'])
        else:
            twts.append(tweet.full_text)
        preclas_ofen.append("0")
        preclas_agre.append("0")
        preclas_vul.append("0")
df["Groserias"] = pd.DataFrame(twts)
df["Agresivo"] = pd.DataFrame(preclas_ofen)
df["Ofensivo"] = pd.DataFrame(preclas_agre)
df["Vulgar"] = pd.DataFrame(preclas_vul)
print("Cargando datos al archivo " + fs)
df.to_csv(fs,encoding= "UTF-8")
print("Todo Listo")