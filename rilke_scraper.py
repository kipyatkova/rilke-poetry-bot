from bs4 import BeautifulSoup
from urllib.request import urlopen
from link_generator import *

rilkegen = PoemLinkGenerator()


class Scraper(object):

    def set_dictionary(self):
        while True:
            user_dictionary = input('Выберите номер сборника: \n1. Произведения, не вошедние в сборники \n2. Валезианские '
                                    'катрены \n3. Сады \n4. Жизнь девы Марии \n5. О бедности и смерти - 3 книга \n'
                                    '6. Об иноческой жизни - 2 книга \n7. Об иноческой жизни - 1 книга.\n')
            if user_dictionary == '1':
                rilkegen.cook_soup('https://stihi.ru/avtor/rylkeriner')
                rilkegen.get_anchor_tags()
                rilkegen.get_links()
                rilkegen.create_dict()
                return rilkegen.dictionary
            elif user_dictionary == '2':
                rilkegen.cook_soup('https://stihi.ru/avtor/rylkeriner&book=7#7')
                rilkegen.get_anchor_tags()
                rilkegen.get_links()
                rilkegen.create_dict()
                return rilkegen.dictionary
            elif user_dictionary == '3':
                rilkegen.cook_soup('https://stihi.ru/avtor/rylkeriner&book=6#6')
                rilkegen.get_anchor_tags()
                rilkegen.get_links()
                rilkegen.create_dict()
                return rilkegen.dictionary
            elif user_dictionary == '4':
                rilkegen.cook_soup('https://stihi.ru/avtor/rylkeriner&book=5#5')
                rilkegen.get_anchor_tags()
                rilkegen.get_links()
                rilkegen.create_dict()
                return rilkegen.dictionary
            elif user_dictionary == '5':
                rilkegen.cook_soup('https://stihi.ru/avtor/rylkeriner&book=4#4')
                rilkegen.get_anchor_tags()
                rilkegen.get_links()
                rilkegen.create_dict()
                return rilkegen.dictionary
            elif user_dictionary == '6':
                rilkegen.cook_soup('https://stihi.ru/avtor/rylkeriner&book=3#3')
                rilkegen.get_anchor_tags()
                rilkegen.get_links()
                rilkegen.create_dict()
                return rilkegen.dictionary
            elif user_dictionary == '7':
                rilkegen.cook_soup('https://stihi.ru/avtor/rylkeriner&book=2#2')
                rilkegen.get_anchor_tags()
                rilkegen.get_links()
                rilkegen.create_dict()
                return rilkegen.dictionary
            else:
                print('Неправильное название сборника.')

    def set_poem(self):
        while True:
            print('Список стихотворений:')
            for key, value in rilkegen.dictionary.items():
                print(key, ':', value)
            self.poem_name = input(f'Какое стихотворение выбрать? ')
            if self.poem_name in rilkegen.dictionary.keys():
                self.poem_url = rilkegen.dictionary.get(self.poem_name)
                break
            else:
                print('Такого стихотворения нет.')

    def get_text(self):
        url = self.poem_url
        page = urlopen(url)
        soup = BeautifulSoup(page, "html.parser")
        full_page_text = soup.get_text()
        rilke_found = full_page_text.rfind(f'{self.poem_name}\nРайнер Рильке')
        copyright_found = full_page_text.rfind('© Copyright')
        poem_text = full_page_text[rilke_found:copyright_found]
        self.poem_text = poem_text
        
        # Write everything in a text file
        w_file = open("poem_data.txt", "w")
        w_file.write(self.poem_text)
        w_file.close()


if __name__ == '__main__':
    print('scraper initiated')
    scraper = Scraper()
    scraper.set_dictionary()
    scraper.set_poem()
    scraper.get_text()
    print(scraper.poem_text)
