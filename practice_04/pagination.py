class Page:
	pass

	
class Book:
	def __init__(self):
		self.pages = []
		self.bookmarks = {}
		
	def add_page(self, page):
		self.pages.append(page)
		
	
	
with open('advn.txt', 'r') as book_file:
	
	txt_list = book_file.readlines()
	
	cymbols = [".", "!", "?", "...", "???", "!!!"]
	