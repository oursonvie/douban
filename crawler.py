# -*- coding: utf-8 -*-

# crawler module

from BeautifulSoup import BeautifulSoup
import urllib2
import codecs

def readlink(link):
    hdr = {
        "Accept-Language": "en-US,en;q=0.5",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Referer": "http://thewebsite.com",
        "Connection": "keep-alive" 
    }
    # response = urllib2.urlopen(link)
    req = urllib2.Request(link, headers=hdr)


#    try:
#        response = urllib2.urlopen(req)
#        html = response.read()
#        pagecontent = BeautifulSoup(html, fromEncoding='gb18030')
#        return pagecontent
#    except urllib2.HTTPError, e:
#        print e.fp.read()
        
    response = urllib2.urlopen(req)
    html = response.read()
    pagecontent = BeautifulSoup(html, fromEncoding='gb18030')
    return pagecontent

