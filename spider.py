import sys
import json
import codecs
import datetime
import urllib
import urllib2
import time
from lxml import etree

def parser(url, xpath):
    f = urllib2.urlopen(url, timeout=5)
    content = f.read()
    f.close()
    tree = etree.HTML(content)
    return tree.xpath(xpath)

def download(url, f):
    sleep = 1.0
    while True:
        try:
            data = urllib2.urlopen(url).read()
            with open(f, 'wb') as fp:
                fp.write(data)
            break
        except Exception, e:
            print >> sys.stderr, 'download fail, retry. s = ' % e
            time.sleep(sleep)
            sleep = sleep * 2
            continue
        

if __name__ == '__main__':

    root = sys.argv[1]

    url = 'http://sc.chinaz.com'    
    suffix_list = ['', '_2', '_3', '_4', '_5', '_6', '_7', '_8', '_9', '_10']
    
    for suffix in suffix_list:
    
        index_url = url + '/ppt/index' + suffix + '.html'
        print >> sys.stderr, 'index_url :', index_url
        content_xpath = '/html/body/'
        content_xpath += 'div[@class=\'all_wrap\']/'
        content_xpath += 'div[@class=\'ppt_body\']/'
        content_xpath += 'div[@class=\'ppt_text\']/'
        content_xpath += 'div[@id=\'container\']/'
        content_xpath += 'div/'
        content_xpath += 'div/'
        content_xpath += 'a/'
        content_xpath += '@href'
        
        for s in parser(index_url, content_xpath):
            content_url = url + s
            print >> sys.stderr, ' content_url :', content_url
            download_xpath = '/html/body'
            download_xpath += '/div[@class=\'all_wrap\']'
            download_xpath += '/div[@class=\'down_wrap\']'
            download_xpath += '/div[@class=\'left\']'
            download_xpath += '/div[@class=\'down_adress\']'
            download_xpath += '/div[@class=\'down_a\']'
            download_xpath += '/div[@class=\'downcon\']'
            download_xpath += '/div[@class=\'downbody\']'
            download_xpath += '/div[@class=\'xunlei\']'
            download_xpath += '/a[2]'
            download_xpath += '/@href'
            
            for download_url in parser(content_url, download_xpath):
                print download_url
                print >> sys.stderr, '  download_url :', download_url
                # line_arr = download_url.strip().split('/')
                # f = line_arr[-1]
                # download(download_url, root + '/' + f)
                