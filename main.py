MENU = {                                                                                
    "espresso": {                                                                       
        "ingredients": {                                                                
            "water": 50,                                                                
            "coffee": 18,                                                               
        },                                                                              
        "cost": 1.5,                                                                    
    },                                                                                  
    "latte": {                                                                          
        "ingredients": {                                                                
            "water": 200,                                                               
            "milk": 150,                                                                
            "coffee": 24,                                                               
        },                                                                              
        "cost": 2.5,                                                                    
    },                                                                                  
    "cappuccino": {                                                                     
        "ingredients": {                                                                
            "water": 250,                                                               
            "milk": 100,                                                                
            "coffee": 24,                                                               
        },                                                                              
        "cost": 3.0,                                                                    
    }                                                                                   
}                                                                                       
profit = 0                                                                              
resources = {                                                                           
    "water": 300,                                                                       
    "milk": 200,                                                                        
    "coffee": 100,                                                                      
}                                                                                       
def is_resource_sufficient(ingredients):                                                
    is_enough = True                                                                    
    for item in ingredients:                                                            
        if ingredients[item] > resources[item]:                                         
            print(f"Sorry there is not enough {item}")                                  
            is_enough = False                                                           
    return is_enough                                                                    
                                                                                        
                                                                                        
def process_coins():                                                                    
    print("Please insert coins")                                                        
    total = int(input("How many quarters?")) * 0.25                                     
    total += int(input("How many Dime?")) * 0.10                                        
    total += int(input("How many Nickel?")) * 0.05                                      
    total += int(input("How many Penny?")) * 0.01                                       
                                                                                        
    return total                                                                        
                                                                                        
                                                                                        
def transaction_successful(money_received, drink_cost):                                 
    """Return true when the payment is accepted, or False if money is insufficient"""   
    if money_received >= drink_cost:                                                    
        change = round(money_received - drink_cost, 2)                                  
        print(f"Here is ${change} as change")                                           
        global profit                                                                   
        profit += drink_cost                                                            
        return True                                                                     
    else:                                                                               
        print("Sorry that's not enough money, money refunded.")                         
        return False                                                                    
                                                                                        
def make_coffee(drink_name, order_ingredients):                                         
    """Deducts the required ingredients from the resources"""                           
    for item in order_ingredients:                                                      
        resources[item] -= order_ingredients[item]                                      
    print(f"Here is your {drink_name}. Enjoy!")                                         
                                                                                        
game_is_on = True                                                                       
                                                                                        
while game_is_on:                                                                       
    choice = input("What would you like? (espresso/latte/cappuccino/):")                
    if choice == "off":                                                                 
        game_is_on = False                                                              
    elif choice == "report":                                                            
        print(f"Water: {resources['water']}")                                           
        print(f"Milk: {resources['milk']}")                                             
        print(f"Coffee: {resources['coffee']}")                                         
        print(f"Money: {profit}")                                                       
    else:                                                                               
        drink = MENU[choice]                                                            
        if is_resource_sufficient(drink["ingredients"]):                                
            payment = process_coins()                                                   
            if transaction_successful(payment, drink["cost"]):                          
                make_coffee(choice, drink["ingredients"])                               
