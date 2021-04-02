from bs4 import BeautifulSoup
import urllib.request

''' этот скрейпер был создан СПЕЦИАЛЬНО для рильке на стихи.ру и больше нигде работать не будет даже если
помолиться '''


class PoemLinkGenerator(object):

    anchor_tags = []
    list_of_links = []


    def cook_soup(self, poet_link):
        html_page = urllib.request.urlopen(poet_link)
        self.soup = BeautifulSoup(html_page, "html.parser")

    def get_anchor_tags(self):
        for tag in self.soup.find_all('a', attrs={'class': 'poemlink'}):
            t = tag.text
            self.anchor_tags.append(t)

    def get_links(self):
        for link in self.soup.find_all('a'):
            poem_links = link.get('href')
            if poem_links and poem_links.startswith('/201'):
                poem_links = 'https://stihi.ru' + poem_links
                self.list_of_links.append(poem_links)
            else:
                pass
            ''' Вы можете подумать, что этот код не должен работать, если у стихотворения нет названия или оно 
            пронумеровано. Вы будете правы, он не должен работать. Не трогайте, пожалуйста, бессмысленный 
            else: pass, а то все сломается к чертям собачьим '''

    def create_dict(self):
        self.dictionary = dict(zip(self.anchor_tags, self.list_of_links))
        return self.dictionary
