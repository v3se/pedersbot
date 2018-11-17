import json 
import requests
import time
import urllib
import random
import datetime
import pyowm
import xml.etree.ElementTree as ET

TOKEN = "561792451:AAE1mJ0GJBe1shUG-SXtwfJ7IFmJZyNKMpA"
URL = "https://api.telegram.org/bot{}/".format(TOKEN)
API_key = '2855e6dab8831245cb2300589875e9cd'
owm = pyowm.OWM(API_key)
api = '9837d485-175c-4021-b79a-fec2abcf504b'


def get_url(url):
    response = requests.get(url)
    content = response.content.decode("utf8")
    return content


def get_json_from_url(url):
    content = get_url(url)
    js = json.loads(content)
    return js


def get_updates(offset=None):
    url = URL + "getUpdates?timeout=100"
    if offset:
        url += "&offset={}".format(offset)
    js = get_json_from_url(url)
    return js

def get_last_update_id(updates):
    update_ids = []
    for update in updates["result"]:
        update_ids.append(int(update["update_id"]))
    return max(update_ids)

def get_last_chat_id_and_text(updates):
    num_updates = len(updates["result"])
    last_update = num_updates - 1
    text = updates["result"][last_update]["message"]["text"]
    chat_id = updates["result"][last_update]["message"]["chat"]["id"]
    return (text, chat_id)

def send_message(text, chat_id):
    text = urllib.parse.quote_plus(text)
    url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
    get_url(url)

def echo_all(updates):
    for update in updates["result"]:
        try:
            do_logic(update)
        except Exception as e:
            print(e)

