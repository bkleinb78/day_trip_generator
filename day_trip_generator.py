import random

destination_list = ['LA', 'Chicago', 'New Orleans', 'Las Vegas']
transportation_list = ['airplane', 'car', 'train']
restaurant_list = ['McDonalds', 'Burger King', 'Longhorn Steak House', 'Wendys']
entertainment_list = ['circus', 'swimming', 'gambling', 'skydiving']

def list_loop(list):
    random_pick = random.choice(list)
    user_reply = input(f"Does {random_pick} sound like fun?! Are you Happy? (y/n):")
        
    if user_reply == "y":
        return random_pick 
    while user_reply == "n":
        if user_reply == "n":
            random_pick = random.choice(list)
            user_reply = input(f"What about {random_pick}? Is this ok? y/n:")
        if user_reply == "y":
            return random_pick
                
final_destination = list_loop(destination_list)
final_restaurant = list_loop(restaurant_list)
final_transportation = list_loop(transportation_list)
final_entertainment = list_loop(entertainment_list)

print("Welcome to Day Trip Generator, you are about to have a day trip generated for you!")

def day_trip(destination, restaurant, transportation, entertainment):
    
    satisfied = input("Are you happy with your choices? (y/n):")
   
    if satisfied == "y":
            print(f"You will be travelling to {destination} by {transportation}. You get to eat at {restaurant} and go {entertainment} for fun!")
    while satisfied == "n":
        change = input("Type 1 to change destination, 2 for restaurant, 3 for transportation or 4 for entertainment. Press 0 for no more changes: ").lower()
        if change == "1":
            destination = list_loop(destination_list)
        elif change == "2":
            restaurant = list_loop(restaurant_list)
        elif change == "3":
            transportation = list_loop(transportation_list)
        elif change == "4":
            entertainment = list_loop(entertainment_list)
        elif change == '0':
            satisfied = input("Are you satisfied with your choices? y/n:")
            print(f"You will be travelling to {destination} by {transportation}. You get to eat at {restaurant} and go {entertainment} for fun!")
            return

day_trip(final_destination,final_restaurant,final_transportation,final_entertainment)
