def arithmetic_arranger(problems, show=False):
  #Rule 1: The limit for problem is five
  if len(problems) > 5:
    return "Error: Too many problems."

  arranged_problems = []
  first_line = []
  second_line = []
  dash_line = []
  result_line = []

  for problem in problems:
    operand1, operator, operand2 = problem.split()
    #Rule 2: The operator must be '+' or '-'
    if operator not in ['+', '-']:
      return "Error: Operator must be '+' or '-'."

    #Rule 3: Each operand has a max of four digits in width
    if len(operand1) > 4 or len(operand2) > 4:
      return "Error: Numbers cannot be more than four digits."

    #Rule 4: Each number (operand) should only contain digits
    if not operand1.isdigit() or not operand2.isdigit():
      return "Error: Numbers must only contain digits."

    #Adjusting the width of the problem and formatting the output (right justify)
    width = max(len(operand1), len(operand2)) + 2
    first_line.append(operand1.rjust(width))
    second_line.append(operator + operand2.rjust(width - 1))
    dash_line.append('-' * width)

    #Calculate the result if show is True
    if show:
      if operator == '+':
        solution = str(int(operand1) + int(operand2))
      else:
        solution = str(int(operand1) - int(operand2))
      result_line.append(solution.rjust(width))

  #Join the lines
  arranged_problems.append("    ".join(first_line))
  arranged_problems.append("    ".join(second_line))
  arranged_problems.append("    ".join(dash_line))

  if show:
    arranged_problems.append("    ".join(result_line))

  return "\n".join(arranged_problems)
