# Source: https://cs.stanford.edu/people/eroberts/courses/soco/projects/2004-05/automata-theory/problem.html

import copy

class Transitions:
    """ Transition Functions
        Q --> Quiescent State
        T --> Final State
        R --> Triggers B State
        B --> Generates P State
        A --> Propagates
        P --> Generates A State, Leads to Final State

        (U, V) --> T
        U == current state of left cell
        V == current state of right cell
        T == state of particular cell at time t + 1
    """

    def __init__(self, current_states):
        """ current_states --> List(String) """
        self.current_states = current_states
        self.next_states = copy.deepcopy(current_states)
        self.num_states = len(current_states)

    def q_rules(self):
        q_to_q = (
            "Q, Q",
            "R, Q",
            "Q, R",
            "R, B",
            "R, A",
            "A, R",
            "B, Q",
            "Q, B",
            "B, B"
            )
        q_to_r = (
            "B, A",
            "Q, A",
            "B, R",
            "Q, R",
            "A, B"
            )
        q_to_a = (
            "P, Q",
            "Q, P",
            "A, Q",
            "B, A",
            "A, B",
            "R, A",
            "R, P"
        )
        q_transition_rules = {q_to_q: "Q", q_to_r: "R", q_to_a: "A"}

        return q_transition_rules
    
    def r_rules(self):
        r_to_q = (
            "Q, Q",
            "Q, B"
        )
        r_to_b = (
            "B, Q",
            "P, B",
            "Q, B",
            "B, P",
            "P, A",
            "A, P"
        )
        r_transition_rules = {r_to_q: "Q", r_to_b: "B"}

        return r_transition_rules
    
    def a_rules(self):
        a_to_q = (
            "B, Q",
            "Q, Q",
            "Q, B"
        )
        a_to_r = (
            "Q, P", 
            "P, Q"
        )
        a_to_b = (
            "P, Q",
            "Q, P"
        )
        a_to_p = (
            "B, R",
            "R, B"
        )
        a_transition_rules = {a_to_q: "Q", a_to_r: "R", a_to_b: "B", a_to_p: "P"}

        return a_transition_rules
    
    def b_rules(self):
        b_to_b = (
            "P, A", 
            "A, P",
            "Q, P",
            "P, A",
            "R, Q",
            "B, Q",
            "Q, B",
            "B, P",
            "P, B",
            "Q, Q"
        )
        b_to_r = (
            "B, Q",
            "P, B",
            "Q, B",
            "B, P",
            "P, A",
            "A, P"
        )
        b_to_p = (
            "P, P",
            "B, A",
            "Q, A",
            "A, B"
        )
        b_transition_rules = {b_to_b: "B", b_to_r: "R", b_to_p: "P"}

        return b_transition_rules
    
    def p_rules(self):
        p_to_t = [
            "P, P"
        ]
        p_transition_rules = {p_to_t: "T"}

        return p_transition_rules

    def give_fire_command(self):
        print("Giving Fire command")
        self.current_states[0] = "P"
        print(self.current_states)
    
    def leftmost_transition(self, cell, cell_right):
        rule = f"({cell}, {cell_right})"

        if cell_right == "P":
            next_state = "T"
        else:
            next_state = "P"
        
        print(rule, "=>", next_state)

        return next_state

    def rightmost_transition(self, cell, cell_left):
        if (cell == "Q" and cell_left == "A"):
            next_state = "A"
        elif (cell == "P" and cell_left == "P"):
            next_state = "P"
        else:
            next_state = "Q"
        
        print("(", cell_left, ",", cell, ") =>", next_state)

        return next_state
    
    def middle_transition(self, cell_left, cell, cell_right):
        """ Transition Rules: Dict{List(String): String} """
        print("Middle Transition")
        rule = f"{cell_left}, {cell_right}"
        print(rule)

        if cell == "Q":
            transition_rules = self.q_rules()
        elif cell == "R":
            transition_rules = self.r_rules()
        elif cell == "A":
            transition_rules = self.a_rules()
        elif cell == "B":
            transition_rules = self.b_rules()
        elif cell == "P":
            transition_rules = self.p_rules()
        elif cell == "T":
            #  If one cell reaches the final state, check if every cell is firing 
            self.check_final()
            # Add code to start next run if all cells fire
        else:
            print("Unknown State:", cell)

        print(transition_rules)

        next_state = False

        for key, value in transition_rules.items():
            if rule in key:
                next_state = value

        if next_state == False:
            print(f"Error: Could not find rule ({rule})")
            quit()

        print(rule, "=>", next_state)
        return next_state

    def make_transition(self):
        """ next_states --> List(String)
            Create list of next states for all cells """

        #  Set leftmost state first
        self.next_states[0] = self.leftmost_transition(self.current_states[0], self.current_states[1])


        print("Number of loops", str(self.num_states - 2))
        
        for i in range(1, self.num_states - 1):
            cell_left = self.current_states[i - 1]
            cell = self.current_states[i]
            cell_right = self.current_states[i + 1]
            next_state = self.middle_transition(cell_left, cell, cell_right)
            self.next_states[i] = next_state
        
        # Set rightmost state last
        self.next_states[-1] = self.rightmost_transition(self.current_states[-2], self.current_states[-1])

        print("Current States:", self.current_states)
        print("Next States:", self.next_states)

        self.current_states = self.next_states
    
    def check_final(self):
        """Return False if cell fired early, True if all cells fire simultaneously"""
        print("Checking Finality")
        if (state != "T" for state in self.next_states):
            print("Cell fired early. Quitting now.")
            quit() 
        else:
            print("All cells fired simultaneouly")
            return True

    def run(self):
        self.give_fire_command()

        print(f"Current States:\n{self.current_states}\nNext States:\n{self.next_states}")

        print("\nRun ")

        self.make_transition()

def __main__():
    """ current_states --> List() """
    print("Starting Program")
    num_cells = 11
    current_states = ["Q" for i in range(num_cells)]

    print("Starting states:", current_states)

    firing_squad = Transitions(current_states)
    firing_squad.run()

__main__()