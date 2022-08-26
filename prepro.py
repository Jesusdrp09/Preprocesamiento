from sys import flags
import pandas

def preprocesamiento():
    #dataframe
    dataframe = pandas.read_csv("datos.csv", delimiter=",", header=None)
    abreviaciones = pandas.read_csv("abreviaciones.csv", delimiter=";")
    contracciones = pandas.read_csv("contracciones.csv", delimiter=";")
    tweets = pandas.DataFrame(data=dataframe)

    #Reemplazando contracciones
    for i in range(len(contracciones['contraccion'])):
        tweets.iloc[:,10].replace(to_replace=r'\s'+contracciones['contraccion'][i]+'\s', value =" "+contracciones['palabra'][i]+" ", inplace=True, regex=True)
        
    #Reemplazando abreviaciones
    for i in range(len(abreviaciones['abreviacion'])):
        tweets.iloc[:,10].replace(to_replace=abreviaciones['abreviacion'][i]+'\s', value=f" {abreviaciones['palabra'][i]} ", regex=True, inplace=True)

    #Reemplazando nombres de usuario    
    tweets.iloc[:,10].replace(to_replace=r'@[\w]{1,15}', value="username", regex=True, inplace=True)
    
    #Guardando los cambios los cambios
    tweets.to_csv("preprocesamiento.csv")
    

