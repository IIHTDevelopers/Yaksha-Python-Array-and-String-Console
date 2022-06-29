
def fetch_n_elements(arr,n):
    pass
    
if __name__=="__main__":
    str_elements=input("Enter space seperated array elements")
    str_array=str_elements.split()
    integer_map_obj = map(int,str_array)
    integer_array=list(integer_map_obj)
    n = int(input("Number of elements to fetch from array: "))
    L=fetch_n_elements(integer_array,n)
    print(' '.join(str(x) for x in L))
