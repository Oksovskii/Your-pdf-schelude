import sqlite3 as sql
import test
from PIL import Image
import imagehash

c = sql.connect("game.db")
cur = c.cursor()

try:
    cur.execute('''SELECT hash FROM hashes''')
    print("Value in table before hashing",cur.fetchone())
    print("Hash:",str(imagehash.average_hash(Image.open('img/rasp-1.jpg'))))
    cur.execute("UPDATE hashes SET hash = '%s'"
                      % (
                        str(imagehash.average_hash(Image.open('img/rasp-1.jpg')))))
    c.commit()
    cur.execute('''SELECT hash FROM hashes''')
    print("Value in table after hashing",cur.fetchone())
    c.close()
except:

    print("DB is noy difined..\nCreating")
    cur.execute('''CREATE TABLE hashes
             (hash)''')

    cur.execute("""INSERT INTO hashes (hash) 
                     VALUES('%s')""" % (
                        str(imagehash.average_hash(Image.open('img/rasp-1.jpg')))))

    c.commit()
    c.close()
    print("DB created")