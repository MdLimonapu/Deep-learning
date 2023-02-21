import random

start_dict = dict([
    ("Truck_A", 210),
    ("Truck_B", 100),
    ("Truck_C", 220),
    ("Truck_D", 120),
    ("Truck_E", 50)
])


Trucks = list(start_dict.keys())


lead_truck = max(start_dict, key=start_dict.get)
max_distance = start_dict[lead_truck]

avg_speed_kmph = 50

truck_time = dict()

#Timing for truck
for truck in Trucks:
    truck_time[truck]=start_dict[truck]/avg_speed_kmph


journey_duration = truck_time[lead_truck]


def reset_order(truck_dict):
    
    

    sorted_truck = {}
    sorted_keys = sorted(truck_dict, key=truck_dict.get, reverse=True)

    for key in sorted_keys:
        sorted_truck[key] = truck_dict[key]

    return sorted_truck



break_order = Trucks
random.shuffle(break_order)


"""
Case: one of the truck takes break and separates from the convoy for period of 30 mins (0.5 hours =30/60)

Truck C leaves (leading truck)
"""

break_period = 0.5

def case_break_time(break_period, start_dict, time):

    journey_duration=time 
    break_count= 1
    print("Platoon: ", start_dict)
    temp_new_order=reset_order(start_dict)
    print("Reset Platoon: ", temp_new_order)


    while journey_duration > 0:
        print("Duration remaining: " + str(journey_duration) + "  Truck Order: ", temp_new_order)
        print("Break No: ", break_count)
        #temp_new_order=reset_order(temp_new_order)
        random.shuffle(break_order)
        removed_truck = break_order[0]
        print(removed_truck + " leaves for break")
        temp_new_order.pop(removed_truck)
        #temp_new_order[removed_truck] = 0
        temp_new_order=reset_order(temp_new_order)
        print("Duration remaining: " + str(journey_duration) + "  Truck Order: ", temp_new_order)
        print("\n")
        print("Break Over")
        journey_duration = journey_duration-break_period
        temp_new_order.update({removed_truck: start_dict[removed_truck]})
        print("Duration remaining: " + str(journey_duration) + "  Truck Order: ", temp_new_order)
        print("\n")
        temp_new_order=reset_order(temp_new_order)
        break_count=break_count+1


case_break_time(break_period, start_dict, journey_duration)
