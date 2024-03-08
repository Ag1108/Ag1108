#library management system
import datetime
def get_date():
    date_entry = input("Enter a date in YYYY-MM-DD format: ")
    year, month, day = map(int, date_entry.split("-"))
    date1 = datetime.date(year, month, day)
    return date1
class Library:
    def __init__(self,college):
        self.books = []
        self.college = college
    
    def addbook(self,title, author, copies, in_date):
        book = {"title":title, "author":author, "copies":copies,
                "in_date":(in_date),"avbl_copies":copies}
        self.books.append(book)
        print(f"{title} has been added to library !!")
        return True
    
    def find_book(self,title=''):
        c = 0
        for book in self.books:
            if book["title"] == title:
                return book,c
            c+=1
        return None
    
    def issue_book(self,title):
        book = self.find_book(title)
        if(book):
            book["avbl_copies"] -=1
            return True
        else:
            return False
    def return_book(self,title):
        book = self.find_book(title)
        if book:
            if book["avbl_copies"] < book["copies"]:
                book["avbl_copies"] +=1
                return True
            else :
                return False
        else:
            return False
    
class Student:
    def __init__(self,name,usid,lib):
        self.name = name
        self.usid = usid
        self.issbook = []
        self.lib = Library(lib)
    
    def create_acc(self,name,usid,lib):
        self.name = name
        self.usid = usid
        
    def borrow_book(self,title,date):
        if self.lib.issue_book(title):
            book = self.lib.find_book(title)
            issbook = {"title" : book[0]["title"], "b_date" : date}
            self.issbook.append(issbook)
            return True
        return False
    
    def return_book(self,title,date):
        for i in range(len(self.issbook)):
            if self.issbook[i]["title"] == title:
                if self.issbook[i]["b_date"] < date:
                    self.issbook.pop(i)
                    if (self.lib.return_book(title)):
                        return True
                    else :
                        return False
                else :
                    return False
        else : 
            return False
        
def lib():
    clg = input("College : ")
    lib = Library(clg)
    print("Pls add books : \n")
    while True:
        title =input("Title : ")
        author = input("Author : ")
        copies = int(input("No. of copies : ")) 
        in_date = get_date()
        lib.addbook(title,author,copies,in_date)
        ch = input("Wish to continue Y/N : ")
        if ch == 'Y' or ch == 'y':
            continue
        else:
            break
    return lib

def student(lib):
    print("Pls give details for the student : ")
    name = input("Name : ")
    usid = int(input("Us_ id : "))
    stud = Student(name,usid,lib)
    return stud

def find_student(usid,students):
    for i in range(len(students)):
        if usid == students[i].usid:
            return i
    else:
        return False

def main():
    print("/t Welcome to Library Management System/t/n")
    print("Library/n")
    lib1 = lib()
    students=[]
    print("Please add first student.")
    students.append(student(lib1))
    while True:
        ch = ('''Pls choose from following : 
1 -> Add student
2 -> Borrow book
3 -> Return book
4 -> Current issues
5 -> EXIT 
choice : ''')   
        if ch == 1:
            students.append(student(lib1))
        elif ch == 2:
            usid = int(input("Please input user id for the student : "))
            stud = find_student(usid,students)
            title = input("Please give title to be borrowed : ")
            date = get_date()
            if stud:
                if (students(stud).borrow_book(title,date)):
                    print("Book Borrowed")
                else :
                    print("book cannot be borrowed")
        elif ch == 3:
            usid = int(input("Please input user id for the student : "))
            stud = find_student(usid,students)
            title = input("Please give title to be returned : ")
            date = get_date()
            if stud:
                if (students(stud).return_book(title,date)):
                    print("Book Returned")
                else :
                    print("book cannot be returned")
        elif ch == 4:
            usid = int(input("Please input user id for the student : "))
            stud = find_student(usid,students)
            print(students[stud].issbook)  
        elif ch == 5:
            break
        else:
            continue
    return 0

main()           