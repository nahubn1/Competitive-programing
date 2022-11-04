class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        score, ptr1, ptr2 = 0, 0, len(tokens)-1
        while ptr1 <= ptr2:
            if tokens[ptr1] <= power:
                power -= tokens[ptr1]
                score += 1
                ptr1 += 1
            else:
                if score and ptr2 - ptr1 > 1:
                    score -= 1
                    power += tokens[ptr2]
                    ptr2 -= 1
                else:
                    break
        return score
