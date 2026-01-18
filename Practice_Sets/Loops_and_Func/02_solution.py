n = int(input("Enter value of n: "))

# MULTI-LINE COMMENT # ALSO BE USED AS MULTI-LINE STRING
"""
  *
 ***
*****
"""
# "*" --> 2(total_rows) - 1 # odd-series
# " " --> (total_rows) - (row_val)


# MY-WAY
for i in range(1,n+1):
    for k in range(i,n): # i to n-1
        print(" ",end="")
    for j in range(i): # 0 to i-1 # we can do (1,n+1) --> 1 to n # still same work
        print("*",end=" ")
    print()


# BHAI-WAY
for i in range(1,n+1):
    print(" " * (n-i),end="")
    print("*" * ((2*i) -1),end="")
    print()
