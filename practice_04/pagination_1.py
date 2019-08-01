import re


class Page:
    def __init__(self, num, content):
        self.num = num
        self.content = content


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


# def main():
txt = []
with open('advs1.txt', 'r') as f:
    txt = f.readlines()

if txt:
    book = Book()
    sentences = book.get_sentences(''.join(txt))

    num = 1
    for p in book.chunks_sentences(sentences, 3):
        page_content = ' '.join(p)
        page = Page(num, page_content)
        # print(page)
        book.add_page(page)
    book.current_page = book.pages[0]

# if __name__ == '__main__':
#     main()
