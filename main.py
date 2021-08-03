from queue import PriorityQueue
from utils import Node, read_input
from constants import INF

class MetroPath:
    def __init__(self, n_station, colors, connections, start_station, end_station, metro_color):
        self.nodes = [Node(x, colors[x]) for x in range(n_station)] # nodes created
        self.build_network(connections)
        self.start_station = start_station
        self.end_station = end_station
        self.metro_color = metro_color

    def build_network(self, connections):
        for station1, station2 in connections:
            self.nodes[station1].neighbors.add(station2) # add to adj list
            self.nodes[station2].neighbors.add(station1) # add to adj list

    def get_edge_weight(self, color_station):
        """
        Return 1 if the metro stops in the next station, 0 otherwise
        """
        if self.metro_color == "*" or color_station == "*": # metro stops 
            return 1
        elif self.metro_color == color_station: # metro stops 
            return 1
        return 0 # no stop

    def dijkstra(self):
        """
        Dijkstra algorithm, single source shortest path.
        """
        distances = [INF for _ in range(len(self.nodes))] 
        distances[self.start_station] = 0 
        priority_queue = PriorityQueue() 
        priority_queue.put((0, self.start_station))
        while len(priority_queue.queue):
            dist, station = priority_queue.get()
            if distances[station] < dist: # outdated improvement
                continue
            for adj_station in self.nodes[station].neighbors: # visit every neighbour
                weight = self.get_edge_weight(self.nodes[adj_station].color) # here we calculate the edge weight
                if distances[adj_station] > dist + weight: # found a better path
                    distances[adj_station]  = dist + weight
                    self.nodes[adj_station].parent = station
                    priority_queue.put((distances[adj_station], adj_station))

    def get_path_solution(self):
        """
        Generate the path solution
        """
        route = []
        current_station = self.end_station
        while current_station != -1:
            if not ((self.nodes[current_station].color == "R" and self.metro_color == "V") or (self.nodes[current_station].color == "V" and self.metro_color == "R")): # if the metro does not stop in this station, do not add it to the path
                route.append(current_station)
            current_station = self.nodes[current_station].parent
        route.reverse()
        return route

    def print_solution(self, route):
        """
        Shows the solution path
        """
        if self.metro_color != '*' and self.nodes[self.start_station].color != '*' and self.metro_color != self.nodes[self.start_station].color:
            print("No es posible subir al metro")
        elif self.metro_color != '*' and self.nodes[self.end_station].color != '*' and self.metro_color != self.nodes[self.end_station].color:
            print("No es posible bajar del metro")
        elif not route or route[0] != self.start_station: 
            print("No existe ruta válida")
        else:
            print("Se ha encontrado la ruta más corta:")
            for i in range(len(route)):
                if i: print("->", end=" ")
                print(route[i]+1, end=" ")

    

if __name__ == "__main__":
    n_station, colors, connections, start_station, end_station, metro_color = read_input()
    metro_path = MetroPath(n_station, colors, connections, start_station, end_station, metro_color)
    metro_path.dijkstra()
    route = metro_path.get_path_solution()
    metro_path.print_solution(route)

