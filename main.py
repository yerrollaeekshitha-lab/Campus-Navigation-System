import heapq

# -----------------------------
# CAMPUS MAP (Graph)
# -----------------------------
campus_graph = {
    "Gate": {
        "Library": 4,
        "Cafeteria": 2
    },
    "Library": {
        "Gate": 4,
        "Lab": 3,
        "Admin": 5
    },
    "Cafeteria": {
        "Gate": 2,
        "Lab": 4
    },
    "Lab": {
        "Library": 3,
        "Cafeteria": 4,
        "Classroom": 2
    },
    "Admin": {
        "Library": 5,
        "Classroom": 3
    },
    "Classroom": {
        "Lab": 2,
        "Admin": 3
    }
}

# -----------------------------
# HEURISTIC VALUES
# -----------------------------
heuristic = {
    "Gate": 7,
    "Library": 5,
    "Cafeteria": 6,
    "Lab": 2,
    "Admin": 3,
    "Classroom": 0
}

# -----------------------------
# A* SEARCH ALGORITHM
# -----------------------------
def a_star(graph, heuristic, start, goal):

    open_list = []
    heapq.heappush(open_list, (0, start))

    came_from = {}

    g_cost = {}
    for node in graph:
        g_cost[node] = float('inf')

    g_cost[start] = 0

    trace = []
    nodes_expanded = 0

    while open_list:

        current_f, current = heapq.heappop(open_list)

        trace.append(f"Visited Node: {current}")
        nodes_expanded += 1

        if current == goal:

            path = []

            while current in came_from:
                path.append(current)
                current = came_from[current]

            path.append(start)
            path.reverse()

            return path, g_cost[goal], trace, nodes_expanded

        for neighbor, cost in graph[current].items():

            new_cost = g_cost[current] + cost

            if new_cost < g_cost[neighbor]:

                came_from[neighbor] = current
                g_cost[neighbor] = new_cost

                f_cost = new_cost + heuristic[neighbor]

                heapq.heappush(open_list, (f_cost, neighbor))

    return None, None, trace, nodes_expanded


# -----------------------------
# MAIN PROGRAM
# -----------------------------
print("=" * 50)
print("      AI CAMPUS NAVIGATION SYSTEM")
print("=" * 50)

print("\nAvailable Locations:")

for location in campus_graph.keys():
    print("•", location)

start = input("\nEnter Starting Location: ")
goal = input("Enter Destination Location: ")

if start not in campus_graph:
    print("\nInvalid Starting Location!")
    exit()

if goal not in campus_graph:
    print("\nInvalid Destination Location!")
    exit()

path, distance, trace, nodes = a_star(
    campus_graph,
    heuristic,
    start,
    goal
)

print("\n" + "=" * 50)

if path:

    print("OPTIMAL PATH FOUND")
    print("=" * 50)

    print("\nRoute:")
    print(" -> ".join(path))

    print("\nTotal Distance:")
    print(distance)

    print("\nNodes Expanded:")
    print(nodes)

    print("\nSearch Trace:")
    for step in trace:
        print(step)

else:
    print("No Path Found!")

print("\n" + "=" * 50)
print("Project: Campus Navigation System")
print("Algorithm Used: A* Search")
print("=" * 50)