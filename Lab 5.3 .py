# Student ID : 1201201025
# Student Name : Tai Jun Ping

# Display the menu
# Ask the user to enter their choice [1 or 2]
# Using a switch-case statement
# If choice is 1 call function get_cm()
# If choice is 2 call function get_meter()
#    Else print "Invalid choice"
# In get_cm():
# Get the value of centimeter from the User
# Call function cm_to_meter(...) and pass centimeter to calculate meter
# Display the centimeter and meter

print("====================================")
print("\t       MENU")
print("====================================")
print(" 1. Convert centimeter to meter.")
print(" 2. Convert meter to centimeter.")
print("====================================")
choice = (input("Enter your choice [1|2] :"))

def get_cm():
    cm = float(input("Please enter a value for centimeter : "))
    m = cm_to_meter(cm)
    print(" {:.2f} cm is {:.2f} meter".format(cm,m))

def cm_to_meter(centimeter):
    meter = centimeter / 100
    return meter

def get_meter():
    m = float(input("Please enter a value for meter : "))
    cm = meter_to_cm(m)
    print(" {:.2f} meter is {:.2f} cm".format(m,cm))

def meter_to_cm(meter):
    centimeter = meter * 100
    return centimeter

if(choice=='1'):
    get_cm()
elif(choice=='2'):
    get_meter()
else:
    print("INVALID CHOICE")
