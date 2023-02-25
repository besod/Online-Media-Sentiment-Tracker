import requests
from bs4 import BeautifulSoup
from content import Content 
import sqlite3

'''The Scraper class is written to start from the home page of each site, locate internal
links, and parse the content from each internal link found:'''

class Scraper:
    def get_page(self, url):
        try:
            r = requests.get(url).text
        except requests.exceptions.RequestException:
            return None
        
        return BeautifulSoup(r, 'html.parser')
    
    def get_element(self, pageObj, selector):
        '''Function used to get a content string from a Beautiful Soup object and a selector. 
           Returns an empty string if no object is found for the given selector'''
        selected_elements = pageObj.select(selector)#select metod runs a CSS selector and return all the matching elements
    
        if selected_elements is not None and len(selected_elements) > 0:
            return '\n'.join([element.get_text() for element in selected_elements])
        # childObj = pageObj.select(selector)
        # if childObj is not None and len(childObj) > 0:
        #     return childObj[0].get_text()
            
        return ""
    
    def search(self, topic, site):
        """
        Searches a given website for a given topic/search word and records all pages found in the first page
        """
        soup = self.get_page(site.search_url + topic)
        
        if soup is not None:
            search_results = soup.select(site.result_listing)
            
            for result in search_results:
                url = result.select(site.result_url)[0].attrs["href"]
                # Check to see whether result url link a relative or an absolute URL
                
                if(site.absolute_url):
                    soup = self.get_page(url)
                else:
                    soup = self.get_page(site.url + url)
                if soup is None:
                    print("Something was wrong with that page or URL. Skipping!")
                    return
                            
                title = self.get_element(soup, site.title_tag)#selects the title element and extracts the text
                body=self.get_element(soup,site.body_tag)#selects the article element and extracts the full article
                
                if title != '' and body != '':                            
                    content = Content(topic, url, title)
                    content.print()
                    connection = sqlite3.connect("newsArticle.db")
                    cursor_scraper = connection.cursor()         
                
                    # Check if the article URL already exists in the database
                    cursor_scraper.execute("SELECT COUNT(*) FROM articles WHERE url=?", (url,))
                    result = cursor_scraper.fetchone()[0]
                    if result > 0:
                        print(f"\nArticle '{url}' already exists in the database.\n")
                        continue
                
                    # Insert the scraped data into the 'data' table
                    try:
                        cursor_scraper.execute("INSERT INTO articles (topic,title,url,body) VALUES ( ?, ?, ?, ?)",
                                    (topic, title, url,body))
                        connection.commit()
                        print(f"\nArticle with url '{url}' saved to the database.\n")
                        
                    except sqlite3.IntegrityError as e:
                        print(f"\nAn error occurred while saving '{title}': {e}")
                        connection.rollback()
                
                if title == None:
                    print(f'Title could not be found.')