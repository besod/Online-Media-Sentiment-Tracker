
### Online-Media-Sentiment-Tracker
Online media sentiment tracker is written in python to crawl websites.  

### Description
As we consume news online we get a glimpse of current events.But it's difficult to keep track of how much attention is devoted to different
events in the media. There are lots of articles in the media but how much is written about a specific subject? Online media sentiment tracker
answers this question using web scraping. 

#### Scraping Sites Through Search
* Most sites retrive a list of search results flr a particular topic by passing 
that topic as a string through a parameter in the URL.http://exam
ple.com?search=Topic, the first part of this URL can be saved as property of the class Website class object, 
and the topic is appended to it. 
* After searching, many sites present the resulting pages as an easily identifiable
list of links
* Each result link is either a relativ URL(e.g. /articles/page.html) or an absolute
URL(e.g. http://example.com/articles/page.html). Which ever the case is the URL is stored 
as property of the Website class object.

The script loops through all the topics in the search word/topics list and announces 
before it starts scraping for a topic: 

<img width="256" alt="image" src="https://user-images.githubusercontent.com/113350472/218481335-80c50202-54d6-4438-87a8-53a14c502619.png">

Then it loops through all of the sites in the sites list and scrapes earch particular
site for each particular topic. After successfully scraping information about a page,
it prints it in the terminal:

<img width="534" alt="image" src="https://user-images.githubusercontent.com/113350472/218328828-e7cbe4a3-7415-40e7-b67d-3d884f285b74.png">






### How to run the program
Before running the program install the modules as in the figure. 

<img width="297" alt="image" src="https://user-images.githubusercontent.com/113350472/218481107-57ee5099-71a7-431b-aed7-673d49e7cc8b.png">





