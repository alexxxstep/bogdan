import re


class Page:
    pass


class Book:
    def __init__(self):
        self.pages = []
        self.bookmarks = {}
        self._current_page = None

	def add_page(self, page):

    # def srtip_sent(self, text):
    # 	split_regex = re.compile(r'[.|!|?|…|???|!]')
    # 	sentences = filter(lambda t: t, [t.strip() for t in split_regex.split(text)])
    # 	return sentences

    def create_page(self, str_list, n):
        iterator = iter(str_list)
        while n > 0:
            yield next(iterator)
            n -= 1


def main():
    with open('advs.txt', 'r') as f:
        txt = f.readlines()

        if txt:
            book = Book()
            sentenses_lst = book.srtip_sent(txt)

            print(sentenses_lst)


if __name__ == '__main__':
    main()
