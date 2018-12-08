def largest_of_four(array):
	"""Return an array consisting of the largest
	   number from each provided sub-array"""
	largest_of_each = []

	for sub_array in array:
		largest_number = 0

		for number in sub_array:
			if number > largest_number:
				largest_number = number

		largest_of_each.append(largest_number)

	return largest_of_each


print(largest_of_four([[4, 5, 1, 3],
					   [13, 27, 18, 26],
					   [32, 35, 37, 39],
					   [1000, 1001, 857, 1]]))