'''
The goal of this problem is to implement a variant of the 2-SUM algorithm. The file contains 1
million integers, both positive and negative (there might be some repetitions). The ith row of
the file specifies the ith entry of the array.

The task is to compute the number of target values tt in the interval [-10000,10000] (inclusive)
such that there are distinct numbers x,yx,y in the input file that satisfy x+y=tx+y=t. (NOTE:
ensuring distinctness requires a one-line addition to the algorithm from lecture.)

Write your numeric answer (an integer between 0 and 20001) in the space provided.

OPTIONAL CHALLENGE: If this problem is too easy for you, try implementing your own hash table for
it. For example, you could compare performance under the chaining and open addressing approaches
to resolving collisions.
'''
import time


# input:
# output:
def two_sum():
    return None


def main():
    start = time.time()
    result = two_sum()
    print('result: ', result)
    print('elapsed time: ', time.time() - start)


main()
