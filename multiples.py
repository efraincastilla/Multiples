# This program is a chalenge in order to print:
#  "Linio" if number is multiple of 3
#  "IT" if number is multiple of 5
# "Linianos" if number is multiple of 3 and 5

def Multiples(num):
    results = ["Linianos", "", "", "Linio", "", "IT", "Linio", "", "", "Linio", "IT", "", "Linio", "", ""]
    prn = results[num % 15]
    
    if (len(prn) == 0):
        prn = str(num)
    
    return prn

if __name__ == "__main__":
    for i in range(1,101):
        print (Multiples(i))

print ("That's all folks!")

 