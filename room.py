import pygame
from random import uniform
from hunter import hunter

def generate_position():  # randomly generate the positions of objects, map is divided 12 * 7
    x = int(uniform(0, 13))
    y = int(uniform(0, 8))
    return [x, y]

def generate_map():
    #randomly generate 8-12 rooms, forming a connected graph
    room_num = int(uniform(8, 13))
    edges = []
    map_matrix = [[0 for j in range(i+1)] for i in range(room_num)]
    # a 'lower matrix', since it's a undirected graph
    # i always greater than j
    # vertex i and vertex j are not connected, '1' otherwise
    while True:
        i = int(uniform(0, room_num))
        j = int(uniform(0, room_num))
        if j == i: continue
        if j > i: i, j = j, i
        map_matrix[i][j] = 1
        edges.append((i, j))
        if is_connected(edges, room_num): break
    return map_matrix

def generate_environment():  # generate transmit, block, etc.
    map = generate_map()
    rooms = []
    for r in range(len(map)):
        rooms.append(room())
    transmits = []
    trans_relation_dict = {}  # key is starting point, value is end point
    for i in range(len(map)):
        for j in range(i+1):
            if map[i][j] == 1:
                temp_index = len(transmits)
                rooms[i].transmits.append(temp_index)
                transmits.append(transmit(*generate_position()))  # lack a check of repeated locations
                rooms[j].transmits.append(temp_index+1)
                transmits.append(transmit(*generate_position()))
                trans_relation_dict[rooms[i].transmits[-1]] = rooms[j].transmits[-1]
                trans_relation_dict[rooms[j].transmits[-1]] = rooms[i].transmits[-1]
    return [rooms, transmits, trans_relation_dict]

def is_connected(edges, vertex_num):  # BFS to check connectivity
    visited = {edges[0][0], edges[0][1]}
    temp_stack =  [edges[0][0], edges[0][1]]
    while temp_stack != []:
        temp = temp_stack.pop()
        for e in edges:
            if temp == e[0] and e[1] not in visited:
                visited.add(e[1])
                temp_stack.append(e[1])
            elif temp == e[1] and e[0] not in visited:
                visited.add(e[0])
                temp_stack.append(e[0])
    if len(visited) == vertex_num: return True
    else: return False

class room():
    def __init__(self):
        self.block_num = int(uniform(0, 16))
        self.breakable_num = int(uniform(0, 6))
        self.transmits = []  # storing the indexes of transmits in the transmit list
        self.blocks = []
        self.breakables = []

class transmit():
    def __init__(self, pos_x, pos_y):
        self.x_index = pos_x
        self.y_index = pos_y
        self.img = pygame.image.load("img/trans.png").convert_alpha()
    
    def transmitting(self, player):
        if self.status == True and 0.5 * player.width + 0.5 * self.width < hunter.get_distance(player):
            return [self.terminal.x_index, self.terminal.y_index]
        return None

class block():
    def __init__(self):
        pass

class breakable_block(block):
    pass

if __name__ == "__main__":
    test = generate_map()
    for t in test:
        print(t)
        print()