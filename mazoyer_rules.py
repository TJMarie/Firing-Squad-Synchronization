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
            "L, A",
            "A, L",
            "A, A",
            "C, L",
            "C, A"
        )
        a_to_b = (
            "A, B",
            "A, G"
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
            "X, C",
            "L, C",
            "B, L",
            "B, B"
        )
        a_to_f = (
            "X, A",
            "A, X"
        )
        a_transition_rules = {a_to_l: "L", a_to_a: "A", a_to_b: "B", a_to_c: "C", a_to_g: "G", a_to_f: "F"}
        return a_transition_rules
    
    def b_rules(self):
        b_to_l = (
            "L, C",
            "A, C",
            "C, X",
            "C, L",
            "C, G"
        )
        b_to_a = (
            "B, A",
            "C, A"
        )
        b_to_b = (
            "L, B",
            "L, G",
            "A, A",
            "A, B",
            "B, B",
            "B, G",
            "G, C"
        )
        b_to_c = (
            "B, C",
            "G, L",
            "G, A"
        )
        b_to_g = (
            "L, A",
            "A, L",
            "B, L",
            "G, X",
            "G, G"
        )
        b_transition_rules = {b_to_l: "L", b_to_a: "A", b_to_b: "B", b_to_c: "C", b_to_g: "G"}
        return b_transition_rules
    
    def c_rules(self):
        c_to_a = (
            "L, A",
            "C, A"
        )
        c_to_b = (
            "A, X",
            "A, L",
            "A, B",
            "A, G",
            "C, B",
            "C, G",
            "G, X",
            "G, L",
            "G, B",
            "G, G"
        )
        c_to_c = (
            "L, L",
            "L, C",
            "B, L",
            "B, C",
            "C, L",
            "C, C"
        )
        c_to_g = (
            "L, B",
            "L, G",
            "B, X",
            "B, G"
        )
        c_transition_rules = {c_to_a: "A", c_to_b: "B", c_to_c: "C", c_to_g: "G"}
        return c_transition_rules
    
    def g_rules(self):
        g_to_a = (
            "X, L",
            "C, X",
            "C, L",
            "C, G"
        )
        g_to_b = (
            "A, L",
            "B, L",
            "G, L"
        )
        g_to_g = (
            "X, B",
            "X, C",
            "L, A",
            "L, B",
            "L, C",
            "A, B",
            "A, C",
            "B, X",
            "B, B",
            "B, C",
            "B, G",
            "C, B",
            "C, C",
            "G, B",
            "G, C"
        )
        g_to_f = (
            "X, G",
            "G, X",
            "G, G"
        )
        g_transition_rules = {g_to_a: "A", g_to_b: "B", g_to_g: "G", g_to_f: "F"}
        return g_transition_rules
    '''
    def h_rules(self):
        h_transition_rules = {}
        return h_transition_rules
    
    def r_rules(self):
        r_transition_rules = {}
        return r_transition_rules'''