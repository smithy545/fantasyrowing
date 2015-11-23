from bs4 import BeautifulSoup

import requests, sys, os

currentmax = 45449

if len(sys.argv) > 1:
    start = int(sys.argv[1])
else:
    start = 0

if not os.path.exists("rowingone/"):
    os.makedirs("rowingone/")

for i in range(start, currentmax):
    url = "http://www.rowingone.com/n_bio_rower.fwx?no_id=" + str(i)
    try:
        r = requests.get(url)
        print "Athlete " + str(i) + " successfully got"
    except Exception as inst:
        print type(inst)
        print inst

    try:
        f = open("rowingone/athlete-" + str(i) + ".html", 'w')
        f.write(r.text.encode('utf8'))
        f.close()
        print "Athlete " + str(i) + " successfully written"
    except Exception as inst:
        print type(inst)
        print inst
    
