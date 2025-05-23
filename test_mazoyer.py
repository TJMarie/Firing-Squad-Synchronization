# Source: https://cs.stanford.edu/people/eroberts/courses/soco/projects/2004-05/automata-theory/problem.html

import copy
import mazoyer_rules

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

    def __init__(self, current_states, rules):
        """ current_states --> List(String) """
        self.current_states = copy.deepcopy(current_states)
        self.next_states = copy.deepcopy(current_states)
        self.num_cells = len(current_states)
        self.rules = rules
        self.chart = ""

        for i in range(self.num_cells):
            self.chart += f"\t{i + 1}"  # Header row


    def give_fire_command(self):
        print("Giving Fire command")
        self.current_states[0] = "G"
        print(self.current_states)
        
    def middle_transition(self, cell_left, cell, cell_right, index):
        """ Transition Rules: Dict{List(String): String} """

        rule = f"{cell_left}, {cell_right}"
        print(f"{str(index + 1)}\t\t{cell}\t\t({rule})")


        if cell == "L":
            transition_rules = self.rules.l_rules()
        elif cell == "A":
            transition_rules = self.rules.a_rules()
        elif cell == "B":
            transition_rules = self.rules.b_rules()
        elif cell == "C":
            transition_rules = self.rules.c_rules()
        elif cell == "R":
            transition_rules = self.rules.r_rules()
        elif cell == "H":
            transition_rules = self.rules.h_rules()
        elif cell == "G":
            transition_rules = self.rules.g_rules()
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

        # print(rule, "=>", next_state)
        return next_state

    def make_transition(self):
        """ next_states --> List(String)
            Create list of next states for all cells """

        #  Set leftmost state first
        self.next_states[0] = self.middle_transition("X", self.current_states[0], self.current_states[1], 0)
        
        for i in range(1, self.num_cells - 1):
            cell_left = self.current_states[i - 1]
            cell = self.current_states[i]
            cell_right = self.current_states[i + 1]
            next_state = self.middle_transition(cell_left, cell, cell_right, i)
            self.next_states[i] = next_state
        
        # Set rightmost state last
        self.next_states[-1] = self.middle_transition(self.current_states[-2], self.current_states[-1], "X", self.num_cells - 1)

        #print("Current States:", self.current_states)
        #print("Next States:", self.next_states)

        self.current_states = copy.deepcopy(self.next_states)
    
    def check_final(self):
        """Return False if cell fired early, True if all cells fire simultaneously"""

        print("Current States:", self.current_states)
        print("Next States:", self.next_states)

        print("\nChecking Finality")
        for state in self.next_states:
            if state != "F":
                print("Cell fired early. Quitting now.")
                self.output() 
                quit()

        print("All cells fired simultaneouly")
        self.output() 
        return True

    def run(self):
        """ Complete an entire run """

        self.give_fire_command()
        print(f"Current States:\n{self.current_states}\nNext States:\n{self.next_states}")

        i = 1 

        while True:  # Fix
            print(f"\nStep {i}\nidx\t\tstate\t\trule")
            self.make_transition()

            row = ""
            for state in self.next_states:
                row += f"{state}\t"

            self.chart += f"\n{str(i)}\t{row}"

            finished = False
            
            for state in self.next_states:
                if (state == "F"):
                    #  If one cell reaches the final state, check if every cell is firing 
                    finished = self.check_final()
                    break

            if finished:
                break

            i += 1

    def output(self):
        print(self.chart)
        file_name = f"MazoyerOutput/mazoyer_output{self.num_cells}.tsv"
        print(f"Outputting to {file_name}")
        output_file = open(file_name, "w")
        output_file.write(self.chart)

def __main__():
    """ current_states --> List() """
    print("Starting Program")

    for i in range(1000, 1001):
        print(f"\nRun {i - 1}")
        num_cells = i
        current_states = ["L" for j in range(num_cells)]

        print("Starting states:", current_states)

        rules = mazoyer_rules.Mazoyer()

        firing_squad = Transitions(current_states, rules)

        print("Starting next run")
        firing_squad.run()

__main__()