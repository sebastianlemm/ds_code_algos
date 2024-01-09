class MyStack(object):
    def __init__(self, type):  # Creates an empty list
        self.elemType = type
        self.state = []  # Empty list

    def __str__(self):  # for print
        return str(self.state)

    def empty(self):
        return len(self.state) == 0

    def push(self, elem):  # Adds an element to the top of a stack
        assert type(elem) == self.elemType
        self.state.append(elem)

    def pop(self):  # Removes an element from the top of the stack
        if self.empty():
            raise ValueError("Requested top of an empty stack")
        else:
            return self.state.pop()

    def top(self):  # Returns the top of a nonempty stack
        if self.empty():
            raise ValueError("Requested top of an empty stack")
        else:
            return self.state[-1]

def is_feasible(graph, state, color, node):
    for adj in range(len(graph)):
        if graph[node][adj] and adj < len(state):
            if state[adj] == color:
                return False
    return True

def graph_coloring(graph, colors):
    n = len(graph)
    s = MyStack(list)
    s.push([])  # Initial empty state

    while not s.empty():
        currentState = s.pop()
        current_node = len(currentState)

        if current_node == n:
            print(currentState)  # Found a solution
            return  # Stop after finding the first solution

        for color in colors:
            if is_feasible(graph, currentState, color, current_node):
                childState = currentState.copy()
                childState.append(color)
                s.push(childState)

# Example usage
graph = [[False, True, False, False, False, True],
         [True, False, True, False, False, True],
         [False, True, False, True, True, False],
         [False, False, True, False, True, False],
         [False, False, True, True, False, True],
         [True, True, False, False, True, False]]
colors = ['r', 'g', 'b']
graph_coloring(graph, colors)


### output ###
### ['b', 'g', 'b', 'r', 'g', 'r'] ###