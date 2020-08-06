# Remove Duplicates from Sorted Array
# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/727/
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # 길이가 0 이하인 경우
        if len(nums) == 0:
            return 0;
        idx = 1
        prev = nums[0]
        for i in range(1, len(nums)):
            if nums[i] == prev :
                continue
            else:
                nums[idx] = nums[i]
                prev = nums[i]
                idx += 1       
        return idx 
'''
    참고자료
    파이썬 중복 제거
    - https://bluese05.tistory.com/13
    in-place 정렬
    https://azza.tistory.com/entry/C-%EB%A1%9C-%EA%B5%AC%ED%98%84%ED%95%9C-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-3%EB%B6%80-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-12%EC%9E%A5-%EC%A0%95%EB%A0%AC%EA%B3%BC-%ED%83%90%EC%83%89
''' 