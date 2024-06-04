


class Library:
    def __init__(self, listofbooks, libraryname):
        self.lst = listofbooks
        self.name = libraryname
        self.d = {}

    def displaybook(self):
        return f"\t\t\t\tWelcome to {self.name}\nAvailable books are -\n{self.lst}"

    def lendbook(self, lendname, bookname):
        if bookname in self.lst and bookname not in self.d:
            print(f"{bookname} lent to {lendname}")
            self.d[bookname] = lendname
        elif bookname in self.d:
            print("Book is not available. Lent to -", self.d[bookname], "\nWe only have -", self.lst)
        else:
            print("Book is not in the library. We only have -", self.lst)

    def addbook(self, bookname):
        print("Book added successfully in the library")
        self.lst.append(bookname)

    def returnbook(self, returnername, bookname):
        if bookname in self.d and self.d[bookname] == returnername:
            print("Book successfully returned")
            self.d.pop(bookname)
        else:
            print("Wrong data or book was not lent out")

if __name__ == '__main__':
    lst = ['Python', 'Science', 'Mathematics', 'Social Science']
    l = Library(lst, 'World Library')
    print(l.displaybook())

    exit = 1
    while exit:
        print("For Lending book press 1\nFor adding book press 2\nFor returning book press 3\nFor exit press 4")
        n = int(input())
        if n == 1:
            l.lendbook(input("Enter your name-"), input("Enter book name-"))
        elif n == 2:
            l.addbook(input("Enter book name you want to add-"))
        elif n == 3:
            l.returnbook(input("Enter your name-"), input("Enter book name-"))
        elif n == 4:
            exit = 0
        else:
            print("Wrong input")






