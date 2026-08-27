info={'Goku':'Ultra Instinct',
      'Luffy':'Gear 5',
      'Ichigo':'Blood Chain'}
print(info)
info['Naruto']={'Sage Mode','Baryon Mode'}
info['Asta']='Demon Form'
print(info)
print(info['Ichigo'])
print(info.keys())
print(info.values())
print(info.items())
del info['Asta']
print(info.pop('Naruto'))
print(info)
info['Goku']='Mastered Ultra Instinct'
print(info['Goku'])