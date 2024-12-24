#   Task: Create classes for Library, Book, and Member.
#The Library should manage books (add, remove) and
#track which members have borrowed which books.
#   Goal: Combine several concepts like:
#relationships, encapsulation, and basic CRUD operations in an object-oriented context.

# Launch the file via Python for it to open as separate window
import os

clear = lambda: os.system('cls')
lines_str = '<' + '=' * 100 + '>\n\n' + '<' + '=' * 100 + '>\n'

wp_welcome_str = 'Welcome to Library accounting'.center(102, ' ')
wp_option1_str = '\n' + ' ' * 40 + '1. Add a new book'
wp_option2_str = ' ' * 40 + '2. Remove a book'
wp_option3_str = ' ' * 40 + '3. Add a new member'
wp_option4_str = ' ' * 40 + '4. Show books list'
wp_option5_str = ' ' * 40 + '5. Show members list'
wp_option6_str = ' ' * 40 + '6. Borrow a book'
wp_option7_str = ' ' * 40 + '7. Return a book'
wp_option8_str = ' ' * 40 + '8. Exit application'
wp_option_number_input_str = '\nType a number of option:'

abp_welcome_str = 'To add a new book you have to type Book\'s Title and Book\'s Author'.center(102, ' ')
abp_title_input_str = '\n' + ' ' * 20 + 'Type book\'s title:'
abp_author_input_str = ' ' * 20 + 'Type book\'s author:'
abp_finish_str = '\n'+'Now book is added to the list!'.center(102, ' ')
abp_finish_option1_str = '\n' + ' ' * 20 + '1. Add a new book'
abp_finish_option2_str = ' ' * 20 + '2. Show books list'
abp_finish_option3_str = ' ' * 20 + '3. Back to the menu'
abp_option_number_input_str = '\nType a number of option:'

rembp_welcome_str = 'To remove a book choose an ID from list and type it in'.center(102, ' ')
rembp_table_book_variables_str = 'ID'.rjust(6, ' ') + ' || ' + 'Book\'s Title'.ljust(30, ' ') + ' || ' + 'Book\'s Author'.ljust(30, ' ') + ' || ' + 'Book\'s Holder'.ljust(20, ' ') + ' || \n ' + '-' * 100
rembp_book_index_input = '\n' + ' ' * 20 + 'Type book\'s ID:'
rembp_finish_str = '\n' + 'Now book is removed from list!'.center(102, ' ')
rembp_finish_option1_str = '\n' + ' ' * 20 + '1. Remove another book'
rembp_finish_option2_str = ' ' * 20 + '2. Add a new book'
rembp_finish_option3_str = ' ' * 20 + '3. Show books list'
rembp_finish_option4_str = ' ' * 20 + '4. Back to the menu'
rembp_option_number_input_str = '\nType a number of option:'

amp_welcome_str = 'To add a new member you have to type Member\'s Fullname'.center(102, ' ')
amp_fullname_input = '\n' + ' ' * 20 + 'Type member\'s full name:'
amp_finish_str = '\n' + 'Now member is added to the list!'.center(102, ' ')
amp_finish_option1_str = '\n' + ' ' * 20 + '1. Add a new member'
amp_finish_option2_str = ' ' * 20 + '2. Show members list'
amp_finish_option3_str = ' ' * 20 + '3. Back to the menu'
amp_option_number_input_str = '\nType a number of option:'

sbp_table_book_variables_str = 'ID'.rjust(6, ' ') + ' || ' + 'Book\'s Title'.ljust(30, ' ') + ' || ' + 'Book\'s Author'.ljust(30, ' ') + ' || ' + 'Book\'s Holder'.ljust(20, ' ') + ' || \n ' + '-' * 100
sbp_finish_option1_str = '\n' + ' ' * 20 + '1. Add a new book'
sbp_finish_option2_str = ' ' * 20 + '2. Borrow a book'
sbp_finish_option3_str = ' ' * 20 + '3. Back to the menu'
sbp_option_number_input_str = '\nType a number of option:'

smp_table_member_variables = ' || Full Name'.ljust(30,' ')+' || '+'Books taken'.ljust(66,' ')+ ' || \n ' + '-' * 100
smp_finish_option1_str = '\n' + ' ' * 20 + '1. Add a new member'
smp_finish_option2_str = ' ' * 20 + '2. Show books list '
smp_finish_option3_str = ' ' * 20 +'3. Return a book'
smp_finish_option4_str = ' ' * 20 + '4. Back to the menu'
smp_option_number_input_str = '\nType a number of option:'

