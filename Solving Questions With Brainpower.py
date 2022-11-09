class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        maxContribution = [0]
        for pt, bp in reversed(questions):
            contribution = pt if bp > len(maxContribution)-1 else pt+maxContribution[-(bp+1)]
            maxContribution.append(max(maxContribution[-1], contribution))
        return maxContribution[-1]
