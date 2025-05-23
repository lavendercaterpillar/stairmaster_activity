# From LeetCode: https://leetcode.com/problems/climbing-stairs/

# You are climbing a staircase. It takes n steps to reach the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

# Example 1:

# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps

# Example 2:

# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step


# basicalli it is Fibonacci series:

def climbStairs(n, memo = None):
        
        if n == 0 or n == 1:
            return 1

        memo = memo if memo is not None else {} 

        if n in memo:
            return memo[n]
        
        memo[n] = climbStairs(n-1, memo) + climbStairs(n-2, memo)
        
        return memo[n]


    # at each step, how many choices do we have?
    # given each choice, how many combinations of steps are left?
    # is there a threshold below which we have only a limited number of combinations?
    # what threshold, and how many combinations?


print(climbStairs(30))