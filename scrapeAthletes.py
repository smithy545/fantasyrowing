# -*- coding:utf-8 -*-
from types import *
from bs4 import BeautifulSoup
from datetime import date
import os, sqlite3, calendar, sys

def getInfo(tag):
    info = {}
    for item in tag.find_all("li"):
        info[item.find("div", "dt").text] = item.find("div", "dd").text
    return info

def quotify(s):
    if type(s) == NoneType:
        return '""'
    if type(s) != UnicodeType:
        s = unicode(s)
    return u'"' + s + u'"'

def getMonth(month):
    m = 0
    try:
        m = list(calendar.month_name).index(month)
    except:
        m = list(calendar.month_abbr).index(month)
    finally:
        return m


athleteDict = {}
raw = ""

for filename in os.listdir("athletes_raw/worldrowing"):
    try:
        f = open("athletes_raw/worldrowing/" + filename, 'r')
        raw = f.read()
        f.close()
    except:
        print "Could not open " + filename
        continue
        
    soup = BeautifulSoup(raw, "html.parser")

    detailslist = soup.select("ul.details.list-unstyled")
    if detailslist:
        athleteDict[soup.title.text] = getInfo(detailslist[0])
    else:
        athleteDict[soup.title.text] = {}

conn = sqlite3.connect("test.db")
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS athlete (
                id INTEGER PRIMARY KEY,
                name text,
                height real,
                weight real,
                gender text,
                residence text,
                clubs text,
                startedrowing integer,
                birthdate text,
                age integer)''')

for i, key in enumerate(athleteDict):
    athleteInfo = athleteDict[key]
    name = key
    height =        athleteInfo.get("Height")
    weight =        athleteInfo.get("Weight")
    gender =        athleteInfo.get("Gender")
    residence =     athleteInfo.get("Place of residence")
    clubs =         athleteInfo.get("Clubs")
    startedrowing = athleteInfo.get("Started Rowing in")
    birthdate =     athleteInfo.get("Birthdate")
    age = None

    if height:
        height = height.split("cm")[0]
    if weight:
        weight = weight.split("kg")[0]
    if birthdate:
        birthdate = birthdate.split(" ")
        month = getMonth(birthdate[1])
        if month != 0:
            birthdate = date(int(birthdate[2]), month, int(birthdate[0]))
            age = (date.today() - birthdate).days / 365
        else:
            birthdate = None
            age = None

    info = [quotify(field) for field in [i, name, height, weight, gender, residence, clubs, startedrowing, birthdate, age]]
     
    try:
        c.execute(u"INSERT INTO athlete VALUES (" + u",".join(info) + u");")
    except Exception as e:
        print e
        print "Error adding athlete " + str(i)
        
conn.commit()
conn.close()
