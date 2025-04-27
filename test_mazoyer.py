# Source: https://cs.stanford.edu/people/eroberts/courses/soco/projects/2004-05/automata-theory/problem.html

import copy

class Transitions:
    """ Transition Rules

        States:
        L --> Quiescent State
        F --> Final State
        A
        B
        C
        G
        H
        R

        (U, V) --> T, where
        U == state of left cell at time t,
        V == state of right cell at time t,
        T == state of particular cell at time t + 1
    """

    def __init__(self, current_states):
        """ current_states --> List(String) """
        self.current_states = copy.deepcopy(current_states)
        self.next_states = copy.deepcopy(current_states)
        self.num_cells = len(current_states)
        self.chart = ""

    def give_fire_command(self):
        print("Giving Fire command")
        self.current_states[0] = "G"
        print(self.current_states)
    '''
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
    '''
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
        # self.next_states[0] = self.leftmost_transition(self.current_states[0], self.current_states[1])

        self.next_states[0] = self.middle_transition("X", self.current_states[0], self.current_states[1])

        print("Number of loops", str(self.num_cells - 2))
        
        for i in range(1, self.num_cells - 1):
            cell_left = self.current_states[i - 1]
            cell = self.current_states[i]
            cell_right = self.current_states[i + 1]
            next_state = self.middle_transition(cell_left, cell, cell_right, i)
            self.next_states[i] = next_state
        
        # Set rightmost state last
        # self.next_states[-1] = self.rightmost_transition(self.current_states[-1], self.current_states[-2])

        self.next_states[-1] = self.middle_transition(self.current_states[-2], self.current_states[-1], "X")

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
        file_name = f"output{self.num_cells}.tsv"
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