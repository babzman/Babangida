#Number to Base 2 converter
def base2(num):
    c=[]
    b=num%2
    c.append(b)
    if num==1:
        return c
    else:

        return c +base2(num//2)
        
         
    
    
    
       

        
print(base2(45))
