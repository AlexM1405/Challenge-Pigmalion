"""
Challenge Pigmalion Alejandro Mora
"""



class Challenge:
    def SumOfTwo(self, nums:list[int], requiredSum:int) -> bool:
    
        Result = set()

        for num in nums:
             Diff = requiredSum - num
             if Diff in Result:
                 return True

             Result.add(num)
             
        return False


challenge = Challenge()

nums = [1,2,4,4]
requiredSum = 8
result = challenge.SumOfTwo(nums, requiredSum)

print(f"The Result is: {result}")
