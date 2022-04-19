import json
import sys
from googletrans import Translator

json_to_translate = sys.argv[1]
lang_translate = sys.argv[2]

file = open(json_to_translate)
data: dict = json.load(file)

translator = Translator()

result:dict = {}
path_of_file = json_to_translate[:json_to_translate.rindex('/')+1]

for key,value in data.items():
    response = translator.translate(value,dest=lang_translate)
    result[key] = response.text
    print(response.origin+' --> '+response.text)

with open(path_of_file+lang_translate+'.json', 'w') as outfile:
    json.dump(result, outfile)



# print(list(data.values()))
# translations = translator.translate(['hola','adios','como estas'],dest='en')

# for translation in translations:
#     print(translation)