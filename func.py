import shutil
import os
import sqlite3 as sql
import imagehash
from PIL import Image
from pdf2image import convert_from_path
import requests
import time
import telebot
import const as c
from datetime import datetime

bot = telebot.TeleBot(c.token)

c = sql.connect("data.db")
cur = c.cursor()

msg = bot.send_message(681875938, 'Beta-script activated. Server time:%s' %
                        str(datetime.strftime(datetime.now(), "%H:%M:%S")))

def schelude():
    get_path = os.path.abspath(os.curdir)

    try:
        # trying to delete+create directories
        shutil.rmtree(os.path.abspath(os.curdir) + '/img')
        shutil.rmtree(os.path.abspath(os.curdir) + '/pdf')
        os.mkdir(get_path + '/img')
        os.mkdir(get_path + '/pdf')
        print('\nDirectory updated\n')
    except:
        # if it is impossile => just create directories
        print('Directories not detected... Creating\n')
        os.mkdir(get_path + '/img')
        os.mkdir(get_path + '/pdf')

    # downloading pdf-file
    url = 'http://rasp.kolledgsvyazi.ru/spo.pdf' #link for your schelude in pdf format
    r = requests.get(url, allow_redirects=True)
    open('pdf/spo.pdf', 'wb').write(r.content)
    print('File downloaded\n')

    # converting pdf-file to img {.jpeg}
    convert_from_path(
        'pdf/spo.pdf', dpi=200, output_folder='img', fmt='jpeg', output_file=str("rasp"))
    print('File converted\nStop working...')

while True:
    try: #trying to download schelude
        schelude()
        cur.execute('''SELECT hash FROM hashes''')
        value = str("%s" % cur.fetchone())
        value2 = str(imagehash.average_hash(Image.open('img/rasp-1.jpg')))
        print("%s" % value , "%s" % value2)

        if value2 == value:
            print("No changes.")
            time.sleep(60)
        else: 
            print("Changed detected. Sending...")
            cur.execute("UPDATE hashes SET hash = '%s'"
                        % (value2))
        
            c.commit()
            
            msg = bot.send_message(681875938, 'Расписание:>')
            bot.send_photo(681875938, photo=open('img/rasp-1.jpg', 'rb'))

            time.sleep(60)
    except: #if schelude is not deteccted time delay 2 sec.
        print("No schelude detected.")
        time.sleep(15)