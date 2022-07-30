import pandas
import os
def preprocesamiento():
    #dataframe
    dataframe = pandas.read_csv("datos.csv", delimiter=",")
    abreviaciones = pandas.read_csv("abreviaciones.csv", delimiter=";")
    contracciones = pandas.read_csv("contracciones.csv", delimiter=";")
    tweets = pandas.DataFrame(data=dataframe)

    #Reemplazando contracciones
    for i in range(len(contracciones['contraccion'])):
        tweets.iloc[:,10].replace(to_replace=contracciones['contraccion'][i], value = contracciones['palabra'][i], regex=True, inplace=True)
        
    #Reemplazando abreviaciones
    for i in range(len(abreviaciones['abreviacion'])):
        tweets.iloc[:,10].replace(to_replace=abreviaciones['abreviacion'][i], value = abreviaciones['palabra'][i], regex=True, inplace=True)

    #Reemplazando nombres de usuario    
    tweets.iloc[:,10].replace(to_replace=r'@[\w]{1,15}', value="username", regex=True, inplace=True)
    
    #Guardando los cambios los cambios
    tweets.to_csv("datos.csv")
    


