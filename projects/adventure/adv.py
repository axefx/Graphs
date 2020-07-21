from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

from util import Graph, Stack, Queue

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

def bfs(starting_room, g):
    explored = set()
    q = Queue() # used for finding next direction
    q.enqueue([]) 
    while q.size() > 0:
        path = q.dequeue()
        next_room = starting_room
        for directions in path:
            next_room = next_room.get_room_in_direction(directions)
        
        if next_room:
            for exits in next_room.get_exits():
                next_path = path[:]
                next_path.append(exits)
                if g[next_room.id][exits] == '?':
                    return (next_path)
                if (next_room, exits) not in explored:
                    q.enqueue(next_path)
                explored.add((next_room, exits))

opposite = {
    'n': 's',
    's': 'n',
    'e': 'w',
    'w': 'e'
}
g = {} # {0: { 's': '?', 'n': 1}}
path = [] # traversal path
starting_direction = 'n' # start with s or random
visited = set()
while len(visited) < len(world.rooms):
    room = player.current_room
    room_id = room.id
    all_exits = room.get_exits()

    if room_id not in g:
        g[room_id] = {direction: '?' for direction in all_exits}
    next_path = bfs(room, g)
    if not next_path: # or len(next_path) == 0:
        path = path
        break
    for direction in next_path:
        next_room = room.get_room_in_direction(direction)
        visited.add(next_room)
        g[room_id][direction] = next_room.id
        if next_room.id not in g:
            g[next_room.id] = {direction: '?' for direction in next_room.get_exits()}
        path.append(direction)
        player.travel(direction)
        g[next_room.id][opposite[direction]] = room_id
        room = next_room

# def bfs(starting_room, g):
#     explored = set()
#     q = Queue() # used for finding next direction
#     q.enqueue([]) 
#     # While the queue is not empty...
#     while q.size() > 0:
#         print(q.queue)
#         path = q.dequeue()
#         print(f"starting_room: {starting_room.id}")
#         next_room = starting_room
#         print(f"next_room: {next_room.id}")
#         print(path)
#         for directions in path:
#             print(directions)
#             print(player.current_room.id)
#             next_room = next_room.get_room_in_direction(directions)
#             print(next_room)
        
#         print(f"next_room: {next_room}")
#         # if next_room.id not in g:
#         #     g[next_room.id] = {direction: '?' for direction in next_room.get_exits()}
#         # Then add A PATH TO its neighbors to the back of the queue
#         if next_room:
#             print(f"next_room: {next_room.id}")
#             for exits in next_room.get_exits():
#                 print(f"exits: {exits}")
#                 # COPY THE PATH
#                 next_path = path[:]
#                 # APPEND THE NEIGHBOR TO THE BACK
#                 next_path.append(exits)
#                 # CHECK IF IT'S THE TARGET
#                 print(f"g: {g}")
#                 if g[next_room.id][exits] == '?':
#                     print("found ?")
#                     print(g)
#                     # IF SO, RETURN PATH
#                     return (next_path)
#                 print(f"g[next_room.id][exits]: {g[next_room.id][exits]}")
#                 if (next_room, exits) not in explored:
#                     print("not in explored")
#                     q.enqueue(next_path)
#                 # If that vertex has not been visited...
#                     # Mark it as visited...
#                 explored.add((next_room, exits))

# opposite = {
#     'n': 's',
#     's': 'n',
#     'e': 'w',
#     'w': 'e'
# }
# g = {} # {0: { 's': '?', 'n': 1}}
# visited = set() # add player current room in before moving
# located = {} # {0: [], 1: ['n']}}
# path = [] # traversal path
# starting_direction = 'n' # start with s or random
# s = Stack() # used for walking player
# s.push(starting_direction)
# # create graph 
# # while len(visited) < len(world.rooms):
# while True:
#     print(f"len(visited): {len(visited)}")
#     room = player.current_room
#     room_id = room.id
#     all_exits = room.get_exits()

#     print(f"player location: {player.current_room.id}")
#     # this adds players currentroom id indexing a dictionary of
#     # {posible moves: '?'} to graph
#     if room_id not in g:
#         g[room_id] = {direction: '?' for direction in all_exits}
#     next_path = bfs(room, g)
#     print(f"bfs: {next_path}")
#     if not next_path: # or len(next_path) == 0:
#         print("no next path")
#         print(f"path: {path}")
#         path = path
#         break
#     print(f"next_path: {next_path}")
#     # visited.add(room_id)
#     # print(f"visited: {visited}")
#     for direction in next_path:
#         next_room = room.get_room_in_direction(direction)
#         g[room_id][direction] = next_room.id
#         if next_room.id not in g:
#             g[next_room.id] = {direction: '?' for direction in next_room.get_exits()}
#         path.append(direction)
#         player.travel(direction)
#         g[next_room.id][opposite[direction]] = room_id
#         room = next_room
    
print('_____'*2*8)
print(f"len(world.rooms): {len(world.rooms)}")
print(f"path: {path}")
print(f"g: {g}")
traversal_path = path




# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
