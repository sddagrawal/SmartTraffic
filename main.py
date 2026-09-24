#road class def
class RoadDirection:

    def __init__(self,dirc,vehicles,wait_time,emergency):
        self.dirc=dirc
        self.vehicles=vehicles
        self.wait_time=wait_time
        self.emergency=emergency

    def calculate_priority(self):
        emergency_bonus =100 if self.emergency else 0
        priority_score=((self.vehicles*2)+(self.wait_time*0.5)+ emergency_bonus )
        return priority_score

    def check_congestion(self):
        #if vehicle number or wait time exceeds threshold
        if self.vehicles>20 or self.wait_time>60:
            return "congested"
        else:
             return "normal"

#1
def get_traffic_data():
    directions= ["north","south","east","west"]
    road_objects=[]

    print("\n--- Enter traffic data for each direction ---")
    
    for dirc in directions:
        print(f"\n>>> Input for {dirc} directiomn:")
        
        #(1) valid vehicle count
        while True:
            try:
                vehicles= int (input(f"enter number of vehicles in {dirc}:"))
                if vehicles<0:
                    print("count can not be negative!!")
                    continue
                break
            except ValueError:
                print("enter valid numeric value")
        
        #(2) valid waiting time
        while True:
            try:
                wait_time=float(input(f"enter waiting time (sec) for {dirc}"))
                if wait_time<0:
                    print("wait time can not be negative!!")
                    continue
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
        
        #creating a RoadDirection object and storing it
        road = RoadDirection(dirc,vehicles,wait_time,emergency)
        road_objects.append(road)
    return road_objects

"""#testing 
if __name__=="__main__":
    traffic_data= get_traffic_data()

    print("\n--- collected data ---")
    for road in traffic_data:
        print(f"{road.dirc}:{road.vehicles} vehicles, {road.wait_time}s wait, emergency: {road.emergency}")
        """


"""#testing 
if __name__== "__main__":
    traffic_data= get_traffic_data()

    print ("/n--- priority and congestion ---")
    for road in traffic_data:
        score= road.calculate_priority()
        status=road.check_congestion()
        print(f"{road.dirc} : priority score= {score}, status={status}")"""



#2
def allocate_green_times(road_list, total_cycle_time=120, min_time=10):
    #calculating priority score
    total_priority= sum(road.calculate_priority() for road in road_list)

    remaining_pool= total_cycle_time-(min_time*len(road_list))

    alloacted_times={}

    for road in road_list:
        score= road.calculate_priority()
        if total_priority>0:
            extra_time=(score/ total_priority)* remaining_pool
            green_time= min_time+ extra_time

        else:
            #case of empty intersection
            green_time=total_cycle_time/ len (road_list)

        #rounding off
        alloacted_times[road.dirc]= round(green_time)

    return alloacted_times

def get_signal_schedule (road_list):
    #sorting priority using lambda
    sorted_roads= sorted(road_list, key=lambda road:road.calculate_priority() , reverse=True)
    return sorted_roads

"""#testing 
if __name__= "__main__":
    traffic_data= get_traffic_data()

    #for green light
    green_times= alloacted_times(traffic_data)
    #for order of traffic signals
    scheduled_roads= get_signal_schedule(traffic_data)

    print("\n--- signal schedule and allocation ---")
    for rank, road in enumerate (scheduled_roads:1):
        dirc_name= road.dirc.capitalize()
        priority= road.calculate_priority()
        allocated_sec= green_times[road.dirc]
        emergency_tag= "[emergency]" if road.emergency else ""

        print (f"Order{rank}: {dirc_name} {emergency_tag} --> priority: {priority} --> green time : {allocated_sec} s")"""
    
        
#3
def calculate_performance(road_list, alloacted_times, standard_fixed_time=30):
    fixed_total_wait= sum (road.vehicles*road.wait_time for road in road_list)

    if fixed_total_wait==0:
        return 0.0,0.0,0.0

    optimized_total_wait=0
    for road in road_list:
        green= alloacted_times[road.dirc]
        time_factor= standard_fixed_time/ green if green>0 else 1.0 
        optimized_total_wait+=road.vehicles*(road.wait_time*time_factor)

    improvement=((fixed_total_wait- optimized_total_wait)/ fixed_total_wait)*100
    return(round (fixed_total_wait, 1),round(optimized_total_wait,1),round (improvement,2),)

#4
if __name__ == "__main__":
    while True:
        traffic_data= get_traffic_data()

        green_times= allocate_green_times(traffic_data)
        scheduled_roads= get_signal_schedule(traffic_data)

        fixed_wait, opt_wait, improvement = calculate_performance(traffic_data, green_times)

        print ("#SMART TRAFFIC SIGNAL FINAL REPORT#")

        print("\n ---- signal order and allocation ----")
        for rank, road in enumerate (scheduled_roads,1):
            dirc_name= road.dirc.capitalize()
            priority=road.calculate_priority()
            status=road.check_congestion()
            emergency_tag= "[EMERGENCY]" if road.emergency else ""
            
            allocated_sec = green_times[road.dirc]
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
        
        


        