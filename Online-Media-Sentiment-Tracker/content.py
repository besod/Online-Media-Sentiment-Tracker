class Content:
    """Common base class for all pages. This class is responsible for creating instances of url,title,topic,date
    and prints the results."""
    
    def __init__(self, topic, url, title):
        self.topic = topic
        self.title = title 
        self.url = url
           
    def print(self):
        ''''Print function controls output and prints the results if needed.'''
        print("New article found for topic: {}".format(self.topic))
        print("TITLE: {}".format(self.title))
        print("URL: {}".format(self.url))