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
map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

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

# keep running this while visited is lower than total room
# if the current room is not in visited
# add it to visited 
# if there is still a direction to go on
# move in that direction and pop it from hash
# if the new room is not in memory
# save the move to path
# save the movement
# move the player in that direction 
# if there are no new direction to go on
# go back to the previous room
# save the movement
# move the player

opposite = {
    'n': 's',
    's': 'n',
    'e': 'w',
    'w': 'e'
}
g = {} # {0: { 's': '?', 'n': 1}}
visited = set() # add player current room in before moving
located = {} # {0: [], 1: ['n']}}
path = [] # traversal path
starting_direction = 'n' # start with s or random
s = Stack() # used for walking player
s.push(starting_direction)
# create graph 
while len(visited) < len(world.rooms):
    print(f"len(visited): {len(visited)}")
    room = player.current_room
    room_id = room.id
    all_exits = room.get_exits()

    print(f"player location: {player.current_room.id}")
    # this adds players currentroom id indexing a dictionary of
    # {posible moves: '?'} to graph
    if room_id not in g:
        g[room_id] = {direction: '?' for direction in all_exits}
    def bfs(starting_room):
        explored = set()
        q = Queue() # used for finding next direction
        q.enqueue([starting_direction]) 
        # While the queue is not empty...
        while q.size() > 0:
            path = q.dequeue()
            direction = path[-1]
            next_room = player.current_room.get_room_in_direction(direction)
            if next_room.id not in g:
                g[next_room.id] = {direction: '?' for direction in next_room.get_exits()}
            # If that vertex has not been visited...
            print(g)
            if (next_room, direction) not in explored:
                # CHECK IF IT'S THE TARGET
                print(next_room.id,direction)
                if direction in g[next_room.id] and g[next_room.id][direction] == '?':
                    # IF SO, RETURN PATH
                    return (path, explored)
                # Mark it as visited...
                explored.add((next_room, direction))
            # Then add A PATH TO its neighbors to the back of the queue
            for exits in next_room.get_exits():
                # COPY THE PATH
                next_path = path[:]
                # APPEND THE NEIGHBOR TO THE BACK
                next_path.append(exits)
                q.enqueue(next_path)
        return None
    next_path, explored = bfs(room)
    print(f"next_path: {next_path}")
    visited.add(room_id)
    print(f"visited: {visited}")
    if next_path:
        for direction in next_path:
            g[room_id][direction] = room.get_room_in_direction(direction).id
            path.append(direction)
            player.travel(direction)
    print(f"player location: {player.current_room.id}")
    if len(visited) < 4:
        break
    # while q.size() > 0:
    #     path = q.dequeue()
    #     direction = path[-1]
    #     next_room = room.get_room_in_direction(direction)
    #     print(f"next_room: {next_room.id}")
    #     exits = next_room.get_exits()
    #     for direction in all_exits:
    #         next_path = path[:]
    #         next_path.append(direction)
    #         if g[room.id][direction] == '?':
    #             unexplored_path = next_path
    #         if (room, direction) not in visited:
    #             q.enqueue(next_path)
    #         visited.add((room, direction))

    # if unexplored_path is None or len(unexplored_path) == 0:
    #     print("no more")
    # for direction in unexplored_path:
    #     new_room = room.get_room_in_direction(direction)
    #     path.append(direction)
    #     if new_room:
    #         g[room.id][direction] = new_room.id
    #         if new_room.id not in g:
    #             g[new_room.id] = {direction: '?' for direction in all_exits}
    #         g[new_room.id][opposite[direction]] = room.id
    #         room = new_room
    # if len(visited) < 2:
    #     break
    # if next_room:
    #     next_room_id = next_room.id
    #     print(f"next_room: {next_room_id}")
    #     print(f"g: {g}")
    #     if next_room_id not in g:
    #         print(f"next_room.get_exits(): {next_room.get_exits()}")
    #         g[next_room_id] = {move: '?' for move in next_room.get_exits()}
        # add both room ids to graph
        # g[next_room_id][opposite[starting_direction]] = room_id
        # g[room_id][starting_direction] = next_room_id
    # print(f"g: {g}")
    # print(' - - '*2*8)
    

    # visited.add(room_id)

    # TODO handle movement
    # print(f"s.size(): {s.size()}")
    # print(f"s.stack: {s.stack}")
    # next_direction = s.pop()
    # print(f"next_direction: {next_direction}")
    # print(f"s.size(): {s.size()}")
    # next_room = player.current_room.get_room_in_direction(next_direction)
    # print(f"g: {g}")
    # print(f"visited: {visited}")
    # unexplored = []
    # for direction in player.current_room.get_exits():
    #     if g[player.current_room.id][direction] == '?':# and direction != next_direction:
    #         unexplored.append(direction)
    # print(f"unexplored: {unexplored}")
    # if next_direction in unexplored:
    #     print(f"next_direction in unexplored: {next_direction in unexplored}")
    #     if next_room.id in visited:
    #         print("next room visited")
    #     print(f"next_room.id: {next_room.id}")
    # print(f"player.current_room.id: {player.current_room.id}")
    # print(f"moving...")
    # path.append(starting_direction)
    # player.travel(starting_direction)
    # print(f"player.current_room.id: {player.current_room.id}")
        
    #     # print(f"next_direction: {next_direction}")
    #     s.push(next_direction)
    # # else:
    # if len(unexplored) > 0:
    #     print(f"unexplored: {unexplored}")
    #     print(f"unexplored: {unexplored[0]}")
    #     s.push(unexplored[-1])
    # else:
    #     print(f"going back")
    #     s.push(opposite[next_direction])

    # print(f"len(visited) after moving: {len(visited)}")
    # # print(f"len(world.rooms): {len(world.rooms)}")
    # print('loop_'*2*8)
    # if len(visited) == 2 or len(path) > 4:
    #     break

    # print(f"s.size(): {s.size()}")
    # print(f"s.stack: {s.stack}")
    # next_direction = s.pop()
    # print(f"next_direction: {next_direction}")
    # print(f"s.size(): {s.size()}")
    # next_room = player.current_room.get_room_in_direction(next_direction)
    # print(f"g: {g}")
    # print(f"visited: {visited}")
    # unexplored = []
    # for direction in player.current_room.get_exits():
    #     if g[player.current_room.id][direction] == '?':# and direction != next_direction:
    #         unexplored.append(direction)
    # print(f"unexplored: {unexplored}")
    # if next_direction in unexplored:
    #     print(f"next_direction in unexplored: {next_direction in unexplored}")
    #     if next_room.id in visited:
    #         print("next room visited")
    #     print(f"next_room.id: {next_room.id}")
    #     print(f"player.current_room.id: {player.current_room.id}")
    #     print(f"moving...")
    #     print(f"next_direction: {next_direction}")
    #     path.append(next_direction)
    #     player.travel(next_direction)
    #     print(f"player.current_room.id: {player.current_room.id}")
        
    #     # print(f"next_direction: {next_direction}")
    #     s.push(next_direction)
    # # else:
    # if len(unexplored) > 0:
    #     print(f"unexplored: {unexplored}")
    #     print(f"unexplored: {unexplored[0]}")
    #     s.push(unexplored[-1])
    # else:
    #     print(f"going back")
    #     s.push(opposite[next_direction])

    # print(f"len(visited) after moving: {len(visited)}")
    # print(f"len(world.rooms): {len(world.rooms)}")
    # print('_____'*2*8)
    # if len(visited) == 5 or len(path) > 4:
    #     break
