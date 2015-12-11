import requests
from bs4 import BeautifulSoup

headers = {"user-agent": "Poem scraper, contact at email.com"}

def get_poem_text_from_page(web_address):
    data = requests.get(web_address, headers=headers)

    soup = BeautifulSoup(data.text)

    poem_text=soup(class_="poem")[0].text

    return poem_text.encode("utf-8")

text = get_poem_text_from_page("https://it.wikisource.org/wiki/Canzoniere_(Rerum_vulgarium_fragmenta)/Lasciato_%C3%A0i,_Morte,_senza_sole_il_mondo")

print(text)
