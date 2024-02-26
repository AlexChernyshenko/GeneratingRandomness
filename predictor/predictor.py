import random

# step 1
min_length = 100
remaining_digits = min_length
learning_set = ''

print("Please provide AI some data to learn...")
print(f"The current data length is {len(learning_set)}, {remaining_digits} symbols left")
while remaining_digits > 0:
    print("Print a random string containing 0 or 1:")
    user_input = input("> ")
    user_input = user_input.split('>')[-1]

    filtered_input = ''.join(char for char in user_input if char in '01')

    learning_set += filtered_input
    remaining_digits = min_length - len(learning_set)

    if remaining_digits > 0:
        print(f"The current data length is {len(learning_set)}, {remaining_digits} symbols left")

print("Final data string:")
print(learning_set)


# step 2
def triad_follow_count(binary_str):
    counts = {'000': [0, 0], '001': [0, 0], '010': [0, 0], '011': [0, 0],
              '100': [0, 0], '101': [0, 0], '110': [0, 0], '111': [0, 0]}

    for i in range(len(binary_str) - 3):
        triad = binary_str[i:i + 3]
        next_char = binary_str[i + 3]
        if next_char == '0':
            counts[triad][0] += 1
        else:
            counts[triad][1] += 1
    return counts


#
#     for i, j in counts.items():
#         print(f"{i}: {j[0]},{j[1]}")
#
#
triad_counts = triad_follow_count(learning_set)

# step 3
balance = 1000
test_min_len = 4
remain_test = test_min_len
test_set = ''

print("You have $1000. Every time the system successfully predicts your next press, you lose $1.")
print("Otherwise, you earn $1. Print \"enough\" to leave the game. Let's go!")

while True:
    print("Print a random string containing 0 or 1:")
    test_input = input("> ")
    if test_input == "enough":
        break

    while len(test_input) < 4:
        test_input = input("Print a random string containing 0 or 1:")
    test_set = ''.join(char for char in test_input if char in '01')

    prediction = ''
    for i in range(len(test_set) - 3):
        current_triad = test_set[i:i+3]
        if triad_counts[current_triad][0] > triad_counts[current_triad][1]:
            prediction += '0'
        elif triad_counts[current_triad][0] < triad_counts[current_triad][1]:
            prediction += '1'
        else:
            prediction += str(random.randint(0, 1))

    print('predictions:')
    print(prediction)

    learning_set += test_set
    triad_counts = triad_follow_count(learning_set)

    correct_prediction = sum(1 for i in range(len(prediction)) if prediction[i] == test_set[i + 3])
    total_predictions = len(prediction)
    accuracy = round((correct_prediction / total_predictions) * 100, 2)

    balance -= (correct_prediction - (total_predictions - correct_prediction))

    print(f"Computer guessed {correct_prediction} out of {total_predictions} symbols right ({accuracy:.2f} %)")
    print(f"Your balance is now ${balance}")

print("Game over!")
