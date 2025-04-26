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
            "Q, Q",
            "R, Q",
            "Q, R",
            "R, B",
            "R, A1", #
            "A0, R", #
            "B, Q",
            "Q, B",
            "B, B",
            "A0, R1",
            "A0, R1"  #
            )
        q_to_r = (
            "B, A1",
            "Q, A1",
            "B, R",
            "Q, R",
            "A0, B"
            )
        q_to_r1 = (
            "A0, B"
        )
        q_to_a = (
            "P, Q",
            "Q, P",
            "A1, Q",
            # "B, A1",
            "A1, B", #
            # "R, A1",
            "R, P"
        )
        q_to_a0 = (
            "R, P",
            "R, A0",
            "A0, Q"  # TEST
        )
        q_to_p = (
            "B, A0"  # TEST
        )
        q_transition_rules = {q_to_q: "Q", q_to_r: "R", q_to_r1: "R1", q_to_a: "A1", q_to_a0: "A0", q_to_p: "P"}

        return q_transition_rules
    
    def r_rules(self):
        r_to_q = (
            "Q, Q",
            "Q, B"
        )
        r_to_b = (
            "B, Q",
            "P, B",
            # "Q, B",
            "B, P",
            "P, A1",
            "A1, P",
            "A0, P",  # TEST
            "Q, P"  # TEST
        )
        r_transition_rules = {r_to_q: "Q", r_to_b: "B"}

        return r_transition_rules
    
    def r1_rules(self):
        r1_to_b = (
            "Q, B",
            "A0, P",
            "B, P"
        )
        r1_transition_rules = {r1_to_b: "B"}

        return r1_transition_rules
    
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
            "R, B",
            "B, B"
        )
        a_transition_rules = {a_to_q: "Q", a_to_r: "R", a_to_b: "B", a_to_p: "P"}

        return a_transition_rules
    
    def a0_rules(self):
        a0_to_q = (
            "Q, B",
            "B, Q",
            "Q, Q",
            "A1, B",
        )
        a0_to_b = (
            "Q, P"
        )
        a0_to_p = (
            "R, B",
            "Q, R1" #
        )
        a0_to_r = (
            "B, P",
        )
        a0_to_r1 = (
            "B, P"
        )
        a0_to_p = (
            "Q, R1"
        )

        a0_transition_rules = {a0_to_q: "Q", a0_to_b: "B", a0_to_p: "P", a0_to_r: "R", a0_to_r1: "R1", a0_to_p: "P"}

        return a0_transition_rules
    
    def b_rules(self):
        b_to_b = (
            "P, A1", 
            "A0, P",
            "Q, P",
            "P, Q",
            "R, Q",
            "B, Q",
            "Q, B",
            "B, P",
            "P, B",
            "Q, Q",
            "Q, R1" #
        )
        b_to_r = (
            "P, R",
            "Q, R",
            "R, P"
        )
        b_to_r1 = (
            "R1, P"
        )
        b_to_p = (
            "P, P",
            "B, A1",
            "R, A0", #
            "A1, B",
            "A1, P"  # TEST
        )
        b_to_q = (
            "B, R",
            #"Q, R" 
        )
        b_to_a0 = (
            "Q, A0" # TEST
        )
        b_transition_rules = {b_to_b: "B", b_to_r: "R", b_to_r1: "R1", b_to_p: "P", b_to_q: "Q", b_to_a0: "A0"}

        return b_transition_rules
    
    def p_rules(self):
        p_to_t = (
            "P, P"
        )
        p_to_p = (
            "Q, Q",
            "A1, A0",
            "R, R",
            "R1, R", #
            "R1, B",
            "B, B",
            "B, P",
            "P, B",
            "A0, A1",  # TEST
            "R, B"  # TEST
        )
        p_transition_rules = {p_to_t: "T", p_to_p: "P"}

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
            next_state = cell
        
        print(f"Leftmost transition:\nCurrent State: {cell}\t{rule} => {next_state}")

        return next_state

    def rightmost_transition(self, cell, cell_left):
        """ (cell, cell_left) """
        if (cell == "Q" and cell_left == "A1"):
            next_state = "P"
        elif (cell == "P" and cell_left == "P"):
            next_state = "T"
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
        elif cell == "R1":
            transition_rules = self.r1_rules()
        elif cell == "A1":
            transition_rules = self.a_rules()
        elif cell == "A0":
            transition_rules = self.a0_rules()
        elif cell == "B":
            transition_rules = self.b_rules()
        elif cell == "P":
            transition_rules = self.p_rules()
        else:
            print("Unknown State:", cell)
            self.output()

        # print(transition_rules)

        next_state = False

        # Add code to check if rule occurs in more than one key
        for key, value in transition_rules.items():
            if rule in key:
                next_state = value

        if next_state == False:
            print(f"Error: Could not find rule ({rule})")
            self.output()

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
        print("\nChecking Finality")
        for state in self.next_states:
            if state != "T":
                print("Cell fired early. Quitting now.")
                self.output() 
            else:
                print("All cells fired simultaneouly")
                self.output() 

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

            for state in self.next_states:
                if (state == "T"):
                    #  If one cell reaches the final state, check if every cell is firing 
                    self.check_final()
                    # Add code to start next run if all cells fire

            i += 1

    def output(self):
        print(self.chart)
        file_name = f"output{self.num_states}.tsv"
        print(f"Outputting to {file_name}")
        output_file = open(file_name, "w")
        output_file.write(self.chart)
        quit()

def __main__():
    """ current_states --> List() """
    print("Starting Program")
    num_cells = 11
    current_states = ["Q" for i in range(num_cells)]

    print("Starting states:", current_states)

    firing_squad = Transitions(current_states)
    firing_squad.run()

__main__()