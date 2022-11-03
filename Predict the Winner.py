class Solution:
    def minmax(self, game, turn):
        if len(game) == 1:
            return game[0] if turn == 1 else -game[0]
        else:
            score_diff_i = game[0] + self.minmax(game[1:], -turn) if turn == 1 else -game[0] + self.minmax(game[1:], -turn)
            score_diff_f = game[-1] + self.minmax(game[:-1], -turn) if turn == 1 else -game[-1] + self.minmax(game[:-1], -turn)
            return max(score_diff_i, score_diff_f) if turn == 1 else min(score_diff_i, score_diff_f)
            
    def PredictTheWinner(self, nums: List[int]) -> bool:
        score_difference = self.minmax(nums, 1)
        return True if score_difference >= 0 else False
