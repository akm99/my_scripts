def take_input(bb,pb,rb):
    bb = int(input("Enter the number of books purchased: "))
    pb = int(input("Enter the number of pencils purchased: "))
    rb = int(input("Enter the number of rubbers purchased: "))
    return bb,pb,rb


def find_total(a,b,c):
    total = 0
    book = 10
    pencil = 10
    rubber = 10
    total = (book * a) + (pencil * b) + (rubber * c) 
    return(total)

print(find_total(take_input(bb,pb,rb)))
