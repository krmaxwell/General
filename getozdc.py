import urllib2
import logging

apiurl = 'http://api.ozdc.net/api.php?aid='

def get_URL(url):
    try:
        response = urllib2.urlopen(url.encode("utf8"))
        return response
    except urllib2.URLError, e:
        if hasattr(e,'reason'):
            logging.warning('urlopen() returned error %s\n',e.reason)
        elif hasattr(e,'code'):
            logging.warning('Server couldn\'t fulfill request: %s\n',e.code)
        else:
            logging.warning('Opened %s with response code %s',url,response.getcode())

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

with open("ozdc.json", 'wb') as outfile:
    for atkid in range(1,4720):
        url = apiurl+str(atkid)
        logging.info("Fetching ID %d", atkid)
        response = get_URL(url)
        if response:
            outfile.write(response.read())
