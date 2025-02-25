def main():
    book_list = []

    N = int(input("Enter the number of books: "))

    for i in range(N):
        print(f"\nEnter details for Book {i+1}:")
        title = input("Title: ")
        author = input("Author: ")
        ISBN = input("ISBN: ")
        price = float(input("Price: "))

        book = Book(title, author, ISBN, price)
        book_list.append(book)

    print("\n--- Book Details ---")
    for book in book_list:
        book.display_info()

if __name__ == "__main__":
    main()
