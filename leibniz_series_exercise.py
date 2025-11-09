def pi(n_terms):
  leibniz_series = []
  for i in range(n_terms):
     leibniz_series.append((-1)**i/(2*i+1))
  sum_numbers = sum(leibniz_series) 
  pi = 4*(sum_numbers)
  return pi 
