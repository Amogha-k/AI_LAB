import heapq

example_map= {
    'S':{'A':1,'G':10},
    'A':{'B':2,'C':1,'S':1},
    'B':{'D':5,'A':2},
    'C':{'A':1,'D':3,'G':4},
    'D':{'B':5,'C':3,'G':2},
    'G':{'S':10,'C':4,'D':2},
}
heuristics = {
    'S':5,
    'A':3,
    'B':4,
    'C':2,
    'D':6,
    'G':0
}

def a_star_search(graph,start,goal,heuristics):
    open_list=[(0,start)]
    closed_list=set()
    
    g_score={location: float('inf') for location in graph}
    g_score[start]=0
      
    while open_list:
        current_g,current_node=heapq.heappop(open_list)
        if current_node==goal:
            return g_score[goal]
        if current_node in closed_list:
            continue
        
        closed_list.add(current_node)
        
        for neibour,distance in graph[current_node].items():
            tentative_g=g_score[current_node]+distance
            
            if tentative_g <g_score[neibour]:
                g_score[neibour]=tentative_g
                f_score=tentative_g+heuristics[neibour]
                heapq.heappush(open_list,(f_score,neibour))
    return float('inf')

start_location='S'
goal_location='G'
shortest_distance=a_star_search(example_map,start_location,goal_location,heuristics)

if shortest_distance < float('inf'):
    print(f"The shortest distance from {start_location} to {goal_location} is {shortest_distance} km.")
else:
    print(f"No path found from {start_location} to {goal_location}.")