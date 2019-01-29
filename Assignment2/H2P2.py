import datetime
now = datetime.datetime.now()
book_title = input("What is the name of your book? ")
book_author = input("Who is the author of {}? ".format(book_title))
book_pub = int(input("When was this book published is this book? "))
book_page = int(input("How many pages does {} have? ".format(book_title)))
book_age = now.year - book_pub
if (book_age < 10):
    print("This book is young!")
else:
    print("the book old!")
if (book_page < 100):
    print("Book long")
elif (100 <= book_page <= 300):
    print("Book longer")
else:
    print("book too long")