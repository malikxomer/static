#dictionay is made up of to things i-e key and value
# In java we call them maps of graphs
#Dictionay[key] --> value
# dictionart = {'name':'Omer' , 'Age':'24'}
#1 : Simple Dictionary ==
phone_book = {
    'omer' : '000-123-456-789',
    'Basil' : '111-123-456-789',
    'Iftikhar' : '222-123-456-789'
              }
print(phone_book['omer'])

#2 : Dictionary keys containing Lists ==
#Each key contains multiple values
phone_book = {
    'omer' : ['000-111-222-333','omer@omer.com','Rawalpindi'],
    'basil' : ['666-777-888-999','basil@basil.com','Gujrat'],
    'iftikhar' : ['555-555-666-555','ifti@ifti.com','Peshawar']
              }
print(phone_book['omer'][1])
