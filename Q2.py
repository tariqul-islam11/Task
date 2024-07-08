class Item:
    def __init__(self, title: str, author: str, year: int):
        self.title = title
        self.author = author
        self.year = year

    def get_info(self):
        return f"Item: (Title: {self.title}, Author: {self.author}, Year: {self.year})"

    def __str__(self):
        return (f"Title: {self.title}\n"
                f"Author: {self.author}\n"
                f"Year: {self.year}")

class Book(Item):
    def __init__(self,title: str, author: str, year: int, publisher: str, isbn: str):
        self.publisher = publisher
        self.isbn = isbn
        super().__init__(title, author, year)

    def get_info(self):
        return f"Book: (Title: {self.title}, Author: {self.author}, Year: {self.year}, Publisher: {self.publisher}, ISBN: {self.isbn})"

class DVD(Item):
    def __init__(self, title: str, author: str, year: int, duration: int, region_code: int):
        self.duration = duration
        self.region = region_code
        super().__init__(title, author, year)
    
    def get_info(self):
        return f"DVD: (Title: {self.title}, Author: {self.author}, Year: {self.year}, Duration: {self.duration}Hour, Region Code: {self.region})"
    
item = Item("Java", "Abid Hasan", 2020)
book_item = Book("Python", "Tarek Islam", 2024, "ABC", "123-45667")
dvd_item = DVD("Avengers", "Russo Brothers", 2011, 2, 1)
info = item.get_info()
print(item.get_info())
print(book_item.get_info())
print(dvd_item.get_info())