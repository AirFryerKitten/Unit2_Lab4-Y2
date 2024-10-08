# There is no need to import SAMPLE_MATRICES
# YOUR CODE AND HEADING HERE

#Jonas York
#U2 L4
#Matrix


def mat_sum(m1, m2):
  m1Row = len(m1)
  m1Column = len(m1[0])
  m2Row = len(m2)
  m2Column = len(m2[0])
  if m1Row == m2Row and m1Column == m2Column:
    new = [[0]*m1Column for i in range(m1Row)]
    for row in range(len(m1)):
      for column in range(m1Row):
        new[row][column] = m1[row][column] + m2[row][column]
    return new
  else:
    return "no solution"

def mat_mul(m1, m2):
  m1Row = len(m1)
  m1Column = len(m1[0])
  m2Row = len(m2)
  m2Column = len(m2[0])
  if m1Column == m2Row:
    new = [[0]*m2Column for i in range(m1Row)]
    for i, row in enumerate(new):
      for otheri, column in enumerate(row):
        answer = 0
        for equation in range(len(m1[i])):
          answer += (m1[i][equation]*m2[equation][otheri])
        new[i][otheri] = answer

    return new
  else:
    return "no solution"



