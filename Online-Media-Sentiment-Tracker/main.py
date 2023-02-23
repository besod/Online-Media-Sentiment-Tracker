from scraper import Scraper
from website import Website
import sqlite3
from texttable import Texttable
from prettytable import PrettyTable
import sys
import time

def main():  
    '''categories and their respective list of topics to search for is saved in dictionary and nested lists during initial development.'''
    categories = {"poletics":['Election','corruption'],
                  "climate change":['Drought','Extreme temperature'],
                  "finance":['Inflation','Interest rate'],
                  "science":['Natural Resources']
                  }
    print(f'\nWELCOME TO THE GREATEST WEB SCRAPER IN THE WORLD.\n') 
    
    '''This block of code creates connection to a database. Create table to store scraped articles.
    Create table for categories and search words.'''
    connection = sqlite3.connect("newsArticle.db")
    #create cursor objec for articles table to store scraped articles
    cursor_scraper = connection.cursor()   
    article=("""CREATE TABLE IF NOT EXISTS articles(id INTEGER PRIMARY KEY AUTOINCREMENT,
            topic text,
            title text,
            url text,
            body text,
            timestamp DATE DEFAULT (datetime('now','localtime')))""")
    cursor_scraper.execute(article)
    connection.commit
    # Create a connection to the database
    
    # Create a cursor object for search words
    cursor_search_words = connection.cursor()
    # Check if the search_words table exists
    cursor_search_words.execute('''SELECT count(name) FROM sqlite_master WHERE type='table' AND name='search_words' ''')
    if cursor_search_words.fetchone()[0] == 1:
        print('Search_words table found.')
    else:
       # Create the search_words table if not exists
        cursor_search_words.execute('''CREATE TABLE IF NOT EXISTS search_words (category TEXT PRIMARY KEY, topic TEXT, created_date TEXT DEFAULT CURRENT_TIMESTAMP)''')
        #Insert the data from the categories dictionary
        for category, topics in categories.items():
            topic_str = ', '.join(topics) # Join the topic words separated with a comma
            cursor_search_words.execute('''SELECT count(*) FROM search_words WHERE category=? AND topic=?''', (category, topic_str))
            if cursor_search_words.fetchone()[0] == 0:
                cursor_search_words.execute("INSERT INTO search_words(category,topic) VALUES (?, ?)", (category, topic_str))
        print(f"Search_words table created!")
       
        # Commit the changes and close the connection
        connection.commit()
    #connection.close()
    
    '''List of websites to scrape stored in a list. HTML and CSS elements are saved in order(see class 'Website').This can eventually be saved in a database.'''
    site_data = [
                ['Reuters','http://reuters.com','http://www.reuters.com/search/news?blob=','div.search-result-content','h3.search-result-title a',False, 'h1','div.article-body__content__17Yit '],
                ['apnews','https://apnews.com','https://apnews.com/hub/trending-news','ul li','a',False,'h1','article'],
                ['Brookings','https://brookings.edu','https://www.brookings.edu/search/?s=','div.article-info','h4 a',True,'h1','div.post-body'],  
                ['The economist','https://www.economist.com','https://www.economist.com/search?q=','li._result-item','a',True,'h1','div.css-13gy2f5'],
                ['forbes','https://www.forbes.com','https://www.forbes.com/search/?q=','div.search-results h3','a',True,'h1','div.article-body']
                ]
   
    scraper = Scraper()
    #main loop that prompts user for input 
    while True:        
        sites = []
        for row in site_data:
            sites.append(Website(row[0], row[1], row[2],row[3], row[4], row[5], row[6], row[7]))
            
        print('''Choose from the menu:>
                 [0] - Quit
                 [1] - Scrape
                 [2] - Add/Remove category
                 [3] - Add/Remove search word''')
        
        user_choice = input(':-> ')
        if user_choice == '0':
            print(f"\nGOOD BYE!")
            break
        
        elif user_choice == '1':
            '''Displays the category and their respective search word/topic in a table format.Loops that iterates
            through all the topics and all the websites after receiving category from the user.
            It contains a search function that navigates to the search page for a particular website and topic,
            and extracts all the result URLs listed on that page.'''    
            while True:
                # fetch the contents of the search_words table and display it in table form using prettytable
                cursor_search_words.execute("SELECT * from search_words")
                result = cursor_search_words.fetchall()
                # create a prettytable object with the column names
                table = PrettyTable(['Category', 'Topic','Created'])
                # add each row to the table
                for row in result:
                    table.add_row(row)                
                table.align["Category"] = "l"
                table.align["Topic"] = "l" 
                table.align["Created"] = "l"
                print(table)
                
                #prompt the user to enter category from the table 
                category_choice = input("Enter a category (Press 'b' anytime to go back to the main menu): \n")
                if category_choice == 'b':
                    break
                
                #try/except block checks if the user enters category that exists in the list provided
                try:
                    cursor_search_words.execute("SELECT topic FROM search_words WHERE category=?",(category_choice,))
                    topics_str = cursor_search_words.fetchone()[0]
                    topics = topics_str.split(', ')
                    print(topics)
                              
                    for topic in topics:
                        print(f'GETTING INFO ABOUT CATEGORY "{category_choice}" AND SEARCH WORDS ARE {topics}: ')
                        for target_site in sites:
                            scraper.search(topic, target_site)                      
                    print('Check your database!\n')
                except TypeError:
                    print('\nERROR! CATEGORY NOT FOUND...\n')       
            
            '''Propts user to add new category and corresponding search word/topic'''   
        elif user_choice == '2':#add/remove category in/from search_words table in the database
                             
           # Prompt the user to choose an action
            action = input("Enter 'add' to add a category or 'remove' to remove a category: ").casefold()

            if action == 'add':
                # Prompt the user to enter a new category and topics
                category = input("Enter a new category: ").casefold()          
                
                # Check if the category already exists in the database
                cursor_search_words.execute("SELECT COUNT(*) FROM search_words WHERE category=?", (category,))
                # If the category does not exist, insert the data into the database
                if cursor_search_words.fetchone()[0] == 0:
                    topics = input("Enter topic words separated by commas: ")                    
                    cursor_search_words.execute("INSERT INTO search_words (category, topic) VALUES (?, ?)", (category, topics))
                    print("Data inserted successfully.")
                else:
                    # If the category already exists, print an error message
                    print("Error: Category already exists in the database.")
            elif action == 'remove':
                # Prompt the user to enter the category to be removed
                category = input("Enter the category to be removed: ").casefold()
                
                # Check if the category exists in the database
                cursor_search_words.execute("SELECT COUNT(*) FROM search_words WHERE category=?", (category,))
                if cursor_search_words.fetchone()[0] == 1:
                    # If the category exists, remove it from the database
                    cursor_search_words.execute("DELETE FROM search_words WHERE category=?", (category,))
                    print("Category removed successfully.")
                else:
                    # If the category does not exist, print an error message
                    print("Error: Category does not exist in the database.")
   
            else:
                print("Invalid action. Please enter 'add', 'remove'.")
            

            connection.commit()
               
        elif user_choice == '3':
            '''This block of code updates database search words.The program continously prompts the user to 
            enter catagory to be updated.'Add' replaces the old search words with new ones given by the user.
            'Remove' replaces the search words with null value.'''
            
            # Prompt the user to enter the category to be updated
            while True:                                         
                category = input("Enter the category to be updated (Press 'b' to go back to main menu): ").casefold()
                if category == 'b':
                    break
                
                # Check if the category already exists in the database
                cursor_search_words.execute("SELECT COUNT(*) FROM search_words WHERE category=?", (category,))
                if cursor_search_words.fetchone()[0] == 1:                    
                    
                    while True:
                        # If the category exists, prompt user for action
                        action = input("\nEnter 'add' to add search word or 'remove' to remove search word (Press 'b' to exit): ").casefold()
                        if action == 'b':
                            break
                    
                        if action == 'add':                  
                            while True:
                                topics = input("Enter topic words separated by commas: ")
                                if topics=='':
                                    print('ERROR! EMPTY ENTRY NOT ALLOWED.')
                                else:
                                    cursor_search_words.execute("UPDATE search_words SET topic=? WHERE category=?",(topics,category))   
                                    connection.commit()
                                    print("Data inserted successfully.")
                                    break
                        elif action == 'remove':                    
                            # Update the search words for the corresponding category
                            query=('''UPDATE search_words SET topic=NULL WHERE category=?''')
                            cursor_search_words.execute(query,(category,))
                            connection.commit()
                            print("Search word removed successfully.")
                            break
                        else:
                            #If user input is not 'add' or 'remove'
                            print('ERROR! YOU HAVE GONE OFF SCRIPT... ')
                            continue
                else:
                    # If the category does not exist, print an error message
                    print("Error: Category does not exist in the database.")
                    continue
        else:
            msg=" Ooops...! You\'ve gone off script. We love to improve, but let's take it from the top and try again.\n"
            print('\n',msg.upper())
            continue                    

       
if __name__ == '__main__':
    main()   
