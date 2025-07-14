from stats import get_word_count, get_char_count, get_sorted_chars
import sys  

def main():
  if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
  book_path = sys.argv[1]
  text = get_book_text(book_path)
  word_count = get_word_count(text)
  char_count = get_char_count(text)
  display_title(book_path)
  display_word_count(word_count)
  display_sorted_chars(get_sorted_chars(char_count))

def get_book_text(path_to_file):
  with open(path_to_file) as f:
    file_contents = f.read()
    return file_contents

def display_sorted_chars(sorted_chars):
  print("--------- Character Count -------")
  for char_dict in sorted_chars:
    char = char_dict["char"]
    num = char_dict["num"]
    if char.isalpha():
      print(f"{char}: {num}")
 
def display_title(book_path):
  print("============ BOOKBOT ============")
  print(f"Analyzing book found at {book_path}")

def display_word_count(word_count):
  print("----------- Word Count ----------")
  print(f"Found {word_count} total words")


main()
