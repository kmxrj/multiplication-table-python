import pandas as pd 
from tabulate import tabulate

#creating a list of list containing my multiplication table
multi_table = []
y = 1
#set size of table
user_in = input("Enter up to what integer you want the multiplication table: ")
size = int(user_in)

#loop filling the multiplication table
for j in range(size) :
    table = []
    x = 1
    for i in range(size) :
        table.append(y * x)
        x = x + 1
    multi_table.append(table)
    y = y + 1

#converts the raw dictionaries into a more usable pandas
df = pd.DataFrame(multi_table)

#prints out table
print(tabulate(df, tablefmt = 'simple_grid', showindex = False)) 