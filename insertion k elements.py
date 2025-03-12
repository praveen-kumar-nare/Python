import random

test_list = [5, 7, 4, 2, 8, 1]

print("The original list : " + str(test_list))

add_list = ["praveen", "kill the boy", "men will be born"]

K = 3

for idx in range(K):
	index = random.randint(0, len(test_list))
	test_list = test_list[:index] + [random.choice(add_list)] + test_list[index:]

print("The created List : " + str(test_list))