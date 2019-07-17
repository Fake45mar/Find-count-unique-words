def count_unique_elements():
	sentence = input("Enter a sentence: ")
	splited_sentence = []
	unique_elements = []
	elements_that_should_delete = ['.', ',', ':', ';', '\\', '/']
	counter = 0
	for elem in sentence.split(" "):

		for char in elem:

			if char in elements_that_should_delete:
				past = elem[:counter]
				entry = elem[counter + 1:]
				elem = entry + past
			counter = counter + 1
		counter = 0
		splited_sentence.append(elem.lower())
	count = 0

	for elem in splited_sentence:

		for same_elem in splited_sentence[1:]:

			if elem == same_elem and same_elem not in unique_elements:
				unique_elements.append(same_elem)
	print(len(unique_elements))


if __name__ == '__main__':
	count_unique_elements()
