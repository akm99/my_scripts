book_bought = int(input("Enter the number of books purchased: "))
pencil_bought = int(input("Enter the number of pencils purchased: "))
rubber_bought = int(input("Enter the number of rubbers purchased: "))


def find_total(bb,pb,rb):
    total = 0
    book = 10
    pencil = 10
    rubber = 10
    total = (book * bb) + (pencil * pb) + (rubber * rb)
    return total

print ("The total is: {}".format(find_total(book_bought,pencil_bought,rubber_bought)))

