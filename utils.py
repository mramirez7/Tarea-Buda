def read_input():
    """
    Reads the input file
    """    
    n_station, n_connections = [int(x) for x in input().split()] # read number of stations and number of connections
    colors = input().split() # read colors 
    connections = []
    for _ in range(n_connections):
        station1, station2 = [int(x)-1 for x in input().split()] # read edge
        connections.append((station1, station2)) # save the edge
    start_station, end_station = [int(x)-1 for x in input().split()] # read start station and end station
    metro_color = input().strip() # read the metro color
    return n_station, colors, connections, start_station, end_station, metro_color 

class Node():
    def __init__(self, id, color):
        self.id = id
        self.color = color
        self.neighbors = set()
        self.parent = -1



