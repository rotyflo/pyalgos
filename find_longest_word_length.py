def find_longest_word_length(string):
	"""Return the length of the longest word in the provided sentence"""
	list_of_words = string.split(' ')

	longest = 0

	for word in list_of_words:
		if len(word) > longest:
			longest = len(word)

	return longest


print(find_longest_word_length(
	"The quick brown fox jumped over the lazy dog"))