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
      

  def get_number_words(text):
    count = len(text.split())
    return count

  def sort_on(dict):
    return dict["num"]

  def get_report(letters_list, book_name, words_count):
    letters_list.sort(key=sort_on, reverse=True)
  
    print(f"--- Begin report of books/{book_name}.txt ---")
    print(f"{words_count} found in the document")
    for letter in letters_list:
      print(f"The '{letter["letter"]}' character was found {letter["num"]} times")
    print("--- End report ---")
  
  with open("file/location") as file:
    file_content = file.read()
    letters_list = get_number_characters(file_content)
    words_count = get_number_words(file_content)
    book_name = "frankenstein"
    get_report(letters_list, book_name, words_count)


main()
