'''This is a tournament game and is team-based and each team can have N members. A player can fight against a single player only.
Input Format:
The first line of input consists of the number of test cases, T

The first line of each test case consists of the number of members each team can have, N.

The second line of each test case consists of N space-separated integers representing the power of beyblades of Team G-Revolution members.


The third line of each test case consists of N space-separated integers representing the power of beyblades of opponent team members.
Output Format:
For each test case, print the maximum number of fights Team G-Revolution can win if they go to fight in an optimal manner.
SAMPLE TEST CASE
Input:
1
10
3 6 7 5 3 5 6 2 9 1 
2 7 0 9 3 6 0 6 2 6 

Output:
7

'''
def main():
    n=int(input())
    for i in range(n):
      tc()
def tc():
    c=int(input())
    row1=input().split()
    row1=list(map(int,row1))
    row2=input().split()
    row2=list(map(int,row2))
    
    r1=sorted(row1)
    r2=sorted(row2)
    
    count=0
  
    for j in r2:
      for i in r1:
        if i>j:
          # print(i)
          count=count+1
          r1.remove(i)
          break 
    print(count)

main()
