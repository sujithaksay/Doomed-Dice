def calculate_sums(die_a, die_b):
    return [a + b for a in die_a for b in die_b]

def undoom_dice(Die_A, Die_B):
    # Calculate original probabilities
    original_sums = calculate_sums(Die_A, Die_B)
    original_probabilities = {sum_val: original_sums.count(sum_val) / len(original_sums) for sum_val in set(original_sums)}

    # Initialize new dice configurations
    New_Die_A = [1,4,0,0,0,0]
    New_Die_B = [1,8,0,0,0,0]
    a1,a2,a3,a4=2,2,2,2
    for i in range(0,5):
        if(i==1):
            a1+=1
        if(i==2):
            a2+=1
        if(i==3):
            a3+=1
        if(i==4):
            a4+=1
        New_Die_A[2]=a1
        New_Die_A[3]=a2
        New_Die_A[4]=a3
        New_Die_A[5]=a4
        for x in range(2,8):
            for y in range(2,8):
                C = [2,3,4,5,6,7]
                if(x==y):
                    continue
                else:
                     D = C
                     D.remove(x)
                     D.remove(y)
                     New_Die_B[2] = D[0]
                     New_Die_B[3] = D[1]
                     New_Die_B[4] = D[2]
                     New_Die_B[5] = D[3]
                     new_sums = calculate_sums(New_Die_A, New_Die_B)
                     new_probabilities = {sum_val: new_sums.count(sum_val) / len(new_sums) for sum_val in set(new_sums)}
                     # Check if the probabilities match
                     if new_probabilities == original_probabilities:
                         return New_Die_A, New_Die_B
    return [], []

# Example usage
Die_A = []
Die_B = Die_A
print("Enter the Die face values for Die A and Die B :")
for z in range(0,6):
    Die_A.append(int(input()))
Die_B = Die_A
print("Die A : ",Die_A)
print("Die B : ",Die_B)
print("\n")
New_Die_A, New_Die_B = undoom_dice(Die_A, Die_B)
print("New_Die_A:", New_Die_A)
print("\nNew_Die_B:", New_Die_B)
