from collections import Counter
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        count, partitions, part_len, remaining, Set = Counter(s), [], 0, 0, set()
        for i in s:
            if i not in Set:
                remaining += count[i]
            Set.add(i)
            remaining -= 1
            part_len += 1
            if remaining == 0:
                partitions.append(part_len)
                part_len, remaining = 0, 0  #reset
                Set.clear()
        return partitions
