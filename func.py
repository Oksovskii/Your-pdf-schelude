import shutil
import os
import sqlite3 as sql
import imagehash
from PIL import Image
from pdf2image import convert_from_path
import requests


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
    images = convert_from_path(
        'pdf/spo.pdf', dpi=200, output_folder='img', fmt='jpeg', output_file=str("rasp"))
    print('File converted\nStop working...')

def chek_hash():
    c = sql.connect("game.db")
    cur = c.cursor()
    cur.execute('''SELECT hash FROM hashes''')
    value = str("%s" % cur.fetchone())
    value2 = str(imagehash.average_hash(Image.open('img/rasp-1.jpg')))
    print("%s" % value , "%s" % value2)

    if value2 == value:
        print("bomzh")
    else: 
        print("hay csta")
        cur.execute("UPDATE hashes SET hash = '%s'"
                      % (value2))
        c.commit()
        c.close()

if __name__ == "__main__":
    chek_hash()