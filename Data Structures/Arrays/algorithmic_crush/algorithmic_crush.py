n, inputs = [int(n) for n in input().split(" ")]
list = [0]*(n+1)
for _ in range(inputs):
    x, y, incr = [int(n) for n in input().split(" ")]
    list[x-1] += incr
    if((y)<=len(list)): list[y] -= incr;
max = x = 0
for i in list:
    x=x+i;
        if(max<x): max=x;
print(max)

'''Let's try an example
Let's try to walk through an example. If we have 1 query and it wants to add 100 to elements 2 through 4 inclusive in a 7-element array, we want to have:
[0, 0, 100, 100, 100, 0, 0]
The idea is that we can represent this initially as:
[0, 0, 100, 0, 0, -100, 0]
It's important to realize that this above array is not our final answer. We will walk through the array from array[0] to array[6] to create our final answer. When we reach array[2], it basically tells us that every element from here and to the right of it (array[2] to array[6]) should have 100 added to them. When we reach array[5], it tells us the same thing, except that every element should have -100 added to it. By following these 2 rules, we get
array[0] = 0;
array[1] = 0;
array[2] = 0 + 100 = 100;
array[3] = 0 + 100 = 100;
array[4] = 0 + 100 = 100;
array[5] = 0 + 100 - 100 = 0;
array[5] = 0 + 100 - 100 = 0;
giving us the final array of
[0, 0, 100, 100, 100, 0, 0]
I hope this helps. It was challenging for me to explain.
Let me know if you have any questions.'''