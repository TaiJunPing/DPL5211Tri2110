# Student ID : 1201201025
# Student Name : Tai Jun Ping

banana = 1.5 #constant value, the value doesn't change, name in Capital letters
graps = 5.6

print("Invoice for Fruits Purchase")
print("---------------------------------")

bananas = int(input("\nEnter the quantity (comb) of bananas bought: "))
grapes = int(input("Enter the amount (kg) of grapes bought: "))

rbananas = bananas * banana
rgrapes = grapes * graps

total = rbananas + rgrapes
print("\nItem\t\tQty\tPrice\tTotal")
print("Banana (combs)\t",bananas,"\tRM1.50\tRM {:.2f}".format(rbananas))
print("Grapes (kg)\t",grapes,"\tRM5.60\tRM {:.2f}".format(rgrapes))
print("\nTotal: RM {:.2f}".format(total))