def pi(n_terms):

  list_of_numbers = []
  for i in range(n_terms):
  list_of_numbers.append((-1)**i/(2*i+1))
sum_numbers = sum(list_of_numbers) 
pi = 4*(sum_numbers) 
return pi 
