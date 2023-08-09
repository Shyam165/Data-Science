import pandas as pd

food1={'number':[1,2,3,4,5], 'name':["apple", "banana","chips", "popcorns", "pizza"], 'price':[100, 200, 234, 321, 456]}
food2={'color':["red", "white", "blue", "purple", "black"], 'weight':[2, 3,4,5,6], 'qty':[1,2,3,3,4]}

table1=pd.DataFrame(food1)
table2=pd.DataFrame(food2)

fusion=table1.join(table2)

print(fusion)