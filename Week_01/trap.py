class Solution:
    def trap(self, height: List[int]) -> int:
        length = len(height)
        if length < 3:
            return 0
        total, i = 0, 0
        stack = []
        while i < length:
            while len(stack) > 0 and height[i] > height[stack[-1]]:
                top = stack.pop() 
                if len(stack) == 0:
                    break
                h = min(height[stack[-1]], height[i]) - height[top]
                dist = i - stack[-1] - 1
                total += (dist * h)
            stack.append(i)
            i += 1
        return total