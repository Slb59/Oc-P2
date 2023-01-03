class Category:
    """ manage a collection of books """

    def __init__(self, name):
        self.name = name
        self.url = ''
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def __str__(self):
        return self.name + ': (' + str(len(self.books)) + ' books)'

    def __repr__(self):
        info = '\n'.join([
            f'name: {self.name}',
            f'page: {self.url}',
            f'books:'
        ])
        info += '\n' + '\n'.join([str(c) for c in self.books])
        return info


