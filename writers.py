import datetime

from abc import abstractmethod, ABC

class Writers:
    def __init__(self, name: str, surname: str, pen_name: str,
                 birth_date: datetime.date, death_date: datetime.date, country: str, works_list: list):
        self.name = name
        self.surname = surname
        self.pen_name = pen_name
        self.birth_date = birth_date
        self.death_date = death_date
        self.country = country
        self.works_list = works_list

new_work = input()

def authors_list(self):
    lauthors = [self.name, self.surname, self.pen_name, self.birth_date, self.death_date, self.country, self.works_list]
    return lauthors

def add_work(self):
    self.works_list.append(new_work)

class Publishing_house:
    def __init__(self, title: str, address: str ):
        self.title = title
        self.address = address

def publishing(self):
    a = [self.title, self.adress]
    return a

number_of_authors = int(input())

all_authors = []

for i in range(number_of_authors):
    all_authors.append(authors_list())

class Works:
    def __init__(self, year: int):
        self.authors = all_authors
        self.publish = publishing()
        self.year = year

def add_author(self):
    self.authors.append(authors_list())

class Book(Works):
    def __init__(self, binding, cover, year: int):
        super().__init__(year)
        self.binding = binding
        self.cover = cover

class Magazine(Works):
    def __init__(self, cover_type, year: int):
        super().__init__(year)
        self.cover_type = cover_type

class Publication(Works):
    def __init__(self, place_of_publication, year: int):
        super().__init__(year)
        self.place = place_of_publication
