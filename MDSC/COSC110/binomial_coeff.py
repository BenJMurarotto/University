def binomial_coeff(n, k) -> int:
  if k == 0:
    return 1
  if n == 0:
    return 0

  res = binomial_coeff(n-1, k) + binomial_coeff(n-1, k-1)
  return res


binomial_coeff(1,2)