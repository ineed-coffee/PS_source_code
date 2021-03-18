import random
import math

class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.x=x_center
        self.y=y_center
        self.r=radius
        return
    
    def randPoint(self) -> List[float]:
        
        theta = random.uniform(0, 2*math.pi)
        r = self.r * math.sqrt(random.uniform(0, 1))
        return [self.x + r*math.cos(theta), self.y + r*math.sin(theta)]
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()
