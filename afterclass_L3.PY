# 1. Define a sample string
text = "  Hello, Python Programming World!  "
print(f"Original Text: '{text}'")

# 2. Strip whitespaces
# Removes leading and trailing spaces from the text
cleaned_text = text.strip()
print(f"Cleaned Text: '{cleaned_text}'")

# 3. String Length
# Counts the total number of characters
length = len(cleaned_text)
print(f"Length of Text: {length}")

# 4. Case Transformations
print(f"Uppercase: '{cleaned_text.upper()}'")
print(f"Lowercase: '{cleaned_text.lower()}'")

# 5. String Slicing [start:end:step]
# Extracts "Python" (from index 7 up to 13)
slice_word = cleaned_text[7:13]
print(f"Sliced Word: '{slice_word}'")

# Reverses the entire cleaned string
reversed_text = cleaned_text[::-1]
print(f"Reversed Text: '{reversed_text}'")

# 6. Search and Count
# Checks if a substring exists inside the string
has_python = "Python" in cleaned_text
print(f"Contains 'Python'?: {has_python}")

# Counts occurrences of a specific letter
count_o = cleaned_text.count("o")
print(f"Count of letter 'o': {count_o}")

# 7. Replace Substring
# Replaces 'World' with 'Universe'
new_text = cleaned_text.replace("World", "Universe")
print(f"Replaced Text: '{new_text}'")

# 8. Split and Join
# Splits the string into a list of words using space as a delimiter
words_list = cleaned_text.split(" ")
print(f"Split into List: {words_list}")

# Joins the list back into a single string using a hyphen
joined_text = "-".join(words_list)
print(f"Joined with Hyphens: '{joined_text}'")
