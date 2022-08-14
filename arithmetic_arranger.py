def arithmetic_arranger(inp, signal=False):
  if len(inp) > 5:
    return "Error: Too many problems."

  #Elements 
  first = []
  second = []
  operator = []

  #CATCHING ELEMENTS
  for element in inp:
    elements = element.split()
    first.append(elements[0])
    operator.append(elements[1])
    second.append(elements[2])

  #print test
  #print(first[0],operator[0],second[0])

  #not * or /
  if "*" in operator or "/" in operator:
    return "Error: Operator must be '+' or '-'."


  #only digits
  for i in range(len(first)):
    if not (first[i].isdigit() and second[i].isdigit()):
      return "Error: Numbers must only contain digits."

  #no more than four digits
  for i in range(len(first)):
    if len(first[i]) > 4 or len(second[i]) > 4:
      return "Error: Numbers cannot be more than four digits."

  f_line = []
  s_line = []
  t_line = []
  fo_line = []

  for i in range(len(first)):
    if len(first[i]) > len(second[i]):
      f_line.append(" "*2 + first[i])
    else:
      f_line.append(" "*(len(second[i]) - len(first[i]) + 2) + first[i])

  for i in range(len(second)):
    if len(second[i]) > len(first[i]):
      s_line.append(operator[i] + " " + second[i])
    else:
      s_line.append(operator[i] + " "*(len(first[i]) - len(second[i]) + 1) + second[i])

  for i in range(len(first)):
    t_line.append("-"*(max(len(first[i]), len(second[i])) + 2))
  
  
  
  
  if signal:
    for i in range(len(first)):
      if operator[i] == "+":
          ans = str(int(first[i]) + int(second[i]))
      else:
          ans = str(int(first[i]) - int(second[i]))

      if len(ans) > max(len(first[i]), len(second[i])):
          fo_line.append(" " + ans)
      else:
          fo_line.append(" "*(max(len(first[i]), len(second[i])) - len(ans) + 2) + ans)
    arranged_problems = "    ".join(f_line) + "\n" + "    ".join(s_line) + "\n" + "    ".join(t_line) + "\n" + "    ".join(fo_line)
  else:
    arranged_problems = "    ".join(f_line) + "\n" + "    ".join(s_line) + "\n" + "    ".join(t_line)
  return(arranged_problems) 