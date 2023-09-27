from bs4 import BeautifulSoup
import requests
import json

def get_news():
    
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/117.0'
    }

    url = 'https://stopgame.ru/news'
    req = requests.get(url=url, headers=headers)
    soup = BeautifulSoup(req.text, "lxml")
    
    
    articles_card = soup.find_all('a', class_="_title_1tbpr_49")
   # print(articles_card)
    
    
    news_dict = {} #создаем слловарь
    for article in articles_card:
        article_title = article.text
        article_href = f'https://stopgame.ru{article.get("href")}'
        
        #достанем ID новости
        article_id = article_href.split("/")[-2]

        
        news_dict[article_id] = {
            'article_title': article_title,
            'article_href': article_href
        }
        
    with open('news_dict.json', 'w', encoding='utf-8')as file:
        json.dump(news_dict, file, indent=4, ensure_ascii=False)
        
        

def check_news():
    with open('news_dict.json', encoding='utf-8') as file: 
        news_dict = json.load(file)
    
        
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/117.0'
    }
    
    url = 'https://stopgame.ru/news'
    req = requests.get(url=url, headers=headers)
    soup = BeautifulSoup(req.text, "lxml")
    
    articles_card = soup.find_all('a', class_="_title_1tbpr_49")

    fresh_news = {}
    for article in articles_card:
         article_href = f'https://stopgame.ru{article.get("href")}'
         article_id = article_href.split("/")[-2]
         
         
         if article_id in news_dict:
             continue
         else:
            article_title = article.text
            
         news_dict[article_id] = {
            'article_title': article_title,
            'article_href': article_href
            }
         
         fresh_news[article_id] = {
            'article_title': article_title,
            'article_href': article_href
         }
         
         
    with open("news_dict.json", "w", encoding="utf-8") as file:
        json.dump(news_dict, file, indent=4, ensure_ascii=False)
        
    return fresh_news
        
        

def main():
    get_news()
    #check_news()
    
if __name__ == '__main__':
    main()

