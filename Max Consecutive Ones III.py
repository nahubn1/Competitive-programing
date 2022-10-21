        start = 0
        zeros_count = 0
        Max = 0
        for end in range(len(nums)):
            if nums[end] == 0:
                zeros_count += 1
            while zeros_count > k:
                if nums[start] == 0:
                    zeros_count -= 1
                start += 1
                
            Max = max(Max, end - start + 1)
            
        return Max
