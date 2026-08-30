saiyan_data=[
    {'name':'Goku',
     'age':43,
     'form':'Autonomus Ultra Instinct'},
    {'name':'Vegeta',
     'age':48,
     'form':'Ultra Ego'
    }
]
def add_new_saiyan(name, age, form):
    new_saiyan={}
    new_saiyan['name']=name
    new_saiyan['age']=age
    new_saiyan['form']=form
    saiyan_data.append(new_saiyan)
add_new_saiyan('Gohan',23,'Beast Form')
add_new_saiyan('Trunks',20,'Super Saiyan Rage')
print(saiyan_data[3])

