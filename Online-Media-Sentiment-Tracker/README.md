
### Online-Media-Sentiment-Tracker
Online media sentiment tracker is written in python to crawl websites. The program scrapes news websites using search words from a database. Category and search words list is already created in sqlite.User can update categories and search words in the table. The scraped title, url and article of website is then printed in the terminal. It also saves the scraped articles in sqlite database.   

### Description
As we consume news online we get a glimpse of current events.But it's difficult to keep track of how much attention is devoted to different
events in the media. There are lots of articles in the media but how much is written about a specific subject? Online media sentiment tracker
answers this question using web scraping. 

#### Scraping Sites Through Search
* Most sites retrive a list of search results for a particular topic by passing 
that topic as a string through a parameter in the URL.http://exam
ple.com?search=Topic, the first part of this URL can be saved as property of the class Website class object, 
and the topic is appended to it. 
* After searching, many sites present the resulting pages as an easily identifiable
list of links
* Each result link is either a relativ URL(e.g. /articles/page.html) or an absolute
URL(e.g. http://example.com/articles/page.html). Which ever the case is the URL is stored 
as property of the Website class object.

* The script loops through all the topics in the search word/topics list and announces 
before it starts scraping for a topic: 

   ![image](https://user-images.githubusercontent.com/113350472/221377352-522d370b-38e4-4bdc-85df-c33d97d3dd2b.png)

* Then it loops through all of the sites in the sites list and scrapes earch particular
site for each particular topic. After successfully scraping information about a page,
it prints it in the terminal:

   ![image](https://user-images.githubusercontent.com/113350472/221377305-ee34bf9c-13b4-4197-a21b-c65d99e1f9df.png)



* Sentiment alanlysis is made using NLTK.
* Visualization of data is made with pandas in jupyter notebook.

### How to run the program
Before running the program install the modules: 
``` 
$ pip install beautifulsoup4
``` 
``` 
$ pip install requests
``` 
``` 
$ pip install prettytable
``` 

   





