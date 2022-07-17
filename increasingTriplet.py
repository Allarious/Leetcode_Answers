
from typing import List

class IncreasingTriplet:
    def find_increasing_triplet(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False

        smallest_number = nums[0]
        smallest_number_to_triplet = float("inf")

        for num in nums:
            if num > smallest_number_to_triplet:
                return True
            if num < smallest_number:
                smallest_number = num
            elif num > smallest_number:
                smallest_number_to_triplet = num

        return False




if __name__ == "__main__":
    print(IncreasingTriplet().find_increasing_triplet([1, 2, 3, 4, 5]))