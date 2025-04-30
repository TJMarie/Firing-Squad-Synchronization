<h1>Firing Squad Synchronization</h1>
<p>This project takes a look at Abraham Waksman and Jacques Mazoyer's solutions to the firing squad synchronization problem. The final product uses mazoyer.py, which imports mazoyer_rules.py, and outputs (a) tsv file(s) to the MazoyerOutput directory containing a chart of the state transitions until fire.</p>

<p>Transition rules are denoted in the format "U, V", where U is the state of the lefthand machine and V is the state of the righthand machine. Every transition rule is listed in mazoyer_rules.py, and a longer summary is outlined in mazoyer_rules.txt. The leftmost and rightmost machines make separate calls to the cell_transition method using a special state, X, denoting the absence of a machine on one side. All other machines are processed in a `for` loop.</p>

<p>Researchers at the Carnegie Institute of Technology wrote a program that verified Abraham Waksman's solution up to 50 soldiers. In the MazoyerOutput directory, you can find tsv files which verify all cases from 2 to 1100+ cells. </p>
