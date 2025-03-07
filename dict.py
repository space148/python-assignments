#creating Dictionary
a={1:'Dinesh', 2:'Dinu',3:'Sai',4:'Bailapudi',5:'Bailapudi Sai Dinesh'}

#adding new value
a[6]='SaiDinesh'

#updating the value in dictionary
a[1]='Dinesh Bailapudi'

#accessing the values in the dictionary
print('5th value in a : ',a[5])

#nested loop dictionary
nested_dict = {}
for i in range(1, 4):
    nested_dict[i] = {}
    for j in range(1, 4):
        # Assign values to the nested dictionary
        nested_dict[i][j] = f"Value ({i}, {j})"

# Print the nested dictionary
print('\n\nnested dictionary : \n',nested_dict,'\n\n')

#keys in a dictionary
print('keys in a')
for i in a:
    print(i,end=' ')

#delete a value from a dictionary
del a[2]
print('\n\na : ',a)