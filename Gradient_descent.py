def _Gradient(X,Y,n,B0,B1,A):
    
    print(f"Intersection B0 Initially : {B0}")
    
    print(f"Slope B1 Initially : {B1}")
    
    iter = int(input("Enter the no of Iteration : "))
    
    for _ in range(iter):
        Y_predicted  = []
        for i in range(n):
            
            Y_predicted.append(B0 + B1 * X[i])
         
        loss = 0.0
        for i in range(n):
            loss += (Y_predicted[i] - Y[i]) ** 2
        loss /= (2 * n)
            
        dB1 = 0.0 ## dE/dB1
        dB0 = 0.0 ## dE/dB0
        
        for i in range(n):
            error = Y_predicted[i] - Y[i]
            dB1 += error*X[i]
            dB0 +=error
    
        # Average
        dB1 /= n
        dB0 /= n
        
        B1 = B1 - A*dB1
        B0 = B0 - A*dB0
    
        
        print(f"Intercept B0 : {B0}")
        print(f"Slope B1     : {B1}")
        print(f"Loss         : {loss}")
        print()
def _main():
    n = int(input("Enter the number of Terms : "))
    X,Y = [],[]
    
    for i in range(n):
        X.append(float(input(f"Enter the Value of X{i+1} : ")))
        Y.append(float(input(f"Enter the Value of Y{i+1} : ")))
    B0 = float(input("Enter the Intersection B0 : "))
    B1 = float(input("Enter the Slope B1 : "))
    A = float(input("Enter the Learning Rate A(alpha) : "))
    
    _Gradient(X,Y,n,B0,B1,A)

_main()

