#1. Given a binary array nums, return the maximum number of consecutive 1's in the array.

def solve(li):
  ans = 0
  temp = 0
  for i in range(len(li)):
    if li[i] == 1:
      temp += 1
      ans = max(temp, ans)
    else:
      temp = 0
    
  return ans
ans = solve(list(map(int, input().split())))
print(ans)