def do_logic(update):
    message_array = update["message"]["text"].split(" ")
    if message_array[0] == "/kumpi":


        message_array.pop(0)

        random_var = random.choice(message_array) #select random index 

        update["message"]["text"] = random_var
        text = update["message"]["text"]
        chat = update["message"]["chat"]["id"]
        send_message(text, chat)

    if message_array[0] == "/rickroll":
        string = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
        update["message"]["text"] = string
        text = update["message"]["text"]
        chat = update["message"]["chat"]["id"]
        send_message(text, chat)

    if message_array[0] == "/kaljaa?":
        kaljaa = ["Kyllä, tänään voit juoda kaljaa", "Ei, valitettavasti tänään et voi juoda kaljaa", "Voit juoda yhden kaljan"]
        string = random.choice(kaljaa)
        update["message"]["text"] = string
        text = update["message"]["text"]
        chat = update["message"]["chat"]["id"]
        send_message(text, chat)

    if message_array[0] == "/kalja":
        string = "https://media.riemurasia.net/albumit/mmedia/j8/ddh/wuux/197159/1364021240.jpg"
        update["message"]["text"] = string
        text = update["message"]["text"]
        chat = update["message"]["chat"]["id"]
        send_message(text, chat)

    if message_array[0] == "/vapu":
        f_date = datetime.date.today()
        l_date = datetime.date(2019, 5, 1)
        delta = str(l_date - f_date)
        vapu = delta.split(" ")
        
        string = vapu[0]

        update["message"]["text"] = string + " päivää vappuun :)"
        text = update["message"]["text"]
        chat = update["message"]["chat"]["id"]
        send_message(text, chat)

    if message_array[0] == "/iltaa":

        string = "Iltaa iltaa"

        update["message"]["text"] = string
        text = update["message"]["text"]
        chat = update["message"]["chat"]["id"]
        send_message(text, chat)

    if message_array[0] == "/loru":
        loru = ['Kiikeri, kiikeri, kissanpoikaa, koikeri, koikeri, koiranpoikaa, luuputin, luuputin, luppakorvaa, tepytin, tepytin, teppylijalkaa.', 'Kissan leikkiä Mykkyrässä, mäkkyrässä lankavyyhti missä? Sykkyrässä, säkkyrässä kissan käpälissä.', 'pili pili pili pili pilluni syyhyy täytyisi kullilla kutkuttaa kullin kutu se on pillun ruoka ja sitähän se syödä lutkuttaa!' , 'Kuu kiurusta kesään, puoli kuuta peipposesta, västäräkistä vähäsen, pääskysestä ei päivääkään.', 'Satu meni saunaan, pisti laukun naulaan. Satu tuli saunasta, otti laukun naulasta.']
        rand = random.choice(loru)

        update["message"]["text"] = rand
        text = update["message"]["text"]
        chat = update["message"]["chat"]["id"]
        send_message(text, chat)


    if message_array[0] == "/d20":
        if len(message_array)>=2:
            mod = int(message_array[1])
            mod_str = str(mod)
            d20 = random.choice(range(1,21))
            d20_str = str(d20)
            d20_mod = str(d20 + mod)
            update["message"]["text"] = d20_str + "+" + mod_str + "=" + d20_mod
            text = update["message"]["text"]
            chat = update["message"]["chat"]["id"]
            send_message(text, chat)
        else:
            
            d20 = str(random.choice(range(1,21)))
        

            update["message"]["text"] = d20
            text = update["message"]["text"]
            chat = update["message"]["chat"]["id"]
            send_message(text, chat)

    if message_array[0] == "/valosta?":
        observation = owm.weather_at_place('Jyväskylä,FI')
        w = observation.get_weather()
        sunrise = w.get_sunrise_time('iso')
        sunset = w.get_sunset_time('iso')

        update["message"]["text"] = sunrise + sunset
        text = update["message"]["text"]
        chat = update["message"]["chat"]["id"]
        send_message(text, chat)

    if message_array[0] == "/terassille?":
        observation = owm.weather_at_place('Jyväskylä,FI')
        w = observation.get_weather()
        temp1 = w.get_temperature('celsius')
        temp2 = temp1.get('temp')
        sunrise = w.get_sunrise_time('iso')
        sunset = w.get_sunset_time('iso')
        klo = datetime.datetime.now().time()
        print(klo)
        print (sunrise)
        print (sunset)
        status = str(w)
        status = status.split("=")
        status = status[2].replace('>', "")
        if status == "Clear":
            status = "Ei näy pilviä :))"
        if status == "Clouds":
            status = "Pilvistä näyttäis myös olevan :)"
        if status == "Rain":
            status = "Sateenvarjo kanssa mukaan :)"
        if status == "Drizzle":
            status = "Pieniä sadekuuroja luvassa :)"
        if status == "Thunderstorm":
            status = "Ukkostaa ehkä :)"
        if status == "Snow":
            status = "Lunta sataa ja kaikkia vituttaa :)"
        if klo > datetime.time(hour=7, minute=00):
            aika = "Täydellinen ajankohta terassille. "
        if klo <= datetime.time(hour=7, minute=00):
            aika = "Terassi ei varmaa oo auki tähän aikaan :( "

        if klo >= datetime.time(hour=23, minute=00):
            aika = "Hieman myöhä ehkä terassille :( "


        


        if 0 < temp2 < 10:
            temp3 = aika + str(temp2) + " C kannattaa laittaa takki."
        if 10 <= temp2 <= 15:
            temp3 = aika + str(temp2) + " C suht lämpönen. Ei ehkä tarvii takkia." 
        if temp2 > 15:
            temp3 = aika + str(temp2) + " C vaimari päälle. Helvetin lämmin." 
        if temp2 <= 0:
            temp3 = aika + str(temp2) + " C vitun kylmä." 
        



        update["message"]["text"] = temp3 + " " + str(status)
        text = update["message"]["text"]
        chat = update["message"]["chat"]["id"]
        send_message(text, chat)


    if message_array[0] == "/peders":
        update["message"]["text"] = "Moi olen PedersBot. Osaan tehdä seuraavaa: \n /kumpi <vaihtoehto_1> <vaihtoehto_2> <vaihtoehto_n> - Valitsen antamistasi vaihtoehdoista mielestäni parhaimman vaihtoehdon :) \n /kalja - Haen sinulle kuvan suosikkijuomastani :) \n /vapu - Vappu on lempijuhlani. Lasken monta päivää vappuun on :) \n /terassille? - Kerron millainen varustus kannattaa olla terassille lähtiessä :) \n Isäni Robbani opettaa minulle uusia asioita joka päivä! Kirjoita \peders niin näät mitä osaan tehdä :))))))"
        text = update["message"]["text"]
        chat = update["message"]["chat"]["id"]
        send_message(text, chat)

    if message_array[0] == "/tissit":
        update["message"]["text"] = "https://d1rgjmn2wmqeif.cloudfront.net/r/b/26050.jpg"
        text = update["message"]["text"]
        chat = update["message"]["chat"]["id"]
        send_message(text, chat)


    if message_array[0] == "/vierre":
        file = open('/var/www/html/temps.txt', 'r')
        temp_beer = file.read(4)
        file.close() 
        update["message"]["text"] = str(temp_beer)
        text = update["message"]["text"]
        chat = update["message"]["chat"]["id"]
        send_message(text, chat)

def main():
    last_update_id = None
    while True:
        #print("getting updates")
        updates = get_updates(last_update_id)
        if updates["result"]:
	        if len(updates["result"]) > 0:
	            last_update_id = get_last_update_id(updates) + 1
	            echo_all(updates)
	        time.sleep(0.5)


if __name__ == '__main__':
    main()
