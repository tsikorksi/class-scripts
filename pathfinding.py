

def min_finder(distance, unvisited, nodes, flag, heuristics):
    """
    finds min of all nodes that are also in unvisited
    :param distance:  the array containing distances
    :param unvisited: the unvisited nodes
    :param nodes: all nodes keys
    :param flag: if true, use heuristics to calculate the minimum
    :param heuristics: the heuristics which need to be accounted for if flag is raised
    :return: the lowest value in distance whose key equivalent in nodes is in unvisited
    """
    if heuristics is None and flag is True:
        raise Exception("Flag is True, but there are no heuristics available for calculation, please check input")
    temp = 999999
    value = ''
    for i in range(0, len(distance)):
        if distance[i] < temp and nodes[i] in unvisited:
            value = nodes[i]
            if flag:
                temp = distance[i] + heuristics[i]
            else:
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
    # for example, the index 0 in every list refers to the same node

    # fills distance and previous with the default values
    for i in range(0, len(graph)):
        distance.append(999999)
        previous.append('')

    # sets the start nodes distance to 0, to kickstart algorithm
    distance[nodes.index(start)] = 0

    return nodes, unvisited, distance, previous


def heuristics_setup(nodes, heuristics_in):
    """
    transforms the heuristics dict into a list which matches up against the existing structure
    :param nodes: the nodes list generated for the graph
    :param heuristics_in: the dict supplied
    :return: the list of heuristics matched to the nodes
    """
    heuristics = []
    for i in range(0, len(nodes)):
        heuristics.append(heuristics_in[nodes[i]])
    return heuristics


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
        current_node = min_finder(distance, unvisited, nodes, False, None)

        unvisited.remove(current_node)

        # key: the char for the values in the sub-dict graph[current_node], dist is the associated distance
        for key, dist in graph[current_node].items():
            # the possible shorter distance
            alternate = distance[nodes.index(current_node)] + dist
            # checks if the new distance is quicker the the recorded one
            if alternate < distance[nodes.index(key)]:
                # replaces the distance in the list if so
                distance[nodes.index(key)] = alternate
                # replaces the last values in the previous list with the node travelled from
                previous[nodes.index(key)] = current_node

    return parser(nodes, previous, start, end), distance[nodes.index(end)]


def a_star(graph, heuristics, start, end):
    """
    A* search algorithm, which calculates the shortest distance between 2 nodes considering the heuristic values
    :param graph: the graph to be searched
    :param heuristics: the dict containing the heuristics for all the nodes
    :param start: the start node
    :param end: the destination
    :return: the route to the end node and the distance
    """
    nodes, unvisited, distance, previous = list_setup(graph, start)
    heuristics = heuristics_setup(nodes, heuristics)

    # until unvisited is empty or the destination node has been visited
    while unvisited or end in unvisited:
        # the key for the min value in unvisited
        current_node = min_finder(distance, unvisited, nodes, True, heuristics)

        unvisited.remove(current_node)

        # key: the char for the values in the sub-dict graph[current_node], dist is the associated distance
        for key, dist in graph[current_node].items():

            # the possible shorter distance, with heuristics accounted for
            alternate_calc = distance[nodes.index(current_node)] + dist + heuristics[nodes.index(key)]
            print(current_node, key, heuristics[nodes.index(key)], alternate_calc)
            # checks if the new distance is quicker the the recorded one

            if alternate_calc < distance[nodes.index(key)]:
                # the actual distance , without heuristics
                alternate = distance[nodes.index(current_node)] + dist
                # replaces the distance in the list if so
                distance[nodes.index(key)] = alternate
                # replaces the last values in the previous list with the node travelled from
                previous[nodes.index(key)] = current_node

    return parser(nodes, previous, start, end), distance[nodes.index(end)]
