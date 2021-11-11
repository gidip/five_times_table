# Multiplication table from 0 to 12

#Change the value of num variable for different time table. 
num = 5

# To take input from the user - e.g type 6 to get six times table.
# num = int(input("Display multiplication table of? "))

# Iterate 10 times from i = 0 to 12 - Change the value 13 to multiply bigger numbers!!!
for i in range(0, 13):
   print(num, 'x', i, '=', num*i)