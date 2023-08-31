def n_digit(num, n):
  """
  Express num as a n-number
    
    Args:
        num (int): The original number to be expressed in n digits
        n (int): The base value to represent num
        
    Returns:
        int: num expressed in n digits
  """
  result = 0
  digit = 0
  while num > 0:
    result += (num % n) * (10 ** digit)
    digit += 1
    num //= n
  return result

n, m = map(int, input().split())
upper_bound = n**m
for i in range(upper_bound):
  #print(n_digit(i,n))
  result = str(n_digit(i,n)+(10**m - 1)//9)
  #result_str = '0'*(m - len(result)) + result
  result_str = [result[i//2] if i % 2 == 0 else ' ' for i in range(2 * m - 1)]
  print(''.join(result_str))