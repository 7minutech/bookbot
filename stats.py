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

def sort_on(items):
  return items["num"]

def get_sorted_chars(chars_dict):
  chars_list_dict = []
  for k in chars_dict:
    v = chars_dict[k]
    tmp_dict = {}
    tmp_dict["char"] = k
    tmp_dict["num"] = v
    chars_list_dict.append(tmp_dict)
  chars_list_dict.sort(reverse=True, key=sort_on)
  return chars_list_dict
