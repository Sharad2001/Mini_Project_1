class Library:
    def __init__(self, list, name):
        self.booklist = list
        self.name = name
        self.lendDict = {}

    def displayBooks(self):
        print(f"we have following books in our library {self.name}.")
        for book in self.booklist:
            print(book)
    def lendBook(self, user, book):
        if book not in self.lendDict.keys():
            self.lendDict.update({book:user})
            print("Lender-Book database has been updated."
                  "You can take the book now")
        else:
            print(f"Book is already being used by {self.lendDict[book]}")

    def addBook(self, book):
        self.booklist.append(book)
        print("Book has been added to the book list.")

    def returnBook(self, book):
        self.booklist.remove(book)

if __name__ == '__main__':
    sharad = Library(["Python", "Rich daddy Poor daddy", "Harry Potter",
                     "C++"], "Oxford")

    while (True):
        print(f"Welcome to the {sharad.name} library.  Enter your choice to continue")
        print("1. Display a Books")
        print("2. Lend a Books")
        print("3. Add a Books")
        print("4. Return a Books")
        user_choice = int(input())

        if user_choice == 1:
            sharad.displayBooks()
        elif user_choice == 2:
            book = input("Enter the book you want to lend: ")
            name = input("Enter your name: ")
            sharad.lendBook(user, book)
        elif user_choice == 3:
            book = input("Enter the book you want to add: ")
            sharad.addBook(book)
        elif user_choice == 4:
            book = input("Enter the book you want to return: ")
            sharad.returnBook(book)
        else:
            print("Not a valid option.")

        print("Press q to quit and c to continue")
        user_choice2 = ""
        while (user_choice2 != "c" and user_choice2 != "q"):

            user_choice2 = input()
            if user_choice2 == "q":
                exit()

            elif user_choice == "c":
                continue