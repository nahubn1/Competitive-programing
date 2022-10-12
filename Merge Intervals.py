class Solution:

    def intersection(self, intervals):
        for i1, inter1 in enumerate(intervals):
            for i2, inter2 in enumerate(intervals):
                if i1 == i2:
                    continue
                if self.overlaping(inter1, inter2):
                    return True
        return False

    @staticmethod
    def overlaping(intv1, intv2):
        if min(intv1) > max(intv2) or min(intv2) > max(intv1):
            return False
        else:
            return True

    @staticmethod
    def overlap(interv):
        list_ = []
        for i1, i2 in interv:
            list_.append(i1)
            list_.append(i2)
        return [min(list_), max(list_)]

    @staticmethod
    def del_rep(list_):
        result = []
        for x in list_:
            if x not in result:
                result.append(x)
        return result

    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        result = []
        if not self.intersection(intervals):
            result = intervals
        while self.intersection(intervals):
            iteration = 0
            result = []
            while len(intervals) > 0:
                iteration += 1
                intv1 = intervals[0]

                commons = [intv1]
                intervals.remove(intervals[0])

                for intv2 in intervals:
                    if self.overlaping(intv1, intv2):
                        commons.append(intv2)

                if len(commons) == 1:
                    result.append(commons[0])
                else:
                    result.append(self.overlap(commons))

                for i, x in enumerate(commons):
                    if i == 0:
                        continue
                    intervals.remove(x)
            intervals = result
        return result
