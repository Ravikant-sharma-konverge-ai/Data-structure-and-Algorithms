# Dynamic Programming

## Longest Common Subsequence
## Write a function to find the length of the longest common subsequence between two sequences. 
# E.g. Given the strings "serendipitous" and "precipitation", the longest common subsequence is "reipito" and its length is 7.
##A "sequence" is a group of items with a deterministic ordering. Lists, tuples and ranges are some common sequence types in Python.
##A "subsequence" is a sequence obtained by deleting zero or more elements from another sequence. For example, "edpt" is a subsequence of "serendipitous".

## recursive solution of above problem
def lcq_recursive(seq1, seq2, idx1=0, idx2=0):
    # Check if either of the sequences is exhausted
    if idx1 == len(seq1) or idx2 == len(seq2):
        return 0
    
    # Check if the current characters are equal
    if seq1[idx1] == seq2[idx2]:
        return 1 + lcq_recursive(seq1, seq2, idx1+1, idx2+1)
    # Skip one element from each sequence
    else:
        return max(lcq_recursive(seq1, seq2, idx1+1, idx2), 
                   lcq_recursive(seq1, seq2, idx1, idx2+1)) 


## memoized solution of above problem
def lcq_memoized(seq1, seq2):
    memo = {}
    
    def recurse(idx1, idx2):
        key = idx1, idx2
        
        if key in memo:
            return memo[key]
        
        if idx1 == len(seq1) or idx2 == len(seq2):
            memo[key] = 0
        elif seq1[idx1] == seq2[idx2]:
            memo[key] = 1 + recurse(idx1+1, idx2+1)
        else:
            memo[key] = max(recurse(idx1+1, idx2), 
                            recurse(idx1, idx2+1))
        return memo[key]
        
    return recurse(0, 0)

##Dynamic matrix solution of above problem
def lcq_dp(seq1, seq2):
    n1, n2 = len(seq1), len(seq2)
    results = [[0 for _ in range(n2+1)] for _ in range(n1+1)]
    for idx1 in range(n1):
        for idx2 in range(n2):
            if seq1[idx1] == seq2[idx2]:
                results[idx1+1][idx2+1] = 1 + results[idx1][idx2]
            else:
                results[idx1+1][idx2+1] = max(results[idx1][idx2+1], results[idx1+1][idx2])
    return results[-1][-1]


if __name__=='__main__':

    test0 = {
    'input': {
        'capacity': 165,
        'weights': [23, 31, 29, 44, 53, 38, 63, 85, 89, 82],
        'profits': [92, 57, 49, 68, 60, 43, 67, 84, 87, 72]
    },
    'output': 309
    }

    test1 = {
        'input': {
            'capacity': 3,
            'weights': [4, 5, 6],
            'profits': [1, 2, 3]
        },
        'output': 0
    }

    test2 = {
        'input': {
            'capacity': 4,
            'weights': [4, 5, 1],
            'profits': [1, 2, 3]
        },
        'output': 3
    }

    test3 = {
        'input': {
            'capacity': 170,
            'weights': [41, 50, 49, 59, 55, 57, 60],
            'profits': [442, 525, 511, 593, 546, 564, 617]
        },
        'output': 1735
    }

    test4 = {
        'input': {
            'capacity': 15,
            'weights': [4, 5, 6],
            'profits': [1, 2, 3]
        },
        'output': 6
    }

    test5 = {
        'input': {
            'capacity': 15,
            'weights': [4, 5, 1, 3, 2, 5],
            'profits': [2, 3, 1, 5, 4, 7]
        },
        'output': 19
    }


    tests = [test0, test1, test2, test3, test4, test5]

    #### Check test cases in all three mathds


## You’re in charge of selecting a football (soccer) team from a large pool of players. 
## Each player has a cost, and a rating. You have a limited budget. 
## What is the highest total rating of a team that fits within your budget. Assume that there’s no minimum or maximum team size.
## General problem statemnt:
## Given n elements, each of which has a weight and a profit, determine the maximum profit that can be obtained by selecting a subset of the elements weighing no more than w.



## recursive solution of above problem
def max_profit_recursive(capacity, weights, profits, idx=0):
    if idx == len(weights):
        return 0
    if weights[idx] > capacity:
        return max_profit_recursive(capacity, weights, profits, idx+1)
    else:
        return max(max_profit_recursive(capacity, weights, profits, idx+1),
                   profits[idx] + max_profit_recursive(capacity-weights[idx], weights, profits, idx+1))


## memoized solution of above problem
def knapsack_memo(capacity, weights, profits):
    memo = {}
    
    def recurse(idx, remaining):
        key = (idx, remaining)
        if key in memo:
            return memo[key]
        elif idx == len(weights):
            memo[key] = 0
        elif weights[idx] > remaining:
            memo[key] = recurse(idx+1, remaining)
        else:
            memo[key] = max(recurse(idx+1, remaining), 
                            profits[idx] + recurse(idx+1, remaining-weights[idx]))
        return memo[key] 
        
    return recurse(0, capacity)

##Dynamic matrix solution of above problem
def knapsack_dp(capacity, weights, profits):
    n = len(weights)
    results = [[0 for _ in range(capacity+1)] for _ in range(n+1)]
    
    for idx in range(n):
        for c in range(capacity+1):
            if weights[idx] > c:
                results[idx+1][c] = results[idx][c]
            else:
                results[idx+1][c] = max(results[idx][c], profits[idx] + results[idx][c-weights[idx]])
            
    return results[-1][-1]    


if __name__=='__main__':

    test0 = {
        'input': {
            'capacity': 165,
            'weights': [23, 31, 29, 44, 53, 38, 63, 85, 89, 82],
            'profits': [92, 57, 49, 68, 60, 43, 67, 84, 87, 72]
        },
        'output': 309
    }

    test1 = {
        'input': {
            'capacity': 3,
            'weights': [4, 5, 6],
            'profits': [1, 2, 3]
        },
        'output': 0
    }

    test2 = {
        'input': {
            'capacity': 4,
            'weights': [4, 5, 1],
            'profits': [1, 2, 3]
        },
        'output': 3
    }

    test3 = {
        'input': {
            'capacity': 170,
            'weights': [41, 50, 49, 59, 55, 57, 60],
            'profits': [442, 525, 511, 593, 546, 564, 617]
        },
        'output': 1735
    }

    test4 = {
        'input': {
            'capacity': 15,
            'weights': [4, 5, 6],
            'profits': [1, 2, 3]
        },
        'output': 6
    }

    test5 = {
        'input': {
            'capacity': 15,
            'weights': [4, 5, 1, 3, 2, 5],
            'profits': [2, 3, 1, 5, 4, 7]
        },
        'output': 19
    }



    tests = [test0, test1, test2, test3, test4, test5]

    #### Check test cases in all three mathds