test_list = [[1,2,3], [0,9,7], [5, 4, 2], [2, 3, 9]]


print("The original list : " + str(test_list))

res = {test_list[0][ele] : test_list[ele + 1] for ele in range(len(test_list) - 1)}


print("The Assigned Matrix : " + str(res))