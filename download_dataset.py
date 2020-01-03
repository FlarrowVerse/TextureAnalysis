import requests
import sys
import shutil
import re
import threading
from bs4 import BeautifulSoup as soup

THREAD_COUNTER = 0
THREAD_MAX     = 5

def get_source( link ):
    r = requests.get( link )
    if r.status_code == 200:
        return soup(r.text, features="html.parser")
    else:
        sys.exit( "[~] Invalid Response Received." )

def filter( html ):
    imgs = html.findAll( "img" )
    if imgs:
        return imgs
    else:
        sys.exit("[~] No images detected on the page.")

def requesthandle( link, name ):
    global THREAD_COUNTER
    THREAD_COUNTER += 1
    try:
        r = requests.get( link, stream=True )
        if r.status_code == 200:
            r.raw.decode_content = True
            f = open( name, "wb" )
            shutil.copyfileobj(r.raw, f)
            f.close()
            print("[*] Downloaded Image: %s" % name)
    except Exception as error:
        print("[~] Error Occured with %s : %s" % (name, error))
    THREAD_COUNTER -= 1

def main():
    for i in range(1, 113):
        requesthandle('http://www.ux.uis.no/~tranden/brodatz/D'+str(i)+'.gif', 'D'+str(i)+'.jpg')


if __name__ == "__main__":
    main()
