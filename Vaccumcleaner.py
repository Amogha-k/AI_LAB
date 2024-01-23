import numpy as np
from datetime import datetime

n=int(input('enter the n value: '))
print()
rooms=np.random.randint(0,2,(n,n))
print(rooms)
count=0
total_rooms=n*n
start=datetime.now()
for row in rooms:
    for room in range(len(row)):
        if row[room]==1:
            row[room]=0
            count +=1
end=datetime.now()
time_taken=end-start
print(f"{count} rooms are cleaned")
print(rooms)
perfomance=round((count/total_rooms)*100,2)
print(f"time_taken taken for cleaning rooms is:{time_taken}")
print()
print(f"the perfomance of the vaccum cleaner{perfomance}")