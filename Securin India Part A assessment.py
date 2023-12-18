def combinations(x):
    a=6
    for i in range(1,x,1):
        a=a*6
    return a 
def print_dice_combinations(num_dice, current_combination):
    if num_dice == 0:
        print(current_combination,end='\t')
    else:
        for i in range(1, 7):
            print_dice_combinations(num_dice - 1, current_combination + [i])
#no_of_faces_in_a_die is the variable that represents the number of faces in a die . The Number of faces in a die is 6 . So no = 6
no_of_faces_in_a_die = 6 
DieA = [1,2,3,4,5,6]
DieB = [1,2,3,4,5,6]
print("The number of spots or value on each faces of the dice is given as follows :")
print("\n[1,2,3,4,5,6]")
print("\nThe number of faces in a die = ",no_of_faces_in_a_die)
#no_of_dice is the variable that represents the number of dice used
no_of_dice = int(input("\nEnter the number of dice used :"))
print("\nThe number of dice used = ",no_of_dice)
print("\nThe Formula for the calculation of total combinations possible is given by :")
print("\n(Number of faces in a die)^(Number of dice used) i.e no_of_faces_in_a_die^no_of_dice")
total_no_of_combinations = combinations(no_of_dice)
print("\nThe total number of possible combinations = ",total_no_of_combinations)
print("\nAll possible combinations are :")
print_dice_combinations(no_of_dice, [])
total_sum = [a + b for a in DieA for b in DieB]
probabilities = {sum_val: total_sum.count(sum_val) / len(total_sum) for sum_val in set(total_sum)}
for i in range(2,12+1):
    print("The Probability of Sum ",i,"=",probabilities[i])
