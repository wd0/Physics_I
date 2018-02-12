g = 9.8

def perr(theo, exp):
  return abs(theo - exp)/theo
  
def transpose(*lists):
  matrix = lists
  transposed = zip(*matrix)
  return transposed

m1s = [0.109, 0.116, 0.129, 0.138, 0.145]
m2s = [0.157, 0.162, 0.171, 0.189, 0.198]
aexps = [1.52, 1.75, 1.79, 1.37, 1.32]

fnets = [round((m2 - m1)*g, 4) for m1, m2 in zip(m1s, m2s)]
sums = [m1 + m2 for m1, m2 in zip(m1s, m2s)]
atheos = [round(fnet/(m1 + m2), 3) for fnet, m1, m2 in zip(fnets, m1s, m2s)]
errs = [round(perr(theo, exp)*100, 1) for theo, exp in zip (atheos, aexps)]

output_rows = transpose(fnets, sums, atheos, errs)
for row in output_rows:
  print(row)
