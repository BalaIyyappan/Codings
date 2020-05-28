def main():
    n=int(input())
    row1=input().split()
    row1=list(map(int,row1))
    row2=input().split()
    row2=list(map(int,row2))
    result=[]
    for i in range(n):
      elem=row2[i]//row1[i]
      result.append(elem)
    print(min(result))
main()


'''
This is to calculate the number of products that can be manufactured with the given amount of resources
The first line of input consists:
Number of different products to be manufactured
Second line consists:
Quantity required to manufacture a single product
Third line consists:
The number of resources available for each product to be manufactured

Sample:
Input:
2
2 5 6 3
20 40 90 50
Output:
8

8 is the maximum number of products manufactured from the lot
'''
