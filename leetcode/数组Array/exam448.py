#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:     2019/8/8 13:44
# @Author:   Domi
# @File:     exam448.py
# @Software: PyCharm

"""
448.《找到数组中消失的数》（easy）

题目：给定一个范围在1≤a[i]≤n(n=数组大小)的整型数组，数组中的元素一些出现了两次，另一些只出现一次。
找到所有在[1,n]范围之间没有出现在数组中的数字。
您能在不使用额外空间且时间复杂度为O(n)的情况下完成这个任务吗? 你可以假定返回的数组不算在额外空间内

思路：类比268，用集合的方法
"""


def find_disappeared_number(nums):
    return list(set(range(1, len(nums)+1))-set(nums))


print(find_disappeared_number([4, 3, 2, 7, 8, 2, 3, 1]))
