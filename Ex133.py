'''import time

# Start Time
start_time = time.time()
print(start_time)

# Code to be timed
# Replace this section with your own code
for i in range(1, 1000001):
    pass

# End Time
end_time = time.time()
print(end_time)

# Calculate runtime
runtime = end_time - start_time

# Print the runtime
print("Runtime: ", runtime, "seconds")'''

from timeit import default_timer


def timer(n):
    start = default_timer()
    print(start)
    # some code here
    for row in range(0, n):
        print(row)
    print(default_timer() - start)


timer(5)
timer(15)




