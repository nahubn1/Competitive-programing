class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        list_ = []
        for x, y in points:
            list_.append([[x, y], x ** 2 + y ** 2])

        list_ = sorted(list_, key=lambda x: x[1])

        result = []
        for point, dist in list_:
            result.append(point)
            if len(result) == k:
                break
        return result
        
