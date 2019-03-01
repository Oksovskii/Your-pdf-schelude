import sqlite3 as sql
import hashlib

c = sql.connect("data.db")
cur = c.cursor()

cur.execute('''CREATE TABLE hashes
            (hash)''')

cur.execute("""INSERT INTO hashes (hash) 
                     VALUES('%s')""" % (
                        str(hash("123"))))

c.commit()
cur.execute('''SELECT hash FROM hashes''')
print("DB created", "\nHash: {%s}" % cur.fetchone())
c.close()