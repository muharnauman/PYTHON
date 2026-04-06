layers = ['charles', 'martina', 'michael', 'florence', 'eli'] 
print(layers[0:3])
def nauman(index,index1):
   index=input(" firast in put")
   index1=input(" firast in put")
  
def make_pizza(**toppings):
 for topping in toppings:
  
  print(topping)
 
make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')
def build_profile(first, last, **user_info):
 """Build a dictionary containing everything we know about a user."""
 profile = {}
 profile['first_name'] = first
 profile['last_name'] = last
 for k, value in user_info.items():
  profile[k] = value
 return profile
user_profile = build_profile('albert', 'einstein',
location='princeton',
 field='physics')
print(user_profile)
def make_pizza(size, *toppings):

 print("\nMaking a " + str(size) +"-inch pizza with the following toppings:")
 for topping in toppings:
  print("- " + topping)