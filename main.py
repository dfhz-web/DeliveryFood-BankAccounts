class FoodDeliverySystem:

    #Class attributes
    order_id = 0
    orders_log = {}

    def __init__(self):
        #in this case it's gonna be a dictionary insted of being pass as a parameter

        #instance
        self.menu = {
            "Burger" : 150,
            "Pizza" : 250,
            "Pasta" : 200,
            "Salad" : 120,
            "Beverages" : 130,
            "Noodles" : 150,
            "Sushi" : 270,
            "Bakery" : 350
            #Here you can add more items to the menu
        }
        self.bill_amount = 0
    
    def display_menu(self):
        print("Menu Options")

        for key, value in self.menu.items():
            print(f'{key} | {value}')

    
    def place_order(self, customer_name, order_items):
        print("Placing order")
        # print(f'{customer_name} and {order_items}')
        # return None
        # order_id += 1


        #1 STEP
        #Convert the "order_items " string to a dictionary
        # string to a list and then to a dictionary

        #outputstring "Burger:1 , Pasta:5,  Salad:1 "
        

        #string to a list
        string_to_list = [item.split(":") for item in order_items.split(",")]
        
        #list to a dic

        list_to_dic = {item[0].strip(): int(item[1].strip()) for item in string_to_list}
        
        # to determine the next available order number
        next_order_number = max(self.orders_log.keys()) + 1 if self.orders_log else 1 
        print(next_order_number)
        #STEP2  
        #Find the next available order number
        # next_order_number = max(orders_log.keys())


        #3 Add a new entry to the 'orders_log' dicitionary using the obtained order number, "customer_name" and the covereted "order_items"

        self.orders_log[next_order_number] = {
            # we don't use self bc we are taking the arguments asked by this method
            "customer_name" : customer_name,
            "order_items" :  list_to_dic
        }

 
        #Give used to the status key asked 
        approval = input("Do you want to place this order? say yes to continue  \n")
       
        if approval  == "yes":
            self.orders_log[next_order_number]["status"] = "Placed"
            print(f"Your order has been placed, order number {next_order_number}")
            return 
        else:
            print("Order placement failed")
            return 
    

    def pickup_order(self, order_id):
        print('**********************')
        print("Pick up in process")
        print(f"Order number {order_id}")

        self.orders_log[order_id]["status"] = "Picked up"

        print("Order's status has been updated \n")
        print(self.orders_log[order_id]["status"])
        return 

       
    def deliver_order(self, order_id):
        print('*************************')

        print('Delivery in process')
        print(f"Order number {order_id}")

        confirmation = input("the delivered was successful? if yes, say yes \n")

        if confirmation == "yes":
           self.orders_log[order_id]["status"] = "Delivered"
        else:
           self.orders_log[order_id]["status"] = "Not Delivered"

        print("Order's status has been updated \n")
        print(self.orders_log[order_id]["status"])
        return 
     
    #this method means to change all items
    def modify_order(self, order_id, new_items):
        print("Order is being modified ")
        #check if the wer are receving arguments

        # print(f"{order_id} and {new_items}")  ok



        # new _items string to a list
        string_to_list = [item.split(":") for item in new_items.split(",")]
        
        #list to a dic

        list_to_dic = {item[0].strip(): int(item[1].strip()) for item in string_to_list}
        

        
        #4 check if the status is not picked or delivered to proceed modifying 
        
        
        if self.orders_log[order_id]["status"] != "Delivered" and  "Picked up":
            #3 update "order_items"

           self.orders_log[order_id]["order_items"] =  list_to_dic
           self.orders_log[order_id]["status"] =  "Placed"

           print(f"Your order has been successful updated{self.orders_log[order_id]}")

           return
        else:
            print("Too late")
            return
        
    def generate_bill(self, order_id):
       
        print("Generate bill")
        #1 STEp GET THE TOTAL AMOUNT wihtout taxes
        # bill= sum(value for value in self.orders_log[order_id]["order_items"].values())
        
        # print(self.orders_log[order_id]["order_items"])
        order_content_keys = self.orders_log[order_id]["order_items"].keys()
        # print(order_content_keys)
        # print('for')
        order_details = {}
        bill = 0
        for key, value in self.menu.items():
            # print(f'{key} | {value}')
            if key in order_content_keys:
                # print(value)
                bill += value 
         
        # get the 10 % and 5% of the bill in local variables
        bill_10 = bill * 0.10
       
        bill_5 = bill * 0.05
      

        if bill > 1000:
            total = bill + bill_10
        elif bill < 1000:
            total =  bill + bill_5


        

        print(total)
        return total
     
    def cancel_order(self, order_id):
        print("Canceling order")
        print(order_id)


        if self.orders_log[order_id]["status"] != "Delivered" and  "Picked up":
            del self.orders_log[order_id]
            print(self.orders_log)
            return
        else:
            print("It was not possible to cancel the order, check here for more info")
            return

    
    def test(self):
        print(self.orders_log)


        

