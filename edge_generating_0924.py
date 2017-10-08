from random import uniform
from random import randint
from random import shuffle

def main(args):

    num_of_rooms = int(uniform(8, 13))
    map_matrix = [[0 for dest in range(orig+1)] for orig in range(num_of_rooms)]
    edge_dict = {r : 0 for r in range(num_of_rooms)} # room # : edge_count
    target_num_of_edges = 0                          # record the requirement for a target/destination room
    
    print("start...")
    print('num of rooms:',num_of_rooms)
    
    rand_rooms = list(edge_dict.keys())
    shuffle(rand_rooms)          # list of rooms in random order
    
    for r in rand_rooms:
        edges_to_build = randint(1,3)              
        print('room ',r, 'is looking for',edges_to_build,'new edges')
        while edges_to_build > 0:
            for dest, edge_count in edge_dict.items():
                if (r != dest) and (edge_count == target_num_of_edges):
                    if r > dest:
                        x,y = r, dest
                    else:
                        x,y = dest, r
                    edge_dict[x] += 1          #increment its edge count
                    edge_dict[y] += 1
                    map_matrix[x][y] = 1
                    edges_to_build -= 1
                    
                if edges_to_build <= 0:
                    break                 
            target_num_of_edges += 1
        target_num_of_edges = 1         #reset the requirement to 1, 
                                        #so that the next room will be connected to a connected graph for sure
    
    print('\nresult:')
    for x in range(num_of_rooms):
        for y in range(len(map_matrix[x])):
            print(map_matrix[x][y],end = ' ')
        print()

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
