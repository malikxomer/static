
data = 'XBOX 360 | 150 | NEW'
details = data.split('|')
print(details)
product_name=details[0]
product_price=details[1]
product_condition=details[2]
print(product_name)
print(product_price)
print(product_condition)

#Easiest way of doing the same
product,price,condition = data.split('|')
print(product)
print(price)
print(condition)
