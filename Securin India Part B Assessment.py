def calculate_sums(die_a, die_b):
    return [a + b for a in die_a for b in die_b]

def undoom_dice(Die_A, Die_B):
    # Calculate original probabilities
    original_sums = calculate_sums(Die_A, Die_B)
    original_probabilities = {sum_val: original_sums.count(sum_val) / len(original_sums) for sum_val in set(original_sums)}

    # Initialize new dice configurations
    New_Die_A = [1,2,3,0,0,0]
    New_Die_B = [1,2,3,4,8,5]
    New_Die_C = [1,2,3,4,8,6]
    New_Die_D = [1,2,3,4,8,7]
    for a1 in range(1,5):
        for a2 in range(1,5):
            for a3 in range(1,5):
                New_Die_A[3]=a1
                New_Die_A[4]=a2
                New_Die_A[5]=a2
            
                new_sums = calculate_sums(New_Die_A, New_Die_B)
                new_probabilities = {sum_val: new_sums.count(sum_val) / len(new_sums) for sum_val in set(new_sums)}
                # Check if the probabilities match
                if new_probabilities == original_probabilities:
                    return New_Die_A, New_Die_B
    for a1 in range(1,5):
        for a2 in range(1,5):
            for a3 in range(1,5):
                New_Die_A[3]=a1
                New_Die_A[4]=a2
                New_Die_A[5]=a2
            
                new_sums = calculate_sums(New_Die_A, New_Die_C)
                new_probabilities = {sum_val: new_sums.count(sum_val) / len(new_sums) for sum_val in set(new_sums)}
                # Check if the probabilities match
                if new_probabilities == original_probabilities:
                    return New_Die_A, New_Die_C
    for a1 in range(1,5):
        for a2 in range(1,5):
            for a3 in range(1,5):
                New_Die_A[3]=a1
                New_Die_A[4]=a2
                New_Die_A[5]=a2
            
                new_sums = calculate_sums(New_Die_A, New_Die_D)
                new_probabilities = {sum_val: new_sums.count(sum_val) / len(new_sums) for sum_val in set(new_sums)}
                # Check if the probabilities match
                if new_probabilities == original_probabilities:
                    return New_Die_A, New_Die_D
   
                
    return [], []

# Example usage
Die_A = [1, 2, 3, 4, 5, 6]
Die_B = Die_A

New_Die_A, New_Die_B = undoom_dice(Die_A, Die_B)
print("New_Die_A:", New_Die_A)
print("New_Die_B:", New_Die_B)
