class Website:
    """Contains information about website structure.Website information in 'site_data' is saved in such structure."""
    def __init__(self, name, url, search_url, result_listing,
        result_url, absolute_url, title_tag):
        self.name = name #name of the website
        self.url = url   # absolut url
        self.search_url = search_url #defines where to go to get search results if topic is appended
        self.result_listing = result_listing #defins the box what holds information about each result
        self.result_url = result_url # defines the tag inside the result_listing box that gives the exact URL for the result
        self.absolute_url=absolute_url #boolean property to tell if result link is absolut or relativ
        self.title_tag = title_tag #title of the articles searched 