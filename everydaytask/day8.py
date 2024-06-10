input_names = """Chandrakant   Narayan  
jagadish     singh 
  Siva  kumar  Pillai  """

#print(lines)
def removingSpaces(lines):
    lines_input = []
    lines = input_names.split("\n")
    for i in lines:
        lines_input.append(' '.join(i.split()))
    return '\n'.join(lines_input)

result = removingSpaces(input_names)
print(result)

#output:
Chandrakant Narayan
jagadish singh
Siva kumar Pillai
