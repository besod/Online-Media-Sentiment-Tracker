
### Online-Media-Sentiment-Tracker
Online media sentiment tracker is written in python to crawl websites. The program scrapes news websites using search words from a database. Category and search words list is already created in sqlite.User can update categories and search words in the table. The scraped title, url and article of website is then printed in the terminal. It also saves the scraped articles in sqlite database.   


**Description:**  
As we consume news online, we get a glimpse of current events. However, it can be difficult to keep track of how much attention is devoted to different events in the media. With numerous articles published daily, quantifying the coverage of specific subjects becomes challenging. The Online Media Sentiment Tracker addresses this issue by using web scraping to monitor and analyze the sentiment of online media coverage.

**Technologies Used:**  
- **Python** 🐍: For overall application development and scripting.
- **SQLite3** 🗄️: For efficient and lightweight database management.
- **Jupyter Notebook** 📓: For interactive data analysis and visualization.
- **Pandas** 🐼: For data manipulation and analysis.
- **NLTK** 🧠: For natural language processing and sentiment analysis.

**Key Features:**  
- **Web Scraping:** Automated extraction of news articles from various online sources.
- **Sentiment Analysis:** Utilizing NLTK for sentiment analysis, the system evaluates the emotional tone of news articles, categorizing them as positive, negative, or neutral.
- **Machine Learning:** The sentiment analysis component employs machine learning algorithms to train and classify text data, enhancing accuracy over time.
- **Data Storage:** Efficient storage and retrieval of articles and sentiment data using SQLite3, ensuring scalability and performance.
- **Data Visualization:** Interactive analysis and visualization of media coverage trends using Jupyter Notebook and Pandas, allowing users to explore sentiment patterns and correlations.
- **Automation:** The project automates the process of collecting and analyzing news articles, reducing manual effort and enabling real-time monitoring of media sentiment.


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

   