print('_____'*2*8)
print(f"len(world.rooms): {len(world.rooms)}")
print(f"path: {path}")
print(f"located: {located}")
print(f"visited: {visited}")
print(f"g: {g}")
print(f"s: {s.stack}")
# traversal_path = path

# g = {}
# for i in range(len(world.rooms)):
#     g[world.rooms[i].id] = { exits:world.rooms[i].get_room_in_direction(exits).id for exits in world.rooms[i].get_exits()}

# visited = set()
# s = Stack()
# s.push(world.starting_room.id)
# while len(visited) is not len(g):
#     room_id = s.pop()
#     if room_id not in visited:
#         visited.add(room_id)
#         if len(g[room_id].keys()) > 1:
#             for direction in g[room_id]:
#                 traversal_path.append(direction)
#                 s.push(g[room_id][direction])

# visited = {}
# s = Queue()
# s.enqueue([world.starting_room.id])
# while s.size() > 0:
#     path = s.dequeue()
#     room_id = path[-1]
#     if room_id not in visited:
#         visited[room_id] = path
#         # traversal_path.append()
#         if len(g[room_id].keys()) == 1:
#             direction = world.rooms[room_id].get_exits()[0]
#             traversal_path.append(direction)
#             s.enqueue([g[room_id][direction]])
#         else:
#             for direction in g[room_id]:
#                 neighbor = g[room_id][direction]
#                 traversal_path.append(direction)
#                 s.enqueue([g[room_id][direction]])

            # next_path = path[:]

            # neighbor_id = g[room_id][direction]
            # next_path.append(neighbor_id)
            # s.enqueue(next_path)
        # if len(g[neighbor_id]) == 1 and neighbor_id not in visited:
        #     traversal_path.append([direction,g[]])
        #     visited.add(g[room_id][direction])
            # s.push(g[room_id][direction])


# print(f"visited: {visited}")
# path = list(visited.keys())
# next_room = {path[i]: path[i+1] for i in range(len(path)-1)}
# print(next_room)
# s = Stack()
# walked = set()
# for i in visited:
#     s.push(i)
#     while s.size() > 0:
#         current_room = s.pop()
#         directions = list(g[current_room].keys())
#         for move in directions:
#             if g[current_room][move] == next_room[current_room]:

    

# directions = {}
# for i in range(len(world.rooms)):
#     directions[world.rooms[i].id] = { world.rooms[i].get_room_in_direction(exits).id: exits for exits in world.rooms[i].get_exits()}
# path = list(visited.keys())
# next_id = {path[i]: path[i+1] for i in range(len(path)-1)}

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
