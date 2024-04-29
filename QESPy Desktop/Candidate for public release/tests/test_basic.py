coefficient_b = -12
coefficient_c = 6

auxiliary_line_sol_1 = -coefficient_b / 2
auxiliary_line_sol_11 = f'{int(auxiliary_line_sol_1)}' if auxiliary_line_sol_1.is_integer() else f'{auxiliary_line_sol_1:.2f}'

print(auxiliary_line_sol_11)