bbp_welcome_str = 'Type in member\'s full name and book\'s ID to borrow a book'.center(100, ' ')
bbp_table_book_variables_str = 'ID'.rjust(6, ' ') + ' || ' + 'Book\'s Title'.ljust(30, ' ') + ' || ' + 'Book\'s Author'.ljust(30, ' ') + ' || ' + 'Book\'s Holder'.ljust(20, ' ') + ' || \n ' + '-' * 100
bbp_fullname_input = '\n' + ' ' * 20 + 'Type member\'s full name:'
bbp_index_input = ' ' * 20 + 'Type book\'s ID:'
bbp_finsh_output_str = '\n' + 'Now book is borrowed by member'.center(102, ' ')
bbp_finish_option1_str = '\n' + ' ' * 20 + '1. Borrow another book'
bbp_finish_option2_str = ' ' * 20 + '2. Return a book'
bbp_finish_option3_str = ' ' * 20 + '3. Back to the menu'
bbp_option_number_input_str = '\nType a number of option:'

retbp_welcome_str = 'Type in member\'s full name and book\'s title to return a book'.center(100, ' ')
retbp_table_member_variables = ' || Full Name'.ljust(30,' ')+' || '+'Books taken'.ljust(66,' ')+ ' || \n ' + '-' * 100
retbp_fullname_input_str = '\n'+' ' * 20+ 'Type member\'s full name:'
retbp_book_title_input_str = ' ' * 20 +'Type book\'s title:'
retbp_finish_output_str = '\n'+'Now book is returned to the library'.center(102, ' ')
retbp_finish_option1_str = '\n' + ' ' * 20 + '1. Return another book'
retbp_finish_option2_str = ' ' * 20 + '2. Borrow a book'
retbp_finish_option3_str = ' ' * 20 + '3. Back to the menu'
retbp_option_number_input_str = '\nType a number of option:'

class Library:
    def __init__(self):
        self.books = []
        self.members = []
    def add_book(self, book):
        self.books.append(book)
    def remove_book(self, index):
        #self.books = [book for book in self.books if book.title.upper != title.upper]
        for book in self.books:
            if book.index == index:
                self.books.remove(book)
                break
    def add_member(self, member):
        self.members.append(member)
    def print_book_list(self):
        list_book_id = 1
        list_index = 0
        for book in self.books:
            book.index = str(list_book_id)
            self.books[list_index].index = str(list_book_id)
            list_book_id += 1
            list_index +=1
            book_str = book.index.rjust(6,' ')+' || '+book.title.ljust(30,' ')+' || '+book.author.ljust(30,' ')+' || '+book.rn_owner.ljust(20,' ')+' || '
            print(book_str)
    def print_member_list(self):
        cnt = 0
        for member in self.members:

            print((' || '+member.Full_Name).ljust(30,' '), end='')
            for book in member.books_taken:
                if cnt == 0:
                    print(' || ' + (book.title + ' ' + book.author).ljust(66, ' ') + ' || ')
                    cnt +=1
                else:
                    print(' || ' + ' '* 26 + ' || ' + (book.title + ' ' + book.author).ljust(66, ' ') + ' || ')
            if not member.books_taken:
                print(' || '+' || '.rjust(70,' '))
    def borrow_book(self,Full_Name,index):      #maybe also add date of taking the book or last interaction
        book = None
        member = None
        for book in self.books:
            if book.index == index:
                break
        for member in self.members:
            if member.Full_Name == Full_Name :
                break
        self.books.remove(book)
        book.rn_owner = member.Full_Name
        self.books.append(book)
        member.books_taken.append(book)
    def return_book(self,Full_Name,title):
        book = None
        member = None
        for book in self.books:
            if book.title == title:
                break
        for member in self.members:
            if member.Full_Name == Full_Name:
                break
        member.books_taken.remove(book)
        self.books.remove(book)
        book.rn_owner = 'Library'
        self.books.append(book)
class Book:
    def __init__(self,title,author):
        self.title = title
        self.author = author
        self.rn_owner = 'Library'
        self.index = None
class Member:
    def __init__(self, Full_Name):
        self.Full_Name = Full_Name
        self.books_taken = []

def welcome_page():
        clear()
        print(lines_str)
        print(wp_welcome_str)
        print(wp_option1_str)
        print(wp_option2_str)
        print(wp_option3_str)
        print(wp_option4_str)
        print(wp_option5_str)
        print(wp_option6_str)
        print(wp_option7_str)
        print(wp_option8_str)
        wp_choice = input(wp_option_number_input_str)
        if wp_choice == '1':
            add_book_page()
        elif wp_choice == '2':
            remove_book_page()
        elif wp_choice == '3':
            add_member_page()
        elif wp_choice == '4':
            show_books_page()
        elif wp_choice == '5':
            show_members_page()
        elif wp_choice == '6':
            borrow_book_page()
        elif wp_choice == '7':
            return_book_page()
        elif wp_choice == '8':
            exit()
        else:
            welcome_page()
