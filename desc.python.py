arr = [45.50, 35, 41.30, 55, 24];     
temp = 0;    
print("Elements of original array: ");    
for i in range(0, len(arr)):     
    print(arr[i]),
    
for i in range(0, len(arr)):    
    for j in range(i+1, len(arr)):    
        if(arr[i] < arr[j]):    
            temp = arr[i];    
            arr[i] = arr[j];    
            arr[j] = temp;    
     
print();    
         
print("Elements of array sorted in descending order: ");    
for i in range(0, len(arr)):     
    print(arr[i]),  
