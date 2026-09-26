def operations(x_input : int, y_input : int, z_input : int, n : int):
    x_list = [number for number in range(x_input)]
    y_list = [number for number in range(y_input)]
    z_list = [number for number in range(z_input)]
        
    result : list[list[int]] = []
    x = 0
    y = 0
    z = 0
    stop = False
    index = 0
    while(stop is False):
        
        
        if x != max(x_list):
            result.append([x, y, z])
            x += 1
            index += 1
            
        if y != max(y_list):
            result.append([x, y, z])
            y += 1
            index += 1
            
        if z != max(z_list):
            result.append([x, y, z])
            z += 1
            index += 1
              
        if x == max(x_list) and y == max(y_list) and z == max(z_list):
            stop = True
        
    print(result) 
    print(f"{result}")
    
    
    
    
    
    

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    operations(x, y, z, n)
    print([[x, y] for x in [1, 2, 3] for y in [4, 5, 6]])
