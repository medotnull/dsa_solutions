def containsWater(s):
  l = 0
  r = len(s) - 1
  max_area = 0
  while l < r:
    max_area = max(max_area, min(s[l], s[r]) * (r - l))
    if s[l] < s[r]:
      l+=1
    else:
      r-=1
  return max_area