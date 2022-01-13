class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points = sorted(points, key=lambda x: x[1])
        # Sort points based of Xend
        
        arrow = 0
        end = -float('inf')
        
        for i in points:
            if i[0] > end:      # If the current end is greater than end, it means shooting an arrow can brust the baloon
                arrow += 1      # Incrementing arrow
                end = i[1]      # Updating end
                
        return arrow
        