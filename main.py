from stats import get_number_words
import sys

def main():

  def get_number_characters(text):
  
    lower_str = text.lower()
    dict_char = {}
    list_char = []
  
    for char in lower_str:
      if char.isalpha():
        if char in dict_char:
          dict_char[char] += 1
        else:
          dict_char[char] = 1
    
    for char in dict_char:
      list_char.append({"letter":char, "num":dict_char[char]})
    
    return list_char
      

  def sort_on(dict):
    return dict["num"]

  def get_report(letters_list, book_path, words_count):
    letters_list.sort(key=sort_on, reverse=True)
  
    print(f"============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {words_count} total words")
    print("--------- Character Count -------")
    for letter in letters_list:
      print(f"{letter["letter"]}: {letter["num"]}")
    print("============= END ===============")
  
  with open(sys.argv[1]) as file:
    file_content = file.read()
    letters_list = get_number_characters(file_content)
    words_count = get_number_words(file_content)
    book_path = sys.argv[1]
    get_report(letters_list, book_path, words_count)

if sys.argv.__len__() < 2:
  print("Usage: python3 main.py <path_to_book>")
  sys.exit(1)
else:
  main()