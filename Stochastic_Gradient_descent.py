
def Stochastic_gradient_descent(B0, B1, A, X, Y, n):


    print(f"\nInitial Values - B0: {B0}, B1: {B1}")
    print("-" * 60)

    iterations = int(input("Enter the number of Iterations (Epochs): "))
    print("-" * 60)
    
    for epoch in range(iterations):
        print(f"\n Epoch {epoch + 1} — Updates within this iteration:")
        print("-" * 60)

       
        for i in range(n):
            
            Y_pred = B0 + B1 * X[i]
            error = Y_pred - Y[i]
            loss = error ** 2

            
            dB0 = error
            dB1 = error * X[i]

         
            B0 = B0 - A * dB0
            B1 = B1 - A * dB1

          
            print(f"Update {i + 1}: B0 = {B0:.4f}, B1 = {B1:.4f}, Loss = {loss:.6f}")
            
    print("\n Training Complete")
    print(f"Final Values - B0: {B0:.4f}, B1: {B1:.4f}")
    print("-" * 60)


def main():
  
    
    n = int(input("Enter the number of data points: "))
    X, Y = [], []

    for i in range(n):
        X.append(float(input(f"Enter X{i + 1}: ")))
        Y.append(float(input(f"Enter Y{i + 1}: ")))

    print("\n--- Initialization ---")
    B0 = float(input("Enter the initial Intercept (B0): "))
    B1 = float(input("Enter the initial Gradient (B1): "))
    A  = float(input("Enter the Learning Rate (A): "))

    Stochastic_gradient_descent(B0, B1, A, X, Y, n)


main()
