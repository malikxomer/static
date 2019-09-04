#index('|') is used to get the index number of '|'
# First Way: This is manual and not good for too much data i-e spread sheet
data = 'XBOX 360 | 150 | New'
product_name = data[:data.index('|')]
product_price = data[11:15]
product_condition = data[16:]
print("product name = "+product_name)
print("product price = "+product_price)
print("product condition ="+product_condition)

# Second way: But this is too length so we have a third way
data = 'XBOX 360 | 150 | New'
product_name = data[:data.index('|')]
print("product name = "+product_name)

new_data = data[data.index('|')+1:]
product_price = new_data[:new_data.index('|')]
print("product price = "+product_price)

product_condition = new_data[new_data.index('|')+1:]
print("product condition ="+product_condition)

#Third way: By using find(), it is short and fast
data = 'XBOX 360 | 150 | New'
product_name_index = data.find('|')
product_name = data[:product_name_index]
print("product name = "+product_name)

#start finding for '|' and starts from index 10 i-e product_name_index+1
product_price_index = data.find('|',product_name_index+1)
product_price = data[product_name_index+1:product_price_index]
print("product price = "+product_price)

#start finding for '|' and starts from index 16 i-e product_price_index+1
product_condition = data[product_price_index+1:]
print("product condition ="+product_condition)



# WE CAN DIRECTLY FIND FROM PIPE TO PIPE I-E ('|') TO ('|')
product_price = data[data.find('|')+1 : data.find('|',10)]
print(product_price)
