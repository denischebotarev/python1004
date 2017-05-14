import requests

url = 'https://translate.yandex.net/api/v1.5/tr.json/translate?'
key = 'trnsl.1.1.20170509T173115Z.7389ba585fa6cfbd.673ddf47a800eab1bf15efb75ffdc3db68bcba5f'
text = 'привет'
lang = 'ru-en'
r = requests.post(url, data={'key': key, 'text': text, 'lang': lang})

print(r.text)
print(r)