def add_book_page():
    clear()
    print(lines_str)
    print(abp_welcome_str)
    title = input(abp_title_input_str)
    author = input(abp_author_input_str)
    library.add_book(Book(title,author))
    print(abp_finish_str)
    print(abp_finish_option1_str)
    print(abp_finish_option2_str)
    print(abp_finish_option3_str)
    abp_choice = input(abp_option_number_input_str)
    if abp_choice == '1':
        add_book_page()
    elif abp_choice == '2':
        show_books_page()
    elif abp_choice == '3':
        welcome_page()
    else:
        welcome_page()

def remove_book_page():
    clear()
    print(lines_str)
    print(rembp_welcome_str)
    print('\n'+rembp_table_book_variables_str)
    library.print_book_list()
    book_id = input(rembp_book_index_input)
    library.remove_book(book_id)
    print(rembp_finish_str)
    print(rembp_finish_option1_str)
    print(rembp_finish_option2_str)
    print(rembp_finish_option3_str)
    print(rembp_finish_option4_str)
    rembp_choice = input(rembp_option_number_input_str)
    if rembp_choice == '1':
        remove_book_page()
    elif rembp_choice == '2':
        add_book_page()
    elif rembp_choice == '3':
        show_books_page()
    elif rembp_choice == '4':
        welcome_page()
    else:
        welcome_page()

def add_member_page():
    clear()
    print(lines_str)
    print(amp_welcome_str)
    full_name = input(amp_fullname_input)
    library.add_member(Member(full_name))
    print(amp_finish_str)
    print(amp_finish_option1_str)
    print(amp_finish_option2_str)
    print(amp_finish_option3_str)
    amp_choice = input(amp_option_number_input_str)
    if amp_choice == '1':
        add_member_page()
    elif amp_choice == '2':
        show_members_page()
    else:
        welcome_page()

def show_books_page():
    clear()
    print(lines_str)
    print(sbp_table_book_variables_str)
    print(library.print_book_list())
    print(sbp_finish_option1_str) # I have no idea from where appears None in output
    print(sbp_finish_option2_str) # I spent about an hour on trying to find it via debug tools but no results(
    print(sbp_finish_option3_str) # So I just left it there, sorry(( If you will be able to find the mistake please tell me
    sbp_choice = input(sbp_option_number_input_str)
    if sbp_choice == '1':
        add_book_page()
    elif sbp_choice == '2':
        remove_book_page()
    elif sbp_choice == '3':
        welcome_page()
    else:
        show_books_page()

def show_members_page():
    clear()
    print(lines_str)
    print(smp_table_member_variables)
    library.print_member_list()
    print(sbp_finish_option1_str)
    print(sbp_finish_option2_str)
    print(sbp_finish_option3_str)
    smp_choice = input(smp_option_number_input_str)
    if smp_choice == '1':
        add_book_page()
    elif smp_choice == '2':
        borrow_book_page()
    elif smp_choice == '3':
        welcome_page()
    else:
        welcome_page()

def borrow_book_page():
    clear()
    print(lines_str)
    print(bbp_welcome_str)
    print(bbp_table_book_variables_str)
    library.print_book_list()
    member_fullname = input(bbp_fullname_input)
    book_id = input(bbp_index_input)
    library.borrow_book(member_fullname,book_id)
    print(bbp_finsh_output_str)
    print(bbp_finish_option1_str)
    print(bbp_finish_option2_str)
    print(bbp_finish_option3_str)
    bbp_choice = input(bbp_option_number_input_str)
    if bbp_choice == '1':
        borrow_book_page()
    elif bbp_choice == '2':
        return_book_page()
    elif bbp_choice == '3':
        welcome_page()
    else:
        welcome_page()

def return_book_page():
    clear()
    print(lines_str)
    print(retbp_welcome_str)
    print(retbp_table_member_variables)
    library.print_member_list()
    member_fullname = input(retbp_fullname_input_str)
    book_title = input(retbp_book_title_input_str)
    library.return_book(member_fullname,book_title)
    print(retbp_finish_output_str)
    print(retbp_finish_option1_str)
    print(retbp_finish_option2_str)
    print(retbp_finish_option3_str)
    retbp_choice = input(retbp_option_number_input_str)
    if retbp_choice == '1':
        return_book_page()
    elif retbp_choice == '2':
        borrow_book_page()
    elif retbp_choice == '3':
        welcome_page()
    else:
        welcome_page()


library = Library()
welcome_page()





#library = Library()
#library.add_member(Member('Sasha Andromedow',library))
#library.add_member(Member('Masha Andromedowa',library))
#library.add_book(Book('32123','22232222'))
#library.add_book(Book('123','111111'))
#library.add_book(Book('321','222222'))
#library.print_book_list()
#library.print_member_list()
#library.borrow_book('Sasha Andromedow','123')
#library.print_book_list()
#library.print_member_list()
#library.return_book('Sasha Andromedow','123')
#library.print_book_list()
#library.print_member_list()
#library.remove_book('123')
#library.print_book_list()
#library.print_member_list()
