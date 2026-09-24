#begin
def calculate_priority(road):
    emergency_bonus =100 if road["emergency"] else 0
    priority_score=(road["vehicles"]*2)+(road["wait_time"]*0.5)+ emergency_bonus 
    return priority_score

def check_congestion(road):
    #if vehicle number or wait time exceeds threshold
    if road["vehicles"]>20 or road["wait_time"]>60:
        return "congested"
    else:
            return "normal"

#1
def get_traffic_data():
    directions= ["north","south","east","west"]
    road_objects=[]

    print("\n--- Enter traffic data for each direction ---")
    
    for dirc in directions:
        print(f"\n>>> Input for {dirc} direction:")
        
        #(1) valid vehicle count
        while True:
            try:
                vehicles= int (input(f"enter number of vehicles in {dirc}:"))
                break
            except ValueError:
                print("enter valid numeric value")
        
        #(2) valid waiting time
        while True:
            try:
                wait_time=float(input(f"enter waiting time (sec) for {dirc}"))
                break
            except ValueError:
                print ("please enter a valid number as input")

         #(3 ) presence of emergency vehicles
        while True:
            emergency_input=(input(f"Is there an emergency vehicle(S) in {dirc}? (yes/no):").strip().lower())
            if emergency_input in ["yes","y"]:
                emergency =True
                break
            elif emergency_input in ["no","n"]:
                emergency =False
                break
            else:
                print("invalid input!! please type 'yes' or 'no'")
        
        #storing data 
        road_objects.append({"dirc": dirc, "vehicles": vehicles, "wait_time":wait_time, "emergency":emergency})
    return road_objects

#2
def allocate_green_times(road_list, total_cycle_time=120, min_time=10):
    #calculating priority score
    total_priority= sum(calculate_priority(road) for road in road_list)

    remaining_pool= total_cycle_time-(min_time*len(road_list))

    alloacted_times={}

    for road in road_list:
        score= calculate_priority(road)
        if total_priority>0:
            extra_time=(score/ total_priority)* remaining_pool
            green_time= min_time+ extra_time

        else:
            #case of empty intersection
            green_time=total_cycle_time/ len (road_list)

        #rounding off
        alloacted_times[road["dirc"]]= round(green_time)

    return alloacted_times

def get_signal_schedule (road_list):
    #sorting priority using lambda
    sorted_roads= sorted(road_list, key=lambda road:calculate_priority(road) , reverse=True)
    return sorted_roads

    
        
#3
def calculate_performance(road_list, alloacted_times, standard_fixed_time=30):
    fixed_total_wait= sum (road["vehicles"]*road["wait_time"] for road in road_list)

    if fixed_total_wait==0:
        return 0.0,0.0,0.0

    optimized_total_wait=0
    for road in road_list:
        green= alloacted_times[road["dirc"]]
        time_factor= standard_fixed_time/ green if green>0 else 1.0 
        optimized_total_wait+=road["vehicles"]*(road["wait_time"]*time_factor)

    improvement=((fixed_total_wait- optimized_total_wait)/ fixed_total_wait)*100
    return(round (fixed_total_wait, 1),round(optimized_total_wait,1),round (improvement,2),)

#4
while True:
    traffic_data= get_traffic_data()

    green_times= allocate_green_times(traffic_data)
    scheduled_roads= get_signal_schedule(traffic_data)

    fixed_wait, opt_wait, improvement = calculate_performance(traffic_data, green_times)

    print ("#SMART TRAFFIC SIGNAL FINAL REPORT#")

    print("\n ---- signal order and allocation ----")
    for rank, road in enumerate (scheduled_roads,1):
        dirc_name= road["dirc"].capitalize()
        priority=calculate_priority(road)
        status=check_congestion(road)
        emergency_tag= "[EMERGENCY]" if road["emergency"] else ""
        
        allocated_sec = green_times[road["dirc"]]
        print(f"order {rank}: {dirc_name:<7}{emergency_tag} --> priority: {priority:<5} --> status: {status:<9} --> green time: {allocated_sec}s")
        
    print("\n--- system performance comparison ---")
    print(f"fixed system total wait delay: {fixed_wait}s")
    print(f"optimized system total wait : {opt_wait}s")
    print(f"efficiency improvement: {improvement}%")
 #5
    repeat= (input ("\n do you want to run another simulation? yes/no:").strip().lower())
    if repeat not in ["yes","y"]:
        print("\nexiting")
        break

    


        