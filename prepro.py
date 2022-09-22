from sys import flags
import pandas
import string
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')

def preprocesamiento():
    #dataframe
    dataframe = pandas.read_csv("datos.csv", delimiter=",", header=None)
    abreviaciones = pandas.read_csv("abreviaciones.csv", delimiter=";")
    contracciones = pandas.read_csv("contracciones.csv", delimiter=";")
    etiquetas = pandas.read_csv("etiquetas.csv", delimiter=";")
    tweets = pandas.DataFrame(data=dataframe)

    #Reemplazando contracciones
    for i in range(len(contracciones['contraccion'])):
        tweets.iloc[:,10].replace(to_replace=r'\s'+contracciones['contraccion'][i]+'\s', value =" "+contracciones['palabra'][i]+" ", inplace=True, regex=True)
        
    #Reemplazando abreviaciones
    for i in range(len(abreviaciones['abreviacion'])):
        tweets.iloc[:,10].replace(to_replace=abreviaciones['abreviacion'][i]+'\s', value=f" {abreviaciones['palabra'][i]} ", regex=True, inplace=True)

    #Reemplazando nombres de usuario    
    tweets.iloc[:,10].replace(to_replace=r'@[\w]{1,15}', value="username", regex=True, inplace=True)
    
    #Reemplazo de Urls
    tweets.iloc[:,10].replace("http\S+", " URL ", regex=True, inplace=True)

    #Eliminación de numeros
    tweets.iloc[:,10].replace("[0-9]+", " ", regex=True, inplace=True)

    #Añadir etiquetas(Reemplazar simbolos por etiquetas)
    for i in range(len(etiquetas['simbolos'])):
        tweets.iloc[:,10].replace(to_replace=etiquetas['simbolos'][i], value= etiquetas['etiquetas'][i], regex=True, inplace=True)
    
    #Remover stopwords
    stop_words = set(stopwords.words('spanish'))
    for i in stop_words:
        tweets.iloc[:,10].replace(to_replace=r'\s'+i+'\s', value= " ", regex=True, inplace=True)
    
    #Poner en minúscula
        tweets.iloc[:,10] = tweets.iloc[:,10].str.lower()

    #Eliminar signos de puntuación
        tweets.iloc[:,10].replace(to_replace=r"[\, | \. | \: | \; | \.{3}] ", value= "", regex=True, inplace=True)

    #Guardando los cambios los cambios
    tweets.to_csv("preprocesamiento.csv")
    

