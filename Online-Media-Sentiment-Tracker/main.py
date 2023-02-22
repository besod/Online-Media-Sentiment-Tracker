from scraper import Scraper
from website import Website
from texttable import Texttable
import sys
import time

def main():             
    scraper = Scraper()

    '''categories and their respective list of topics to search for is saved in dictionary and nested lists'''
    categories = {"poletics":['Election','corruption'],
                  "climate change":['Drought','Extreme temperature'],
                  "finance":['Inflation','Interest rate'],
                  "science":['Natural Resources']
                  }

    '''List of websites to scrape. HTML and CSS elements are saved in order(see class 'website')'''
    site_data = [
                ['The economist','https://www.economist.com','https://www.economist.com/search?q=','li._result-item','a',True,'h1'],
                ['forbes','https://www.forbes.com','https://www.forbes.com/search/?q=','div.search-results h3','a',True,'h1'],
                ['Brookings','https://brookings.edu','https://www.brookings.edu/search/?s=','div.article-info','h4 a',True,'h1'],        
                ['Reuters','http://reuters.com','http://www.reuters.com/search/news?blob=','div.search-result-content','h3.search-result-title a',False, 'h1'],
                # #['apnews','https://apnews.com','https://apnews.com/hub/trending-news','li','div a',False,'h1']
                 ]

    print(f'\nWELCOME TO THE GREATEST WEB SCRAPER IN THE WORLD.\n') 
    #main loop that prompts user for input 
    while True:        
        sites = []
        for row in site_data:
            sites.append(Website(row[0], row[1], row[2],row[3], row[4], row[5], row[6]))

        #new dictionary of category and respective list of topic created    
        category = categories
        print('''Choose from the menu:>
                 [0] - Quit
                 [1] - Scrape
                 [2] - Add category
                 [3] - Add search word''')
        
        user_choice = input(':-> ').upper()
        if user_choice == '0':
            break
        elif user_choice == '1':
            '''displays the category and their respective search word/topic in a table format'''
            print(f"Type a category from the table (press 'b' anytime to go back to the main menu) ")
            table_data=[['Category','Topic/Search word']] + [[key.upper(),',' .join(value)] for key,value in category.items()] 
            table_obj=Texttable()
            table_obj.set_cols_align(["l", "l"])
            table_obj.add_rows(table_data)
            print(table_obj.draw())
            
            user_input=input(':-> ')
            if user_input == 'b':
                sys.exit

            '''loops that iterate through all the topics and all the websites after receiving category from the user.
            It also contains a search function that navigates to the search page for a particular website and topic,
            and extracts all the result URLs listed on that page.'''    
            for choice_category,search_word in category.items():
                if user_input == choice_category or user_input in choice_category:                    
                    for topic in search_word:
                        print(f'GETTING INFO ABOUT {topic}')
                        for target_site in sites:
                            scraper.search(topic, target_site)                         
                    print('Completed! Check your database!')

                    #sets time to 24 hrs for next web scraping
                    print(f'Time to wait {24} hrs...')
                    print(f" Press ctrl + c if you wish to disrupt!")
                    time.sleep(24*60*60)
            
            '''Propts user to add new category and corresponding search word/topic'''   
        elif user_choice == '2':         
            new_category = input("Enter the name of the new category: ")
            new_list = []
            while True:
                new_word = input("Enter a search word for the new category (or type 'stop' to stop): ")
                if new_word == 'stop':
                    break
                new_list.append(new_word)
                category[new_category] = new_list

            '''prompts user to add search word/topic in a chosen category.'''   
        elif user_choice == '3':
            key = input("Enter the category: ")
            if key in category:
                while True:
                    new_word = input("Enter new search word/topic (or type 'stop' to stop: ")
                    if new_word == 'stop':
                        break
                    category[key].append(new_word)
            else:
                print("Category not found in table.")
        else:
            msg=" Ooops...! You\'ve gone off script. We love to improve, but let's take it from the top and try again.\n"
            print('\n',msg.upper())
            continue                    

       
if __name__ == '__main__':
    main()   
