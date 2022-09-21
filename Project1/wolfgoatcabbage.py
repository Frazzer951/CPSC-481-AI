from search import Problem, depth_first_graph_search, breadth_first_graph_search


class WolfGoatCabbage(Problem):
    def __init__(self):
        """Define goal state and initialize a problem"""
        super().__init__(frozenset({"F", "W", "G", "C"}), frozenset())

    def is_valid_action(self, state, action):
        """Return true if the action is valid and false if it is not"""
        new_state = self.result(state, action)

        return not (
            (
                ("F" in new_state and ("W" not in new_state and "G" not in new_state))
                or ("F" not in new_state and ("W" in new_state and "G" in new_state))
                or ("F" in new_state and ("G" not in new_state and "C" not in new_state))
                or ("F" not in new_state and ("G" in new_state and "C" in new_state))
            )
        )

    def actions(self, state):
        """Return the actions that can be executed in the given
        state. The result would typically be a list, but if there are
        many actions, consider yielding them one at a time in an
        iterator, rather than building them all at once."""

        if (
            ("F" in state and ("W" not in state and "G" not in state))
            or ("F" not in state and ("W" in state and "G" in state))
            or ("F" in state and ("G" not in state and "C" not in state))
            or ("F" not in state and ("G" in state and "C" in state))
        ):
            return []

        possible_actions = [{"F"}]

        if "F" in state:
            things = list(state)
            possible_actions.extend([{"F", x} for x in things if x != "F"])
        else:
            things = [item for item in ["W", "G", "C"] if item not in state]
            possible_actions.extend([{"F", x} for x in things])

        return [action for action in possible_actions if self.is_valid_action(state, action)]

    def result(self, state, action):
        """Return the state that results from executing the given
        action in the given state. The action must be one of
        self.actions(state)."""

        new_state = set(state)

        if "F" in state:
            for item in action:
                new_state.remove(item)
        else:
            for item in action:
                new_state.add(item)

        return frozenset(new_state)

    def goal_test(self, state):
        """Given a state, return True if state is a goal state or False, otherwise"""

        return state == self.goal


if __name__ == "__main__":
    wgc = WolfGoatCabbage()
    solution = depth_first_graph_search(wgc).solution()
    print(solution)
    solution = breadth_first_graph_search(wgc).solution()
    print(solution)
