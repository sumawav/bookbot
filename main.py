import sys
from stats import get_num_words
from stats import make_dictionary
from stats import pretty_report

def get_book_text(file_path):
	with open(file_path) as f:
		file_contents = f.read()
		return file_contents

def main():
	if len(sys.argv) < 2:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)
	book_path = sys.argv[1]	
	text = get_book_text(book_path)
	num_words = get_num_words(text)
	dictionary = make_dictionary(text)



	print(f"============ BOOKBOT ============")
	print(f"Analyzing book found at {book_path}...")
	print(f"----------- Word Count ----------")
	print(f"Found {num_words} total words")
	print(f"--------- Character Count -------")
	pretty_report(dictionary)
	print(f"============= END ===============")
main()
