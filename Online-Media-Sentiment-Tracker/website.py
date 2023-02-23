class Website:
    """Contains information about website structure."""
    def __init__(self, name, url, search_url, result_listing,
    result_url, absolute_url, title_tag,body_tag):
        self.name = name #name of the website
        self.url = url   # absolut url
        self.search_url = search_url #defines where to go to get search results if topic is appended
        self.result_listing = result_listing #defins the tag inside the resultListing box to get exact URL
        self.result_url = result_url # defines the box that holds information about each result
        self.absolute_url=absolute_url #boolean property to tell if result link is absolut or relativ
        self.title_tag = title_tag #title of the articles searched 
        self.body_tag = body_tag