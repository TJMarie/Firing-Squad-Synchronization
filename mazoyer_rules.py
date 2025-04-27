class Mazoyer:
    def l_rules(self):
        l_to_l = (
            "X, L",
            "L, X",
            "L, L",
            "L, B",
            "L, C",
            "L, G",
            "A, A",
            "A, B",
            "A, C",
            "B, X",
            "B, L",
            "B, A",
            "B, B",
            "B, C",
            "B, G",
            "C, A",
            "C, B",
            "C, C",
            "G, A",
            "G, B",
            "G, C"
        )
        l_to_a = (
            "C, L",
            "G, G"
        )
        l_to_c = (
            "A, X",
            "A, G",
            "G, L"
        )
        l_to_g = (
            "A, L",
            "C, X", 
            "C, G"
        )

        l_transition_rules = {l_to_l: "L", l_to_a: "A", l_to_c: "C", l_to_g: "G"}
        return l_transition_rules
    
    def a_rules(self):
        a_to_l = (
            "L, B"
        )
        a_to_a = (
            "L, L",
            "L, A",
            "A, L",
            "A, A",
            "C, L",
            "C, A",
            "H, A"
        )
        a_to_b = (
            "A, B"
        )
        a_to_c = (
            "A, C",
            "B, X",
            "B, C",
            "B, G",
            "G, X",
            "G, C",
            "G, G"
        )
        a_to_g = (
            "L, C"
        )
        a_transition_rules = {a_to_l: "L", a_to_a: "A", a_to_b: "B", a_to_c: "C", a_to_g: "G"}
        return a_transition_rules
    
    def b_rules(self):
        b_to_l = (
            "L, C"
        )
        b_to_a = (
            "B, A",
            "C, X",
            "C, A",
            "C, G"
        )
        b_to_b = (
            "L, L",
            "L, B",
            "A, L",
            "A, B",
            "B, L",
            "B, B"
        )
        b_to_c = (
            "B, C"
        )
        b_to_g = (
            "L, A"
        )
        b_transition_rules = {b_to_l: "L", b_to_a: "A", b_to_b: "B", b_to_c: "C", b_to_g: "G"}
        return b_transition_rules
    
    def c_rules(self):
        c_transition_rules = {}
        return c_transition_rules
    
    def g_rules(self):
        g_transition_rules = {}
        return g_transition_rules
    
    def h_rules(self):
        h_transition_rules = {}
        return h_transition_rules
    
    def r_rules(self):
        r_transition_rules = {}
        return r_transition_rules