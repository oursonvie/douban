# -*- coding: utf-8 -*-

# crawler module

from BeautifulSoup import BeautifulSoup
import urllib2
import codecs

def readlink(link):
    response = urllib2.urlopen(link)
    html = response.read()
    pagecontent = BeautifulSoup(html, fromEncoding='gb18030')
<<<<<<< HEAD
    return pagecontent
=======
    return pagecontent
>>>>>>> c8ab6d37bc03e1b6fe1265d3a7eb3419c4ddf005
