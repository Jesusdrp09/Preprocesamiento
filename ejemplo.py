import twint 
import os
import prepro
import time

initial_time = time.time()
os.remove("datos.csv")
file = open("datos.csv", "w")

config = twint.Config()
config.Search = "feliz OR triste OR covid OR coronavirus"
config.Lang = "es"
config.Since = "2020-03-14"
config.Near = "Colombia" 
config.Filter_retweets = True
config.Store_csv = True
config.Output = "./datos.csv"
twint.run.Search(config)

prepro.preprocesamiento()
print("Tiempo total: ", time.time()-initial_time)