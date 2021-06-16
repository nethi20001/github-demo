# AddImplementation
def add(x,y):
    return x+y
    
#Subtract implementaion    
def subtract(x,y):
    return x-y      #On master branch
    
# Mul implementaion    
def multiply(x,y):
    return x*y        #On bug34 branch            
    
#Divide Implementation    
def divide(x,y):
    if x<0:
      return NEGATIVE_PARAM_ERROR #Master branch   
    if y==0:
      return DIVISION_BY_0_ERROR #on bug789 branch
    else:
        return x/y

