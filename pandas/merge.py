import pandas as pd

employee1={'number':[1,2,3,4,5], 'name':["shyam", "shivam", "rahul", "rohit", "sonu"], 'salary':[2345,25443,3243,2341,4563]}
employee2={'number':[1,2,3,4,5], 'name':["sohan", "shivam", "rahul", "rohit", "sonu"], 'salary':[2345,2543,3243,2341,4563]}

#note: if we change some data in above both table then only common data in both table will be printed otherwise if both table is same then output will be same as one of the table

table1=pd.DataFrame(employee1)
table2=pd.DataFrame(employee2)

fusion=pd.merge(table1,table2, on='name')  # here only 'name' column common item will be printed and in final column only one common name is printed

print(fusion)