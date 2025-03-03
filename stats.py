def get_num_words(text):
	num_words = len(text.split())
	return num_words

def make_dictionary(text):
	dictionary = {}
	for char in text:
		lower_char = char.lower()
		if lower_char not in dictionary:
			dictionary[lower_char] = 1
		else:
			dictionary[lower_char] += 1

	return dictionary

def pretty_report(dictionary):
	sorted_dict = {k: v for k, v in sorted(dictionary.items(), key=lambda item: item[1], reverse=True)}
	for k in sorted_dict:
		if k.isalpha():
			print(f"{k}: {sorted_dict[k]}")
