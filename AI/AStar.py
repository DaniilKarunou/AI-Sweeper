import heapq
from gameObjects.elems import Duzykamien

# 1 - wall
# 2 - grass
# 3 - rocks
# 4 - water

def h(a, b):
    """Manhattan distance"""
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def get_moves(node):
    """Returns the moves taken to reach the node"""
    moves = []
    while node.parent is not None:
        moves.append(node.action)
        node = node.parent
    return list(reversed(moves))


class AStar:
    """A* algorithm"""
    def __init__(self, matrix, endpoint):
        self.matrix = matrix
        self.endpoint = endpoint

    def goaltest(self, state):
        """Returns True if the state is the goal state"""
        current = (state[1] * 60, state[0] * 60)
        return current == self.endpoint

    def g(self, state):
        """Returns the cost of the path from the initial state to the current state"""
        if state.action in ["L", "R"]:
            state.cost = state.parent.cost
        elif state.action == "M":
            state.cost = state.parent.cost + self.matrix[state.state[0]][state.state[1]]
        return state.cost

    def f(self, state):
        """Returns the total cost of the path from the initial state to the goal state"""
        return self.g(state) + h(state.state, self.endpoint)

    def succ(self, state, direction):
        """Returns a list of the successor states"""
        states = []
        for action in ["L", "R", "M"]:

            node_new = node(state, direction)
            if action == "L":
                if direction == "L":
                    node_new.direction = "D"
                    node_new.action = action
                    states.append(node_new)
                elif direction == "R":
                    node_new.direction = "U"
                    node_new.action = action
                    states.append(node_new)
                elif direction == "U":
                    node_new.direction = "L"
                    node_new.action = action
                    states.append(node_new)
                else:
                    node_new.direction = "R"
                    node_new.action = action
                    states.append(node_new)
            elif action == "R":
                if direction == "L":
                    node_new.direction = "U"
                    node_new.action = action
                    states.append(node_new)
                elif direction == "R":
                    node_new.direction = "D"
                    node_new.action = action
                    states.append(node_new)
                elif direction == "U":
                    node_new.direction = "R"
                    node_new.action = action
                    states.append(node_new)
                else:
                    node_new.direction = "L"
                    node_new.action = action
                    states.append(node_new)

            elif action == "M":
                if direction == "L" and (0 <= state[1] - 1 <= len(self.matrix[0]) - 1) and (
                        self.matrix[state[0]][state[1] - 1] != Duzykamien().koszt):
                    node_new.state = [state[0], state[1] - 1]
                    node_new.action = action
                    states.append(node_new)
                elif direction == "R" and (0 <= state[1] + 1 <= len(self.matrix[0]) - 1) and (
                        self.matrix[state[0]][state[1] + 1] != Duzykamien().koszt):
                    node_new.state = [state[0], state[1] + 1]
                    node_new.action = action
                    states.append(node_new)
                elif direction == "U" and (0 <= state[0] - 1 <= len(self.matrix) - 1) and (
                        self.matrix[state[0] - 1][state[1]] != Duzykamien().koszt):
                    node_new.state = [state[0] - 1, state[1]]
                    node_new.action = action
                    states.append(node_new)
                elif direction == "D" and (0 <= state[0] + 1 <= len(self.matrix) - 1) and (
                        self.matrix[state[0] + 1][state[1]] != Duzykamien().koszt):
                    node_new.state = [state[0] + 1, state[1]]
                    node_new.action = action
                    states.append(node_new)
        return states

    def graphsearch(self, fringe, explored, istate, direction):
        """Returns the moves taken to reach the goal state"""
        fringe.put(node(istate, direction), 0)
        while True:
            if not fringe:
                return False

            elem = fringe.get()

            if self.goaltest(elem.state):
                return get_moves(elem)

            explored.append(elem)

            for state in self.succ(elem.state, elem.direction):
                state.parent = elem
                p = self.f(state)
                state.cost = self.g(state)
                if (state not in fringe) and (state not in explored):
                    fringe.put(state, p)
                elif (state in fringe) and state.cost > p:
                    fringe.replace(state, p)


class node():
    """Node class"""
    def __init__(self, state, direction):
        self.state = state
        self.parent = None
        self.action = None
        self.direction = direction
        self.cost = 0

    def __eq__(self, other):
        if isinstance(other, node):
            return (self.state == other.state and
                    self.action == other.action and
                    self.direction == other.direction)

    def __lt__(self, other):
        return self.cost < other.cost

    def __gt__(self, other):
        return self.cost > other.cost

    def __le__(self, other):
        return self.cost <= other.cost

    def __ge__(self, other):
        return self.cost >= other.cost

class PriorityQueue:
    def __init__(self):
        self.queue = []

    def put(self, item, priority):
        heapq.heappush(self.queue, [priority, item])

    def get(self):
        return heapq.heappop(self.queue)[1]

    def empty(self):
        return len(self.queue) == 0

    def replace(self, item, priority):
        for i in range(len(self.queue)):
            if self.queue[i][1] == item:
                self.queue[i] = (priority, item)
                heapq.heapify(self.queue)
                return
        raise ValueError("Item not found")

    def __contains__(self, item):
        return any(item == pair[1] for pair in self.queue)



