# fantasyrowing
A basic system for developing fantasy rowing teams during the IRA season

Well here it is. I didn't think I'd ever actually share this code so it's uncommented and ugly. I will be updating it sporadically and try to make it more readable and editable.

The code is segmented into two parts. One part are the scrapers which are pretty self explanatory. One scrapes from worldrowing.com directly and another from a database worldrowing uses called rowingone.com. They are both in the athletes_raw folder

The second part is the parsers. One parser gets pretty much all the info from the available files in the athletes_raw folder. The other one just touches up on the names of the athletes which aren't formatted in the first parser. This system, mostly arose cause I'm lazy. I think I'll fix it soon.

Anyway, do what you will with this code, it's not useful enough to warrant making a license.

Sidenote: The scrapers use very inefficient methods of downloading in that they download one file at a time and wait until it's complete before moving on. A better implementation would use subroutines to download multiple at once and parse them as it goes. For my purposes I didn't feel it was worth the effort so I just ran it for a while with my computer connected to the ethernet (it took a few hours for worldrowing and significantly longer for rowingone) but I encourage somebody less lazy than me to work on it. If not I'll probably improve this later (perhaps using lua to scrape as I know subroutines in that language better).

Python libraries required:

- BeautifulSoup4
- sqlite3
