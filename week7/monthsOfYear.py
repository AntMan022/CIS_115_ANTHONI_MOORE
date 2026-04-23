

print("months 1-12")
startmonth = int(input("Give your start month as #: "))-1
endmonth = int(input("Give your end month as #: "))
months = ["Jan", "Feb", "March", "Apirl", "May", "June", "July", "Aug", "Sept", "Oct", "Nov", "Dec"]


def months_of_year(startmonth, endmonth):
    for i in range (startmonth, endmonth):
        print(months[i])


months_of_year(startmonth, endmonth)
