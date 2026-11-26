from investment_science.ch02.ex2_11 import PROJECT_1, PROJECT_2

# Cash flows a_k = y_k - x_k of Project 2 less those of Project 1.
DIFFERENCE = [y - x for (x, y) in zip(PROJECT_1, PROJECT_2)]
