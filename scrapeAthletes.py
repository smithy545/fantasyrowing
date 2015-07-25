import urllib

opener = urllib.request.FancyURLopener({})
url = "http://www.rowingone.com/n_search_bio_result.fwx"
f = opener.open()
