#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import List
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        new_list = set(nums)
        if len(nums) == len(new_list) :
            return False
        return True
    

def test_containsDuplicate():
    c = Solution()
    assert c.containsDuplicate([1,2,3,1]) == True
    assert c.containsDuplicate([1,2,3,4]) == False


if __name__ == "__main__":
    test_containsDuplicate()
