# -*- coding: utf-8 -*-

import crawler
import mongo

# homepage of a user on douban
homepage = 'https://www.douban.com/people/sucks1990/'
user_name = homepage.split('/')[4]

music_server = 'https://music.douban.com/people/'
# there are always 3 categories of everything
categories = ['do','wish','collect']

page_cache = []



def getMusic():
    
    for pages_link in page_cache:
        
        content = crawler.readlink(pages_link)        
        items = content.find('div', attrs = {'class':'grid-view'}).findAll('div', attrs = {'class':'item'})
        for item in items:
            # item in pic
            cd_link = item.find('div', attrs = {'class':'pic'}).find('a')['href']
            cd_title = item.find('div', attrs = {'class':'pic'}).find('a')['title']
            cd_cover = item.find('div', attrs = {'class':'pic'}).find('img')['src']
            
            # item in info
            cd_intro = item.find('div', attrs = {'class':'info'}).find('li', attrs={'class':'intro'}).text
            cd_addtime = item.find('div', attrs = {'class':'info'}).find('span', attrs={'class':'date'}).text
            try:
                cd_mannual_tags = item.find('div', attrs = {'class':'info'}).find('span', attrs={'class':'tags'}).text[3:]
            except AttributeError:
                cd_mannual_tags = 'No Comment'
            
            cd_detail = {
                'title': cd_title,
                'link': cd_link,
                'cover': cd_cover,
                'intro': cd_intro,
                'add_date': cd_addtime,
                'tag_by_user': cd_mannual_tags
            }
            
            mongo.insert_cd(cd_detail)

def getNextPage(link):
    content = crawler.readlink(link)
    try:
        next_page = content.find('span', attrs={'class':'next'}).find('a')['href']
        page_cache.append(next_page)
        getNextPage(next_page)
    except TypeError:
        print('Reach to the last page')
    
    
def getAllPages():
    
    for category in categories: 
        starting_page = music_server + user_name + '/' + category
        print starting_page
        content = crawler.readlink(starting_page)
        
        print starting_page
        getNextPage(starting_page)
       
        
        for pages in page_cache:
            print pages

            
# i was planning to get all the detail data of the CD
# turns out only scroe i was interested
def getOfficialDetail():
    cd_urls = mongo.get_cd_urls()
    
    for cd in cd_urls:
        cd_id = cd['_id']
        link = cd['link']
        print link
        content = crawler.readlink(link)
        
        try:
            cd['douban_score']
            
            #print link
        
            try:
                douban_score = content.find('strong',attrs={'class':'ll rating_num'}).text
            except AttributeError:
                douban_score = 'unkonwn'

            try:    
                people_voted = content.find('span',attrs={'property':'v:votes'}).text
            except AttributeError:
                people_voted = 'unknown'

            new_entities = {
                'douban_score': douban_score,
                'people_voted': people_voted
            }
        
            mongo.update(new_entities, cd_id)  
        except:
            print('already in the database')
        
  
    
def main():
    getAllPages()
    getMusic()
    getOfficialDetail()

if __name__ == "__main__":
    main()

