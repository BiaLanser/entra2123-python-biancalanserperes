import requests

def translate(text, lang):
    url = "https://translate.yandex.net/api/v1.5/tr.json/translate"
    payload = {
        'key': 'trnsl.1.1.20230831T144244Z.c6f503de2167ce05.c5e2111a7ec5b04862675a46fa39747ed509d125',
        'text': text,
        'lang': lang,
    }
    response = requests.get(url, params=payload)
    return response.json()["text"][0]

def main():
    text_translate = input("Digite o texto que deseja traduzir: ")
    translation_en = translate(text_translate, 'en')
    translation_es = translate(text_translate, 'es')
    
    print("Tradução em inglês: ", translation_en)
    print("Tradução em espanhol: ", translation_es)

if __name__ == '__main__':
    main()
