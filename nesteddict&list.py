#dictionary inside dictionary
info={'Goku':{'age':43,'Highest form':'Ultra Instinct'},
      'Vegeta':{'age':48,'Highest form':'Ultra Ego'}}
print(info['Goku'])
print(info['Vegeta']['Highest form'])
info['Gohan']={'age':23,'Highest form':'Beast Form','children':'Pan'}
print(info['Gohan'].pop('children'))


#list inside dictionary
district_data={'Comilla':['Sadar','Kotbari'],
             'Dhaka':['Banani','Gulshan','Dhanmondi']}
print(district_data)
print(district_data['Comilla'])


#dictionary inside list
student_data=[{'Name':'Yeasin','age':22,'grade':'A+'},
              {'Name':'Jihad','age':22,'grade':'A'}]
print(student_data[1])
student_data.append({'Name':'Sayem','age':23,'grade':'B+'})
print(student_data)