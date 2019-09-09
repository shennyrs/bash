#enumerate used for numbering or indexing the members in the lst

def main():
    months=["jan","feb","mar","apr","may","jun","jul","aug","sep","oct","nov","dec"]
    for i,j in enumerate(months):
        print(i,j)
        
main()

#result will look like this
# 0 jan
# 1 feb
# 2 mar
# 3 apr
# 4 may
# 5 jun
# 6 jul
# 7 aug
# 8 sep
# 9 oct
# 10 nov
# 11 dec