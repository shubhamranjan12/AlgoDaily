def reverse_string(str1):
  str1=list(str1)
  start = 0
  end=len(str1)-1
  while start < end:
    str1[start],str1[end]=str1[end],str1[start]
    start += 1
    end -= 1

  str1 = ''.join(str1)
  return str1
