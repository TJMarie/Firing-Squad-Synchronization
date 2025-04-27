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
        self.current_states = copy.deepcopy(current_states)
        self.next_states = copy.deepcopy(current_states)
        self.num_states = len(current_states)
        self.chart = ""

    def q_rules(self):
        q_to_q = (
            "Q, A011",
            "Q, A110",
            "Q, A111",
            "B, A011",
            "B, A110",
            "B, A111",
            "R0, A010",
            "R0, A011",
            "R0, A110",
            "R0, A111",

            "A001, Q",
            "A001, B",
            "A001, R1",
            "A100, Q",
            "A100, B",
            "A101, Q",
            "A101, B",
            "Q, Q",
            "Q, B",
            "Q, R1",

            "B, Q",
            "B, B",
            "B, R1",
            "B, P0",
            "B, P1",
            "R0, Q",
            "R0, B",
            "R0, Y",
            "P0, B",
            "P0, R1",
            "P1, B",
            "P1, R1"
            )
        q_to_a000 = (
            "Q, A001",
            "B, A001",
            "R0, A001",
            "R1, A001",

            "Q, P0",
            "Y, P0",

            "R0, P0"
        )
        q_to_a001 = (
            "Q, A000",
            "B, A000",
            "R0, A000",
            "R1, A000"
        )
        q_to_a010 = (
            "A011, Q",
            "A011, B",

            "P0, Q"
        )
        q_to_a011 = (
            "A010, Q",
            "A010, B"
        )
        q_to_a100 = (
            "Q, A101",
            "B, A101",
            "R0, A101",
            "R1, A101",

            "Q, P1"
        )
        q_to_a101 = (
            "Q, A100",
            "B, A100",
            "R0, A100",
            "R1, A100"
        )
        q_to_a110 = (
            "A111, Q",
            "A111, B",

            "P1, Q"
        )
        q_to_a111 = (
            "A110, Q",
            "A110, B"
        )
        q_to_b0 = (
            "P0, A011",
            "P1, A110",

            "A001, P0"
        )
        q_to_p0 = (
            "Q, A000",
            "Q, A100",

            "A010, Q",
            "A110, Q",

            "P0, P0",
            "P0, P1",
            "P1, P0",
            "P1, P1"
        )
        q_to_p1 = (
            "Q, A001",
            "Q, A101",

            "A011, Q",
            "A111, Q"
        )
        q_to_r0 = (
            "Q, A010",
            "B, A010",

            "Q, R0",

            "B, R0",
            "P0, R0",
            "P1, R0"
            )
        q_to_r1 = (
            "A000, Q",
            "A000, B",

            "R1, Q",
            "R1, B",
            "R1, P0",
            "R1, P1"
        )
        q_transition_rules = {
            q_to_q: "Q", 
            q_to_a000: "A000", 
            q_to_a001: "A001", 
            q_to_a010: "A010", 
            q_to_a011: "A011", 
            q_to_a100: "A100", 
            q_to_a101: "A101", 
            q_to_a110: "A110", 
            q_to_a111: "A111", 
            q_to_b0: "B0", 
            q_to_p0: "P0", 
            q_to_p1: "P1",
            q_to_r0: "R0", 
            q_to_r1: "R1"}

        return q_transition_rules
    
    def b0_rules(self):
        b0_to_b0 = (
            "P, Y"
        )
        b0_to_p0 = (
            "Y, A000",
            "Y, A101",
            "P, P",
            "A010, Y",
            "A111, Y"
        )
        b0_to_p1 = (
            "Y, A100",
            "Y, A001",
            "A110, Y",
            "A011, Y"
        )
        b0_to_r0 = (
            "Y, R0",
            "P, R0"
        )
        b0_to_r1 = (
            "R1, Y"
        )
        # Else B0

        b0_transition_rules = {
            b0_to_b0: "B0",
            b0_to_p0: "P0",
            b0_to_p1: "P1",
            b0_to_r0: "R0",
            b0_to_r1: "R1"
        }
        return b0_transition_rules
    
    def b1_rules(self):
        b1_to_q = (
            "Y, R0",
            "R1, Q"
        )
        b1_to_p0 = (
            "Y, A000",
            "Y, A101",
            "A010, Y",
            "A111, Y",
            "P0, P0",
            "P0, P1",
            "P1, P0",
            "P1, P1"
        )
        b1_to_p1 = (
            "Y, A100",
            "Y, A001",
            "A110, Y",
            "A011, Y"
        )
        b1_transition_rules = {
            b1_to_q: "Q",
            b1_to_p0: "P0",
            b1_to_p1: "P1"
        }
        return b1_transition_rules
    
    def r0_rules(self):
        r0_to_b0 = (
            "B1, Y",
            "P0, Y",
            "P1, Y"
        )
        r0_to_b1 = (
            "B0, Y"
        )
        # Else Q
        r0_transition_rules = {r0_to_b0: "B0", r0_to_b1: "B1"}

        return r0_transition_rules
    
    def r1_rules(self):
        r1_to_b0 = (
            "B1, Y",
            "P0, Y",
            "P1, Y"
        )
        r1_to_b1 = (
            "B0, Y"
        )
        # Else Q
        r1_transition_rules = {r1_to_b0: "B0", r1_to_b1: "B1"}

        return r1_transition_rules
    
    def p0_rules(self):
        p0_to_t = (
            "P0, P0",
            "P0, P1",
            "P1, P0"
        )
        # Else P0

        return {p0_to_t: "T"}
    
    def p1_rules(self):
        p1_to_t = (
            "P0, P0",
            "P0, P1",
            "P1, P0"
        )
        # Else P1

        return {p1_to_t: "T"}
    
    def a000_rules(self):
        a000_to_q = (
            "Y, P0",
            "Y, P1"
        )
        a000_to_b0 = (
            "Y, P0"
        )

        return {a000_to_q: "Q", a000_to_b0: "B0"}
    
    def a001_rules(self):
        return {("Y, Y"): "Q"}
    
    def a100_rules(self):
        a100_to_p1 = (
            "B0, Y",
            "B1, Y"
        )
        a100_to_r1 = (
            "Q, P1"
        )

    def give_fire_command(self):
        print("Giving Fire command")
        self.current_states[0] = "P"
        print(self.current_states)
    
    def leftmost_transition(self, cell, cell_right):
        rule = f"({cell}, {cell_right})"

        if cell_right == "P":
            next_state = "T"
        else:
            next_state = cell
        
        print(f"Leftmost transition:\nCurrent State: {cell}\t{rule} => {next_state}")

        return next_state

    def rightmost_transition(self, cell, cell_left):
        """ (cell, cell_left) """
        if (cell == "Q" and cell_left == "A1"):
            next_state = "P"
        elif (cell == "P" and cell_left == "P"):
            next_state = "P"
        else:
            next_state = cell
        
        print(f"\nRightmost transition:\nCurrent State: {cell}\t({cell_left}, {cell}) => {next_state}")

        return next_state
    
    def middle_transition(self, cell_left, cell, cell_right, index):
        """ Transition Rules: Dict{List(String): String} """

        print("\nMiddle Transition")
        rule = f"{cell_left}, {cell_right}"
        print(f"Current State:\t{cell}\t{str(index + 1)}")
        print("Rule:\t"+ rule)

        if cell == "Q":
            transition_rules = self.q_rules()
        elif cell == "R":
            transition_rules = self.r_rules()
        elif cell == "A1":
            transition_rules = self.a_rules()
        elif cell == "A0":
            transition_rules = self.a0_rules()
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

        # print(transition_rules)

        next_state = False

        # Add code to check if rule occurs in more than one key
        for key, value in transition_rules.items():
            if rule in key:
                next_state = value

        if next_state == False:
            print(f"Error: Could not find rule ({rule})")
            print(self.chart)
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
            next_state = self.middle_transition(cell_left, cell, cell_right, i)
            self.next_states[i] = next_state
        
        # Set rightmost state last
        self.next_states[-1] = self.rightmost_transition(self.current_states[-1], self.current_states[-2])

        print("Current States:", self.current_states)
        print("Next States:", self.next_states)

        self.current_states = copy.deepcopy(self.next_states)
    
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

        i = 1

        while True:  # Fix
            print("\n\nStep", i)
            self.make_transition()

            row = ""
            for state in self.next_states:
                row += f"{state}\t"

            self.chart += f"{str(i)}\t{row}\n"
            i += 1

def __main__():
    """ current_states --> List() """
    print("Starting Program")
    num_cells = 11
    current_states = ["Q" for i in range(num_cells)]

    print("Starting states:", current_states)

    firing_squad = Transitions(current_states)
    firing_squad.run()

__main__()