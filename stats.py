def get_word_count(text):
  word_list = text.split()
  return len(word_list)

def get_char_count(text):
  char_count_dict = {}
  for char in text:
    lower_char = char.lower()
    if lower_char not in char_count_dict:
      char_count_dict[lower_char] = 1
    else:
      char_count_dict[lower_char] += 1
  return char_count_dict

