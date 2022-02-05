k = list(range(1,40))
  
a = (filter(lambda x: (x % 3 == 0), k)) 
b = (filter(lambda x: (x % 5 == 0), k))
list3=list(a) 
list5=list(b) 

  
print(list3,"This number only divisible by 3 \n") 
print(list5,"This number only divisible by 5")