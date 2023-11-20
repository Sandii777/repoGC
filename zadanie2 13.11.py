# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 14:15:42 2023

@author: student
"""

class Library:
    def __init__(self,city, street, zip_code, open_hours: str, phone):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone
        
    def __str__(self):
        return f"Library: {self.city}, {self.street}, {self.zip_code}\nOpen hours: {self.open_hours}\nPhone: {self.phone}"
        
class Employee:
    def __init__(self, first_name, last_name, hire_date, birth_date, city, street, zip_code, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone
        
    def __str__(self):
        return f"Employee: {self.first_name} {self.last_name}\nHire Date: {self.hire_date}\nBirth Date: {self.birth_date}\nLocation: {self.city}, {self.street}, {self.zip_code}\nPhone: {self.phone}"

        
class Book:
    def __init__(self, library, publication_date, author_name, author_surname, number_of_pages):
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages
        
        
    def __str__(self):
        return f"Book: {self.author_name} {self.author_surname}\nPublication Date: {self.publication_date}\nNumber of Pages: {self.number_of_pages}\n{self.library}"

                
        
class Order:
    def __init__(self, employee, student, books, order_date):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date
        
        
    def __str__(self):
        book_list = "\n".join([f"\t- {book}" for book in self.books])
        return f"Order Date: {self.order_date}\n{self.employee}\n{self.student}\nBooks:\n{book_list}"
        


biblio1 = Library("City1", "Street1", "12345", "9:00 - 17:00M", "123-456-789")
biblio2 = Library("City2", "Street2", "54321", "10:00 - 18:00 ", "987-654-321")

pracownik1 = Employee("Anna", "Nowak", "2022-01-01", "1990-01-01", "City1", "Street1", "12345", "555-1234")
pracownik2 = Employee("Brajan", "Kowalski", "2022-02-01", "1995-02-15", "City2", "Street2", "54321", "555-5678")
pracownik3 = Employee("Andrzej", "Rybak", "2022-03-01", "1985-03-20", "City1", "Street1", "12345", "555-9876")

książka1 = Book(biblio1, "2021-01-01", "Author1", "Surname1", 200)
książka2 = Book(biblio1, "2021-02-01", "Author2", "Surname2", 250)
książka3 = Book(biblio2, "2021-03-01", "Author3", "Surname3", 300)
książka4 = Book(biblio2, "2021-04-01", "Author4", "Surname4", 180)
książka5 = Book(biblio2, "2021-05-01", "Author5", "Surname5", 220)

zam1 = Order(pracownik1, "Student1", [książka1, książka2, książka3], "2022-04-01")
zam2 = Order(pracownik2, "Student2", [książka4, książka5], "2022-05-01")


print(zam1,"\n-----------------\n",zam2)










        
        
