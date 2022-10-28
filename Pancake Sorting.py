class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        end = len(arr)
        flips = []
        while end > 0:
            k = arr.index(max(arr[:end])) + 1
            arr = list(reversed(arr[:k])) + arr[k:]
            arr = list(reversed(arr[:end])) + arr[end:]
            flips.append(k)
            flips.append(end)
            end -= 1
        return flips
