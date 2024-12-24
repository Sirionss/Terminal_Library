#   Task: Create classes for Library, Book, and Member.
#The Library should manage books (add, remove) and
#track which members have borrowed which books.
#   Goal: Combine several concepts like:
#relationships, encapsulation, and basic CRUD operations in an object-oriented context.

class Library:
    def __init__(self):
        self.books = []
        self.members = []
    def add_book(self, book):
        self.books.append(book)
    def remove_book(self, title):
        self.books = [book for book in self.books if book.title.upper != title.upper]
    def add_member(self, member):
        self.members.append(member)
    def print_book_list(self):
        for book in self.books:
            print(book.title,book.author,book.rn_owner)
    def print_member_list(self):
        for member in self.members:
            print(member.Full_Name)
            print('Books taken:')
            for book in member.books_taken:
                print(book.title,book.author)
    def borrow_book(self,Full_Name,title):      #maybe also add date of taking the book or last interaction
        borrowed_book = [book for book in self.books if book.title.upper == title.upper][0]
        member = [member for member in self.members if member.Full_Name.upper == Full_Name.upper][0]
        self.books.remove(borrowed_book)
        borrowed_book.rn_owner = member.Full_Name
        self.books.append(borrowed_book)
        member.books_taken.append(borrowed_book)
    def return_book(self,Full_Name,title):
        member = [member for member in self.members if member.Full_Name.upper == Full_Name.upper][0]
        returned_book = [book for book in member.books_taken if book.title.upper == title.upper][0]
        member.books_taken.remove(returned_book)
        self.books.remove(returned_book)
        returned_book.rn_owner = 'Library'
        self.books.append(returned_book)
class Book:
    def __init__(self,title,author,rn_owner):
        self.title = title
        self.author = author
        self.rn_owner = rn_owner
class Member:
    def __init__(self, Full_Name, library_name):
        self.Full_Name = Full_Name
        self.books_taken = []

library = Library()
library.add_member(Member('Sasha Andromedow',library))
library.add_member(Member('Masha Andromedowa',library))
library.add_book(Book('123','111111','Library'))
library.add_book(Book('321','222222','Library'))
library.print_book_list()
library.print_member_list()
library.borrow_book('Sasha Andromedow','123')
library.print_book_list()
library.print_member_list()
library.return_book('Sasha Andromedow','123')
library.print_book_list()
library.print_member_list()
library.remove_book('123')
library.print_book_list()
library.print_member_list()

