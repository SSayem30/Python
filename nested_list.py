row1=[1,1,1]
row2=[1,1,1]
row3=[1,1,1]
matrix=[row1,row2,row3]
print(f"{row1}\n{row2}\n{row3}\n")
position=input("Enter the position where you want to hide money ")
rownum=int(position[0])
colomnum=int(position[1])
rowselected=matrix[rownum-1]
rowselected[colomnum-1]='x'
print(f"{row1}\n{row2}\n{row3}\n")