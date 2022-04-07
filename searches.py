from queue import Queue
import cleaner as clnr
import string
from collections import deque

class Node:
    def __init__(self):
        self.parent = ''
        self.children = {}
        self.path_cost = 0
        self.key = ''
        self.goal = False


def BFS(starting_node, dictionary, pairs_array, threshold):
    # init queue, graph
    q = Queue()
    g = {}
    start_NODE = Node()
    start_NODE.parent = starting_node
    start_NODE.path_cost = 0
    q.put(start_NODE)
    count = 1
    max_fringe = 0
    # identify node in que
    while not q.empty():
        if q.qsize() > max_fringe:
            max_fringe = q.qsize()

        temp_node = q.get()

        # check for goal
        if clnr.checker(temp_node.parent, dictionary) >= threshold:
            temp_node.goal = True
            g[count] = temp_node
            break
        else:
            t_be_added = clnr.apply_pairs(pairs_array, temp_node.parent)

            temp_node.children = t_be_added

            g[count] = temp_node
            count = count + 1

            # add the new nodes to the back of the qu
            for key in temp_node.children:
                add_node = Node()
                add_node.parent = temp_node.children[key]
                add_node.path_cost = temp_node.path_cost + 1
                add_node.key = temp_node.key + key.translate(str.maketrans('', '', string.punctuation))
                q.put(add_node)
        if len(g) >= 1000:
            break

    return g, max_fringe

def DFS (starting_node, dictionary, pairs_array, threshold):
    # init queue, graph
    q = deque()
    g = {}
    start_NODE = Node()
    start_NODE.parent = starting_node
    start_NODE.path_cost = 0
    q.append(start_NODE)
    count = 1
    max_fringe = 0
    # identify node in que
    while q:
        if len(q) > max_fringe:
            max_fringe = len(q)

        temp_node = q.popleft()

        # check for goal
        if clnr.checker(temp_node.parent, dictionary) >= threshold:
            temp_node.goal = True
            g[count] = temp_node
            break
        else:
            t_be_added = clnr.apply_pairs(pairs_array, temp_node.parent)

            temp_node.children = t_be_added

            g[count] = temp_node
            count = count + 1

            # add the new nodes to the back of the qu
            temp_q = deque()
            for key in temp_node.children:
                add_node = Node()
                add_node.parent = temp_node.children[key]
                add_node.path_cost = temp_node.path_cost + 1
                add_node.key = temp_node.key + key.translate(str.maketrans('', '', string.punctuation))
                temp_q.append(add_node)

                #q.put(add_node)
            q = temp_q + q
        if len(g) >= 1000:
            if len(q) > max_fringe:
                max_fringe = len(q)
            break

    return g, max_fringe

def IDS ():
    return 'ids'

def UCS ():
    return 'ucs'