import pandas as pd

employee={'number':[1,2,3,4,5], 'name':["shyam", "shivam", "rahul", "rohit", "sonu"], 'salary':[2345,2543,3243,2341,4563]}
table1=pd.DataFrame(employee)
print(table1)

# print(table1.head(3))
# print(table1.tail(2))