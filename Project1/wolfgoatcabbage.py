from search import Problem, depth_first_graph_search, breadth_first_graph_search


class WolfGoatCabbage(Problem):
    def __init__(self):
        """Define goal state and initialize a problem"""
        super().__init__({"F", "W", "G", "C"}, set())

    def actions(self, state):
        """Return the actions that can be executed in the given
        state. The result would typically be a list, but if there are
        many actions, consider yielding them one at a time in an
        iterator, rather than building them all at once."""
        raise NotImplementedError

    def result(self, state, action):
        """Return the state that results from executing the given
        action in the given state. The action must be one of
        self.actions(state)."""
        raise NotImplementedError

    def goal_test(self, state):
        """Given a state, return True if state is a goal state or False, otherwise"""

        return state == self.goal


if __name__ == "__main__":
    wgc = WolfGoatCabbage()
    solution = depth_first_graph_search(wgc).solution()
    print(solution)
    solution = breadth_first_graph_search(wgc).solution()
    print(solution)
