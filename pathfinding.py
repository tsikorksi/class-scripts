
def min_finder(distance, unvisited, nodes):
    """
    finds min of all nodes that are also in unvisited
    :param distance:  the array containing distances
    :param unvisited: the unvisited nodes
    :param nodes: all nodes keys
    :return: the lowest value in distance whose key equivalent in nodes is in unvisited
    """
    temp = 999999
    value = ''
    for i in range(0, len(distance)):
        if distance[i] < temp and nodes[i] in unvisited:
            value = nodes[i]
            temp = distance[i]
    return value


def parser(nodes, previous, start, end):
    """
    takes the calculated values and works out the full route
    :param nodes: the list of nodes
    :param previous: the master node for each node
    :param start: the root node
    :param end: the destination node
    :return: the final route
    """
    done = False
    route = end
    while not done:
        # adds the node that came before the later one to the total route
        route = previous[nodes.index(route[0])] + route
        # once the start node has been added, the loop ends
        if route[0] == start:
            done = True
    return route


def list_setup(graph, start):
    """
    generates and sets up the initial buffers
    :param graph: the graph calculating for
    :param start: the initial node
    :return: the 4 buffers which are used to calculate the route, with their initial states filled
    """
    # list of all nodes, does not change
    nodes = list(graph.keys())
    # list of unvisited nodes, will be emptied as we go
    unvisited = list(graph.keys())
    # list of distances to a node
    distance = []
    # list of routes to each node
    previous = []

    # note that distance, nodes and previous use the same indexes, and are equivalent to 1 list

    # fills distance and previous with the default values
    for i in range(0, len(graph)):
        distance.append(999999)
        previous.append('')

    # sets the start nodes distance to 0, to kickstart algorithm
    distance[nodes.index(start)] = 0

    return nodes, unvisited, distance, previous


def dijkstra(graph, start, end):
    """
    Dijkstra's algorithm solver
    :param graph: the graph to be solved
    :param start: the start node
    :param end: the destination node
    :return: the route from start to end and that distance
    """
    nodes, unvisited, distance, previous = list_setup(graph, start)

    # until unvisited is empty
    while unvisited:
        # the key for the min value in unvisited
        u = min_finder(distance, unvisited, nodes)

        unvisited.remove(u)

        # key: the char for the values in the sub-dict graph[u], dist is the associated distance
        for key, dist in graph[u].items():
            # the possible shorter distance
            alternate = distance[nodes.index(u)] + dist
            # checks if the new distance is quicker the the recorded one
            if alternate < distance[nodes.index(key)]:
                # replaces the distance in the list if so
                distance[nodes.index(key)] = alternate
                # replaces the last values in the previous list with the node travelled from
                previous[nodes.index(key)] = u

    return parser(nodes, previous, start, end), distance[nodes.index(end)]


def a_star(graph, heuristics, start, end):
    return ()
