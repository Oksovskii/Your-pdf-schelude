import sqlite3 as sql
import test
from PIL import Image
import imagehash

str(imagehash.average_hash(Image.open('img/rasp-1.jpg')))


c = sql.connect("game.db")
cur = c.cursor()

try:
    cur.execute('''SELECT hash FROM hashes''')
    print(cur.fetchone())
except:

    print("DB is noy difined..\nCreating")
    cur.execute('''CREATE TABLE hashes
             (hash)''')

    cur.execute("""INSERT INTO hashes (hash)
                    VALUES ('%s')""" % (
                        str(imagehash.average_hash(Image.open('img/rasp-1.jpg')))))

    c.commit()
    print("DB created")