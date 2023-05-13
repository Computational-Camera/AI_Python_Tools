# input 1D array seperated by space " "
d_in = []
n = int(input())
data_input = input().split(" ")
for d in data_input:
    d_in.append(int(d))

# simple sort
data  = sorted(d_in)
    
# sort and return previous array index
sort_index = [i for i, x in sorted(enumerate(d_in), key=lambda x: x[1])]
    
