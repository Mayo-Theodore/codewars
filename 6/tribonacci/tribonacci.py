def n(signature, n):
    while len(signature) < 5:
        signature.append(1)
    return signature

def tribonacci(signature, n):
  res = signature[:n]
  for i in range(n - 3): res.append(sum(res[-3:]))
  return res
