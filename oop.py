from main import FoodDeliverySystem

table1 = FoodDeliverySystem()
# table1.display_menu()
print('*****************************************')
table1.place_order("Daniel","Burger:1 , Pasta:1,  Salad:1 ")
print('*****************************************')

# table1.deliver_order(1)
print('*****************************************')
# table1.modify_order(1, "Noodles:150, Sushi:270" )
print('*****************************************')
# table1.pickup_order(1)
print('*****************************************')
table1.generate_bill(1)
print('*****************************************')



daniel = FoodDeliverySystem()
daniel.place_order("Daniel","Burger:1000 ")
# table1.cancel_order(1)
daniel.test()
