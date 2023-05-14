# Webscrapping
El webscrapping o raspado, es una técnica que sirve para extraer información de un sitio web, en este proyecto se utilizó la librería Twint para extraer tweets de la plataforma Twitter. Se hace filtros por idioma, fechas, cantidad de tweets, etc. Podemos ver un ejemplo en el archivo [ejemplo.py]([Preprocesamiento/ejemplo.py at master · Jesusdrp09/Preprocesamiento · GitHub](https://github.com/Jesusdrp09/Preprocesamiento/blob/master/ejemplo.py))
# Preprocesamiento
En este proyecto se aplican 9 técnicas de preprocesamiento: 
- Reemplazo de contracciones: desde el archivo contracciones.csv se extraen las contracciones más comunes usadas en el diario vivir de los colombianos y se reemplazan por la palabra o frase estandarizada.
- Reemplazo de abreviaciones: desde el archivo abreviaciones.csv se extraen las abreviaciones más comunes usadas en el diario vivir de los colombianos y se reemplazan por la palabra o frase estandarizada.
- Reemplazo de nombres de usuario: los tweets algunas veces contienen nombres de usuarios como @juanPerea000, como estos nombres de usuarios no le aportan información a los modelos de inteligencia artificial, podemos reemplazar todos la palabra "USERNAME".
- Reemplazo de URLs: las URLs no le aportan información a los modelos de inteligencia artificial, es por ello que se reemplazan las URL por la palabra "URL"
- Eliminación de números: los números suelen aportar información mínima al modelo, es por ello que algunos casos se pueden omitir, en el proyecto actual simplemente se eliminan todos los números. 
- Añadir etiquetas: algunas veces para expresarnos utilizamos emojis como: 😊😂😒😢, estos emojis pueden ser reemplazados por las emociones que representan como "felicidad", "alegría", "enojo" o "tristeza", esto con el fin de estandarizar las palabras que recibe el modelo y así otorgarle más información.
- Eliminación de stopwords: los "stopwords" son palabras de un idioma que solas carecen de sentido como: el, en, un, entre otros. Estás palabras se pueden eliminar en modelos de Machine Learning, ya que su aporte es muy poco o nulo al análisis de sentimiento. 
- Lowercasing: Hola, hola, HOLa y HOla quieren decir lo mismo, es por ello que se aplica la técnica de lowercasing, la cual ayuda a colocar todas las letras en minúscula. 
- Eliminar signos de puntuación: los signos de puntuación no aportan mucha información al modelo, además, aparecen no importando si el sentimiento que se expresa en el tweet es positivo, negativo o neutro. Es por ello que se eliminan todos los signos de puntuación. 


Podemos ver esta información en el archivo [prepro.py]([Preprocesamiento/prepro.py at master · Jesusdrp09/Preprocesamiento · GitHub](https://github.com/Jesusdrp09/Preprocesamiento/blob/master/prepro.py))
