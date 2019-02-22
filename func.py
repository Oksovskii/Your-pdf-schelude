import shutil
import os
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
    url = 'http://rasp.kolledgsvyazi.ru/spo.pdf'
    r = requests.get(url, allow_redirects=True)
    open('pdf/spo.pdf', 'wb').write(r.content)
    print('File downloaded\n')

    # converting pdf-file to img {.jpeg}
    images = convert_from_path(
        'pdf/spo.pdf', dpi=200, output_folder='img', fmt='jpeg', output_file=str("rasp"))
    print('File converted\nStop working...')
