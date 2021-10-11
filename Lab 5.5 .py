# Student ID : 1201201025
# Student Name : Tai Jun Ping

def rectangle(width,length):
    area = length * width
    return area

def triangle(width,length):
    area = (length * width) /2
    return area

i=0
while(i<2):
    width = float(input("Enter width : "))
    length = float(input("Enter length : "))

    ar = rectangle(length,width)
    at = triangle(length,width)

    print("Rectangle area : {:.2f}".format(ar))
    print("Triangle area : {:.2f}".format(at))
    i+=1