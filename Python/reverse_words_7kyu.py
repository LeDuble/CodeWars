# Complete the function that accepts a string parameter, and reverses each word in the string. All spaces in the string should be retained.
# Examples

# "This is an example!" ==> "sihT si na !elpmaxe"
# "double  spaces"      ==> "elbuod  secaps"

# refactored version
def reverse_words(text):
    lst = [word[::-1] for word in text.split(" ")]
    return " ".join(lst)

# # initial version
# def reverse_words(text):
#     split_text = text.split(" ")
#     empty_list = []
#     for word in split_text:
#         word_reversed = word[::-1]
#         empty_list.append(word_reversed)
#     return " ".join(empty_list)