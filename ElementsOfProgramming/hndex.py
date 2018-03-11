# Find the h-index for this author, which is the largest number of
# publlications, h, where the number of citations is at least h.

citations = [1,4,1,4,2,1,3,5,6]

h = 0
count = 0

while True:
    for i in range(len(citations)):
        if h <= citations[i]:
            count += 1

    if count > h:
        count = 0
        h += 1
    else:
        break


print(h)


# Faster n(log(n)) algorithm

citations.sort()
h = 0
i = len(citations)-1
while i>0:
    if h > citations[i]:
        break
    h+=1
    i-=1

print('faater version: ', h)