#BANKER'S ALGORITHM
#SRISTI AGRAWAL (BT18GCS297)

process = int(input("Enter the No of processes: "))
Total = [10, 5, 7]
#mylist = [Pno. , allo1, allo2, allo3, max1, max2, max3 ]
#The mylist array will store data as above from the user input.

mylist = []
for i in range(process):
    process_no = input("Enter the Process No: ")
    allocation_1 = int(input("Enter the Allocation: "))
    allocation_2 = int(input("Enter the Allocation: "))
    allocation_3 = int(input("Enter the Allocation: "))
    max_1 = int(input("Enter the Max Need: "))
    max_2 = int(input("Enter the Max Need: "))
    max_3 = int(input("Enter the Max Need: "))

    mylist.append([process_no, allocation_1, allocation_2,
                allocation_3, max_1, max_2, max_3])

Arraysum = []  #This is the sum of your allocation from mylist array


for i in range(3):
    sum=0

    for j in range(len(mylist)):
        sum=sum+mylist[j][i+1]
    Arraysum.append(sum)

left = []
for i in range(len(mylist)):
    temp=[]
    for j in range(3):
        temp.append(mylist[i][j+4]-mylist[i][j+1])
    left.append(temp)

avail=[]
for i in range(3):
    avail.append(Total[i]-Arraysum[i])

def check(mylist):
    if len(mylist)!=0:
        return True
pro=[]

print("Process array is:")
print(mylist)

while check(mylist):
    for i in range(len(mylist)):
        if(avail[0]>=left[i][0] and avail[1]>=left[i][1] and avail[2]>=left[i][2]):
            pro.append("p"+ str(mylist[i][0]))
            avail[0]=avail[0]+mylist[i][1]
            avail[1] = avail[1] + mylist[i][2]
            avail[2] = avail[2] + mylist[i][2]
            mylist.remove(mylist[i])
            break
if len(pro)!=0:
    print("No deadlock will occur!")
    print("The sequence of the process is:")
    for i in range(len(pro)):
        print(pro[i])




