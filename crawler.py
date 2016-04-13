# -*- coding: utf-8 -*-

# crawler module

from BeautifulSoup import BeautifulSoup
import urllib2
import codecs
import time

def readlink(link):
    
    time.sleep(0.5)
    hdr = {
        'cookie': 'bid="gGaaSvR57os"; ll="118371"; ct=y; __ads_session=o3Bwsr+TtAjElwoDpgA=; viewed="3193304_6425619_3824579_1448639_1686536_1463600_10448971_1397392_26291447_26596288"; ps=y; ue="aolly2001@hotmail.com"; dbcl2="63146836:xUc5hrT/DpI"; ck="LK2i"; ap=1; __utmt=1; __utma=30149280.1090969023.1460440577.1460532723.1460534860.7; __utmb=30149280.14.10.1460534860; __utmc=30149280; __utmz=30149280.1460520253.4.3.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/people/sucks1990/; __utmv=30149280.6314; push_noty_num=0; push_doumail_num=0'
    }

    req = urllib2.Request(link, headers=hdr)
    response = urllib2.urlopen(req)

# cough cough cough
#
#    try:
#        response = urllib2.urlopen(req)
#        html = response.read()
#        pagecontent = BeautifulSoup(html, fromEncoding='gb18030')
#        return pagecontent
#    except urllib2.HTTPError, e:
#        print e.fp.read()
    
    
#    response = urllib2.urlopen(link)
    html = response.read()
    pagecontent = BeautifulSoup(html)
    return pagecontent

