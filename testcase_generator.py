from random import randint

n_stations = randint(3,10) # number of stations
n_connections = randint(n_stations-1, n_stations*(n_stations-1)//2)
colors = "RV*" # red, green, no color

station_colors = [colors[randint(0,2)] for _ in range(n_stations)] # chooses randomly a color for each station

graph = [set() for _ in range(n_stations)]

# tree structure, so we can guaranteed the graph is connected
for station in range(1, n_stations):
    tree_station = randint(0, station-1) 
    graph[station].add(tree_station)
    graph[tree_station].add(station)

# add the rest of edges
for _ in range(n_connections - (n_stations-1)):
    while True:
        station1 = randint(0, n_stations-2)
        station2 = randint(station1+1, n_stations-1)
        if station1 not in graph[station2]: # this edge does not exist
            graph[station1].add(station2)
            graph[station2].add(station1)
            break

# print the graph
print(n_stations, n_connections)

#print colors
print(" ".join(station_colors))
#print connections
for i in range(n_stations):
    for station in graph[i]:
        if i < station:
            print(i+1, station+1)

start = randint(1, n_stations-1) 
end = randint(start+1, n_stations)
metro_color = colors[randint(0,2)]
print(start, end) # print start and end stations
print(metro_color) # print metro color
