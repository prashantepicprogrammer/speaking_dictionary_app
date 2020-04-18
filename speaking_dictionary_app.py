import requests
import bs4
from gtts import gTTS
import playsound

search = input('Search Anything : ')

def speech(msg):
    language = 'en'
    msgobj = gTTS(text=msg , lang=language , slow=False)
    msgobj.save('speech.mp3')
    playsound.playsound('speech.mp3' , True)

def fetchData(search):
    res = requests.get('https://en.wikipedia.org/wiki/'+search)
    soup = bs4.BeautifulSoup(res.text , 'lxml')
    data = soup.select('p')
    print(data[1].text)
    speech(data[1].text)

fetchData(search)
