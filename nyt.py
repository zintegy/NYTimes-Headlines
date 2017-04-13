from nytimesarticle import articleAPI

api = articleAPI('007d1598452c4a18b7950b9a51119d3f')


articles = api.search(begin_date=19800102, end_date=19800103)
articles1 = api.search(begin_date=19800103, end_date=19800104)


