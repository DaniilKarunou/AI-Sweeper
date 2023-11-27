def get_moves(node):
    moves = []
    while node.parent is not None:
        moves.append(node.action)
        node = node.parent
    return list(reversed(moves))


class BFS:
    def __init__(self, matrix, goal):
        self.matrix = matrix
        self.goal = goal

    def goaltest(self, state):
        current = (state[1]*60, state[0]*60)
        try:
            return current in list(self.goal.keys())
        except AttributeError:
            return current == self.goal

    def succ(self, state, direction):
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
                        self.matrix[state[0]][state[1] - 1] != 5):
                    node_new.state = [state[0], state[1] - 1]
                    node_new.action = action
                    states.append(node_new)
                elif direction == "R" and (0 <= state[1] + 1 <= len(self.matrix[0]) - 1) and (
                        self.matrix[state[0]][state[1] + 1] != 5):
                    node_new.state = [state[0], state[1] + 1]
                    node_new.action = action
                    states.append(node_new)
                elif direction == "U" and (0 <= state[0] - 1 <= len(self.matrix) - 1) and (
                        self.matrix[state[0] - 1][state[1]] != 5):
                    node_new.state = [state[0] - 1, state[1]]
                    node_new.action = action
                    states.append(node_new)
                elif direction == "D" and (0 <= state[0] + 1 <= len(self.matrix) - 1) and (
                        self.matrix[state[0] + 1][state[1]] != 5):
                    node_new.state = [state[0] + 1, state[1]]
                    node_new.action = action
                    states.append(node_new)
        return states

    def graphsearch(self, fringe, explored, istate, direction):
        fringe.append(node(istate, direction))
        while True:
            if not fringe:
                return False

            elem = fringe.popleft()

            if self.goaltest(elem.state):
                return get_moves(elem)

            explored.append(elem)

            for state in self.succ(elem.state, elem.direction):

                if (state not in fringe) and (state not in explored):
                    state.parent = elem
                    fringe.append(state)

class node():
    def __init__(self, state, direction):
        self.state = state
        self.parent = None
        self.action = None
        self.direction = direction

    def __eq__(self, other):
        if isinstance(other, node):
            return (self.state == other.state and
                    self.action == other.action and
                    self.direction == other.direction)
