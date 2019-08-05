import re


class Page:
    def __init__(self, num, content):
        self.num = num
        self.content = content


class Bookmark:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name_):
        self._name = name_


class Book:
    def __init__(self):
        self.pages = []
        self.bookmarks = {}
        self._current_page = None

    @property
    def current_page(self):
        return self._current_page

    @current_page.setter
    def current_page(self, page):
        self._current_page = page

    def add_page(self, page):
        self.pages.append(page)

    def get_numbs_pages(self):
        '''Вернуть общее количество страниц;'''
        try:
            return len(self.pages)
        except:
            return None

    def get_numb_current_page(self):
        '''узнать  текущийномер страницы;'''
        try:
            return self.current_page.num
        except:
            return None

    def get_page_by_numb(self, numb):
        '''узнать страницу по намеру'''
        try:
            return self.pages[numb - 1]
        except:
            return None

    def move_forward(self, n=1):
        '''перейти на N страницу вперед;'''
        numb_cp = self.get_numb_current_page()

        try:
            c_page = self.pages[numb_cp - 1 + n]
            self.current_page = c_page
        except:
            print('uncorrect move!')

    def move_backward(self, n=1):
        '''перейти на N страницу назад;'''
        numb_cp = self.get_numb_current_page()

        try:
            c_page = self.pages[numb_cp - 1 - n]
            self.current_page = c_page
        except:
            print('uncorrect move!')

    def move_to_first(self):
        '''Перейти на первую страницу'''

        try:
            c_page = self.pages[0]
            self.current_page = c_page
        except:
            print('uncorrect move!')

    def move_to_last(self):
        '''Перейти на последнюю страницу'''
        try:
            c_page = self.pages[-1]
            self.current_page = c_page
        except:
            print('uncorrect move!')

    def create_bookmark(self, name_b):
        keys_names = self.get_list_bookmarks()
        if name_b in keys_names:
            print(f'*error. this name is already exist!')
            return None
        bookmark = Bookmark(name_b)
        return bookmark

    def establish_bookmark(self, name_b, numb_page=0):
        """	Установить закладку с конкретным именем для текущей странcицы,
	        обычно имена закладок должны быть уникальны и метод должен проверять
	        наличие закладки с определенным именем, прежде чем создать новую;
            Установить закладку с именем для конкретной страницы по ее номеру, помним про уникальность имени"""

        bookmark = self.create_bookmark(name_b)
        if bookmark:
            if numb_page > 0:
                page = self.get_page_by_numb(numb_page)
                if page:
                    self.bookmarks[bookmark] = page
            else:
                self.bookmarks[bookmark] = self.current_page

    def get_list_bookmarks(self):
        """Вернуть список существующих закладок;"""
        keys_names = [i.name for i in self.bookmarks.keys()]
        return keys_names

    def move_by_bookmarkname(self, name_b):
        """	Перейти на страницу по имени закладки;"""

        for key, item in self.bookmarks.items():
            if key.name == name_b:
                self.current_page = item
                return True
        else:
            return False

    def get_numbs_by_context(self, f_content):
        """Метод поиска по контексту, который вернет список номеров страниц, где будет обнаружен указанный контекст"""
        numbs_p = []
        for p in self.pages:
            if p.content.count(f_content) > 0:
                numbs_p.append(p.num)
        return numbs_p

    def get_content_current_page(self):
        """	Вернуть текст текущей страницы."""
        return self.current_page.content


class ManagerPagination:

    def __init__(self):
        self.books = []

    def create_book_from_file(self, file_, nums_sent_on_page=3):

        txt = self.get_txt_from_file(file_)

        book = Book()
        sentences = self.get_sentences(txt)

        num_page = 1
        for p in self.chunks_sentences(sentences, nums_sent_on_page):
            page_content = ' '.join(p)
            page = Page(num_page, page_content)
            book.add_page(page)
            book.current_page = book.pages[0]
            num_page += 1

        self.books.append(book)

        return book

    def get_txt_from_file(self, file_):
        txt = []
        with open(file_, 'r') as f:
            txt = f.readlines()

        return ''.join(txt)

    def get_sentences(self, text):
        sentences = []

        pattern = re.compile(r'([А-ЯA-Z]((Mr.|Mrs.|th.|K.|St.)|[^?!.\(]|\([^\)]*\))*[.?!])')

        for i, sent in enumerate(pattern.findall(text)):
            sentences.append(f'{sent[0]}')
        return sentences

    def chunks_sentences(self, lst, count):
        start = 0
        left = len(lst)
        while left > 0:
            stop = start + min(count, left)
            yield lst[start:stop]
            start = stop
            left -= count


