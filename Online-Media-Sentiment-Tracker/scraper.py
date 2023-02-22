import requests
from bs4 import BeautifulSoup
from connect import Connect
from content import Content 

'''The Scraper class is written to start from the home page of each site, locate internal
links, and parse the content from each internal link found:'''
class Scraper:
    def get_page(self, url):
        try:
            r = requests.get(url).text
        except requests.exceptions.RequestException:
            return None        
        return BeautifulSoup(r, 'html.parser')
    
    def get_element(self, page_obj, selector):
        '''Function used to get a content string from a Beautiful Soup object and a selector. 
           Returns an empty string if no object is found for the given selector'''
        selected_elements = page_obj.select(selector)#select metod runs a CSS selector and return all the matching elements
        if selected_elements is not None and len(selected_elements) > 0:
            return '\n'.join([element.get_text() for element in selected_elements])
                    
        return ""
    
    def search(self, topic, site):
        '''Searches a given website for a given topic/search word and records all sites found in the first page'''
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
                if title != ' ' :                            
                    content = Content(topic, url, title)
                    connection=Connect(topic,url,title)
                    content.print()#print selected result
                    connection.save_to_db()#store in sqlite
                if title == None:
                    print(f'Title could not be found.')