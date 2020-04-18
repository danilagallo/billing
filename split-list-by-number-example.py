# file to debug and test the behavior for thread split

l = [x for x in range(5000)]
n = len(l)
number_threads = 4

increment = n//number_threads
print(increment)

i = 0
start = 0
end = increment
while i <= number_threads:
    print(l[start:end])
    start = end
    end += increment
    i += 1
