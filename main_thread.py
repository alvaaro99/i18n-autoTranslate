import json
import sys
import threading
from googletrans import Translator

json_to_translate = sys.argv[1]
lang_translate = sys.argv[2]

file = open(json_to_translate)
data: dict = json.load(file)

translator = Translator()

result:dict = {}

def translate(key,value,lang):
    response = translator.translate(value,dest=lang)
    result[key] = response.text
    print(response.origin+' --> '+response.text)

path_of_file = json_to_translate[:json_to_translate.rindex('/')+1]

works = []
for key,value in data.items():
    work = threading.Thread(target=translate,args=[key,value,lang_translate])
    works.append(work)
    work.start()

for work in works:
    work.join()

print(result)
with open(path_of_file+lang_translate+'.json', 'w') as outfile:
    json.dump(result, outfile)