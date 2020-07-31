from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

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
def reverse_direction(direction):
    if direction == "n":
        return "s"
    elif direction == "s":
        return "n"
    elif direction == "e":
        return "w"
    elif direction == "w":
        return "e"
    else:
        return None

def add_to_visited(room_in, next_room, direction, visited):
    visited[room_in.id][direction] = next_room.id

    if next_room.id not in visited:
        visited[next_room.id] = {}

    visited[next_room.id][reverse_direction(direction)] = room_in.id

def generate_path(p):
    visited = {}
    path = []
    while len(visited) != len(room_graph):
        curr_room = p.current_room
        if curr_room.id not in visited:
            visited[curr_room.id] = {}

        exits = curr_room.get_exits()
        unvisited_exits = [e for e in exits if e not in visited[curr_room.id]]

        if len(unvisited_exits) == 0:
            pass    
        else:
            direction = random.choice(unvisited_exits)
            p.travel(direction)
            next_room = p.current_room

            path.append(direction)
            add_to_visited(curr_room, next_room, direction, visited)

    return path

# traversal_path = ['n', 'n']
traversal_path = []



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
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")
