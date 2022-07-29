
class Links:
    def __init__(self, url):
        self._url = url

    def _get_page(self):
        pass

    def _get_links(self):
        self._links = []  # list of links

    @property
    def links(self):
        return self._links

    @property
    def url(self):
        return self._url

l1 = Links('https://www.python.org')

for link in l1.links:
    print(link)

print(l1.url)

