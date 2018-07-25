def sort_scores(unsorted_scores, HIGHEST_POSSIBLE_SCORE):
	count = [0] * (HIGHEST_POSSIBLE_SCORE + 1)

	for i in unsorted_scores:
		count[i] += 1

	sorted_scores = []
	for i in range(0, HIGHEST_POSSIBLE_SCORE):
		num = count[i]
		while num > 0:
			sorted_scores.append(i)
			num -= 1
	
	return sorted_scores


unsorted_scores = [77, 11, 99, 100, 88, 0, 22, 22, 66, 88, 44, 23, 4]
HIGHEST_POSSIBLE_SCORE = 100
print(sort_scores(unsorted_scores, HIGHEST_POSSIBLE_SCORE))