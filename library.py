class Library:
    def __init__(self, book_list, name):
        self.booksList = book_list
        self.name = name
        self.lendDict = {}

    def displayBooks(self):
        print(f"\n📚 Welcome to {self.name} Library! Here are the available books:")
        for book in self.booksList:
            print(f" - {book}")

    def lendBook(self, user, book):
        if book not in self.booksList:
            print("❌ Sorry, this book is not in our collection.")
        elif book not in self.lendDict:
            self.lendDict[book] = user
            print(f"✅ '{book}' has been lent to {user}. Enjoy your reading!")
        else:
            print(f"⚠️ Sorry, '{book}' is already being used by {self.lendDict[book]}.")

    def addBook(self, book):
        self.booksList.append(book)
        print(f"📘 '{book}' has been added to the library.")

    def returnBook(self, book):
        if book in self.lendDict:
            self.lendDict.pop(book)
            print(f"🔄 '{book}' has been returned. Thank you!")
        else:
            print("⚠️ This book wasn't lent out from our library.")

# Main program
if __name__ == '__main__':
    books = Library(
        ['Python', 'Rich Dad Poor Dad', 'Harry Potter', 'C++ Basics', 'Algorithms by CLRS'],
        "Let's Upskill"
    )

    while True:
        print(f"\n📖 Welcome to the {books.name} Library")
        print("Choose an option:")
        print("1. Display Books")
        print("2. Lend a Book")
        print("3. Add a Book")
        print("4. Return a Book")

        user_choice = input("Enter your choice (1-4): ")

        if user_choice not in ['1', '2', '3', '4']:
            print("❌ Invalid option. Please try again.")
            continue

        user_choice = int(user_choice)

        if user_choice == 1:
            books.displayBooks()

        elif user_choice == 2:
            book = input("📚 Enter the name of the book you want to lend: ")
            user = input("🙋 Enter your name: ")
            books.lendBook(user, book)

        elif user_choice == 3:
            book = input("📘 Enter the name of the book you want to add: ")
            books.addBook(book)

        elif user_choice == 4:
            book = input("🔄 Enter the name of the book you want to return: ")
            books.returnBook(book)

        user_choice2 = input("\nPress 'q' to quit or 'c' to continue: ").lower()
        if user_choice2 == 'q':
            print("👋 Thanks for visiting the library. Goodbye!")
            break
        elif user_choice2 != 'c':
            print("⚠️ Invalid input. Returning to main menu...")
