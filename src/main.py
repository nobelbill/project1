__author__ = '1002097'

import urllib
from bs4 import BeautifulSoup
import re
url= 'http://comic.naver.com/webtoon/list.nhn?titleId=20853'
page='&page='
page_num=1
def num_parse (title):
#    print title
    first = title.split('.')
    if(first[0].isdigit()):
        print first[0]
        #return (first[0],first[1])
        return (first)

def title_parse (tag) :
    if(tag.img['title'] != None):
        num_parse(tag.img['title'])
#        print tag.img['title']


def page_parse (page_html):
    for parse in bs.find_all('body')[0].find_all('a') :
        if(parse.find('img',title= re.compile('.')) != None):
            title_parse(parse)
#    print parse.find(id="alt")



#for link in bs.find_all('a') :
#    if str(link).find('page=2"') != -1 :

for page_num in range(1,200):
    print page_num
    real_url=url + page + str(page_num)
    reponse = urllib.urlopen(real_url)
    html = reponse.read()
    parse_html =  html.split()
    bs = BeautifulSoup(html)
    page_parse(bs)


#print bs.prettify()
#print bs.find_all('img')

#for string in bs.strings:
#   print (repr(string))


