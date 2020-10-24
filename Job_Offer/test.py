#  from IPython import embed; embed(colors="neutral")
from num import my_function

def get_random_numbers(size):
    """Return an array of random numbers with size: "size"."""
    from random import seed
    from random import random
    ret = []
    seed(1)
    i = 0
    while i < size:
        value = random()
        ret.append(value)
        i = i + 1
    return ret

def test(size):
    """Test the sorting algorithum with random numbers."""
    print "First test case:"
    arr = [5000000, 4366346346, 12411, 2141, 32, 5, 32, 32523523, 35325, 352]
    ret = my_function(arr)
    print ret

    print "\nReal world test case:"
    import time

    print "\nGenerating %d random numbers ..." % (size)
    start = time.time()
    num_arr = get_random_numbers(size)
    duration = time.time() - start
    print "Random number is generated in %f seconds" % (duration)

    print "\nSorting %d random numbers ..." % (size)
    start = time.time()
    ret = my_function(num_arr)
    duration = time.time() - start
    print "With current algorithm, the job is done in %f seconds" % (duration)
    print "Done"
    #  print ret

if __name__ == "__main__":
    SIZE = 1000

    import sys
    if (sys.argv.__len__() > 1):
        SIZE = int(sys.argv[1])

    test(SIZE)
