import time
initial_time = time.time()

import twint
import os 
import prepro

os.remove("datos.csv")
file = open("datos.csv", "w") 

config = twint.Config()
config.Limit = 10
config.Search = "al"
config.Lang = "es"
config.Since = "2020-03-14"
config.Near = "Colombia"
config.Filter_retweets = True
config.Store_csv = True
config.Output = "./datos.csv"
twint.run.Search(config)

prepro.preprocesamiento()
print("Tiempo total: ", time.time()-initial_time)
