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
# world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

# add starting id to stack
# while the stack is not empty
# get id from stack
# mark as visited
# for each direction get the neighbor id
# if neighbor is a dead end and not visited## if len(neighbors direction) == 1
# add direction to and back in traversal_path
# mark neighbor as visited
#
# add neighbor id to stack
# add to visited 
# add direction to traversal path


g = {}
for i in range(len(world.rooms)):
    g[world.rooms[i].id] = { exits:world.rooms[i].get_room_in_direction(exits).id for exits in world.rooms[i].get_exits()}

visited = {}
s = Queue()
s.enqueue([world.starting_room.id])
while s.size() > 0:
    path = s.dequeue()
    room_id = path[-1]
    if room_id not in visited:
        visited[room_id] = path
        # traversal_path.append()

        for direction in g[room_id]:
            next_path = path[:]

            neighbor_id = g[room_id][direction]
            next_path.append(neighbor_id)
            s.enqueue(next_path)
        # if len(g[neighbor_id]) == 1 and neighbor_id not in visited:
        #     traversal_path.append([direction,g[]])
        #     visited.add(g[room_id][direction])
            # s.push(g[room_id][direction])


print(f"visited: {visited}")
# directions = {}
# for i in range(len(world.rooms)):
#     directions[world.rooms[i].id] = { world.rooms[i].get_room_in_direction(exits).id: exits for exits in world.rooms[i].get_exits()}
# path = list(visited.keys())
# next_id = {path[i]: path[i+1] for i in range(len(path)-1)}

go_back = {
    'n': 's',
    's': 'n',
    'e': 'w',
    'w': 'e'
}

room = {}
visited = set()
path = []

while len(visited) != len(room_graph):              # keep running this while visited is lower than total room
    roomId = player.current_room.id
    if roomId not in visited:                                       # if the current room is not in visited
        visited.add(roomId)                                           # add it to visited 
        directions = list(g[player.current_room.id].keys())
        room[roomId] = directions
    while len(room[roomId]) >= 0:                                  
        if len(room[roomId]) > 0:                                  # if there is still a direction to go on
            move = room[roomId].pop()                               # move in that direction and pop it from hash
            if g[roomId][move] not in visited:               # if the new room is not in memory
                path.append(move)                                                   #save the move to path
                traversal_path.append(move)              #save the movement
                player.travel(move)                                                # move the player in that direction 
                break
        elif len(room[roomId]) == 0:                                        # if there are no new direction to go on
            back_room = path.pop()                                       # go back to the previous room
            traversal_path.append(go_back[back_room])         #save the movement
            player.travel(go_back[back_room])                # move the player
            break

print(f"traversal_path: {traversal_path}")
####
# visited = set()
# visited.add(world.starting_room.id)

# current_room_id = world.starting_room.id
# total_rooms = len(world.rooms)

# while len(visited) < total_rooms:
#     moves = find_next_path(current_room_id, visited)
#     # Traverse the returned list of moves
#     for direction in moves:
#         player.travel(direction)
#         traversal_path.append(direction)
#         visited.add(player.current_room.id)
#     # update current room
#     current_room_id = player.current_room.id
###
####
# visited = []

# for _ in range(len(world.room_grid)):
#     visited.append([False] * len(world.room_grid[0]))

# island_count = 0

# s = Stack()
# for row in range(len(world.room_grid)):
#     for col in range(len(world.room_grid[0])):
#         s.push((row, col))
#         while s.size() > 0:
#             r, c = s.pop()
#             if not visited[r][c]:
#                 visited[r][c] = True
#                 # Traverse and mark each as visited
#                 # dft(row, col, islands, visited)
#                 # Increment counter
#                 island_count += 1
# print(visited)


# populate a graph with all the rooms
# do a breadth first traversal using a stack



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
