def calculate_sums(die_a, die_b):
    return [a + b for a in die_a for b in die_b]

def undoom_dice(Die_A, Die_B):
    # Calculate original probabilities
    original_sums = calculate_sums(Die_A, Die_B)
    original_probabilities = {sum_val: original_sums.count(sum_val) / len(original_sums) for sum_val in set(original_sums)}

    # Initialize new dice configurations
    New_Die_A = [0] * 6
    New_Die_B = [0] * 6

    # Iterate through all possible combinations for New_Die_A and New_Die_B
    for a1 in range(1, 5):
        for a2 in range(1, 5):
            for a3 in range(1, 5):
                for a4 in range(1, 5):
                    for a5 in range(1, 5):
                        for a6 in range(1, 5):
                            New_Die_A = [a1, a2, a3, a4, a5, a6]

                            for b1 in range(1, 12):
                                for b2 in range(1, 12):
                                    for b3 in range(1, 12):
                                        for b4 in range(1, 12):
                                            for b5 in range(1, 12):
                                                for b6 in range(1, 12):
                                                    New_Die_B = [b1, b2, b3, b4, b5, b6]

                                                    # Calculate new probabilities
                                                    new_sums = calculate_sums(New_Die_A, New_Die_B)
                                                    new_probabilities = {sum_val: new_sums.count(sum_val) / len(new_sums) for sum_val in set(new_sums)}

                                                    # Check if the probabilities match
                                                    if new_probabilities == original_probabilities:
                                                        return New_Die_A, New_Die_B

    # If no valid configuration is found, return empty lists
    return [], []

# Example usage
Die_A = [1, 2, 3, 4, 5, 6]
Die_B = Die_A

New_Die_A, New_Die_B = undoom_dice(Die_A, Die_B)
print("New_Die_A:", New_Die_A)
print("New_Die_B:", New_Die_B)
