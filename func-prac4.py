book_bought = int(input("Enter the number of books purchased: "))
pencil_bought = int(input("Enter the number of pencils purchased: "))
rubber_bought = int(input("Enter the number of rubbers purchased: "))


def find_total(total):
    total = 0
    book = 10
    pencil = 10
    rubber = 10
    total = (book * book_bought) + (pencil * pencil_bought) + (rubber * rubber_bought)
    return total

print ("The total is: {}".format(find_total))

