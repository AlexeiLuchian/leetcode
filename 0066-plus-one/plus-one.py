class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        digits[-1] += 1

        for i in range(len(digits)-1, -1, -1):
            if i != 0:
                if digits[i] == 10:
                    digits[i-1] += 1
                    digits[i] = 0
            else:
                if digits[i] == 10:
                    digits[i] = 0
                    x = [1]
                    return x + digits
        
        return digits