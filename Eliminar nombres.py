import pandas

#dataframe
dataframe = {'col1':["Hola A. pa'lante @soyeduardo_1","Mucho gusto @jesusadmin", "(a)", "acept."], 'col2':["Hola A. pa'lante @soyeduardo_1","Mucho gusto @jesusadmin", "(a)", "acept."]}
print(dataframe)
abreviaciones = pandas.read_csv("abreviaciones.csv", delimiter=";")
contracciones = pandas.read_csv("contracciones.csv", delimiter=";")
print(abreviaciones)
tweets = pandas.DataFrame(data=dataframe)

#Reemplazando abreviaciones
for i in range(len(abreviaciones['abreviacion'])):
    tweets['col1'].replace(to_replace=abreviaciones['abreviacion'][i], value = abreviaciones['palabra'][i], regex=True, inplace=True)

#Reemplazando contracciones
for i in range(len(contracciones['contraccion'])):
    tweets['col1'].replace(to_replace=contracciones['contraccion'][i], value = contracciones['palabra'][i], regex=True, inplace=True)

#Reemplazando nombres de usuario    
tweets['col1'].replace(to_replace=r'@[\w]{1,15}', value="username", regex=True, inplace=True)

#Mostrando los cambios
print(tweets)


