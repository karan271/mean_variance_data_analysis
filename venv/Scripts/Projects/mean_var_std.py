import numpy as np
import pandas as pd

def calculate(nums):
    if len(nums) < 9:
        raise ValueError ('List must contain nine numbers!')
    else:
        nums = np.array(nums)

    nums1 = nums.reshape((3,3))

    calc = {
        'mean': [np.mean(nums1, 0).tolist(), np.mean(nums1, 1).tolist(), np.mean(nums1).tolist()],
        'variance': [np.var(nums1, 0).tolist(), np.var(nums1, 1).tolist(), np.var(nums1).tolist()],
        'standard deviation': [np.std(nums1, 0).tolist(), np.std(nums1, 1).tolist(), np.std(nums1).tolist()],
        'max': [np.max(nums1,0).tolist(), np.max(nums1, 1).tolist(), np.max(nums1).tolist()],
        'min': [np.min(nums1,0).tolist(), np.min(nums1, 1).tolist(), np.min(nums1).tolist()],
        'sum': [np.sum(nums1,0).tolist(), np.sum(nums1, 1).tolist(), np.sum(nums1).tolist()],
    }
    # for key, value in calc.items():
    #     print(f'{key}: {value}')
    return calc

print(calculate([0,1,2,3,4,5,6,7,8]))