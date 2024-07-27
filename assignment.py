# String slicing in programming, specifically in Python, refers to accessing a portion (substring) of a string by specifying a range of indices. The syntax for slicing is string[start:end:step], where:

# start is the index where the slice begins inclusively.
# end is the index where the slice ends (exclusive).
# step is the interval between indices in the slice (optional).

# Basic examples:

s = 'Hello World!'

print(s[0:5])

# This slice starts at index 0 and ends at index 5 (not inclusive), returning the first five characters.

print(s[:5])   # Output: Hello
print(s[7:])   # Output: World!

# Omitting the start index defaults to 0.
# Omitting the end index defaults to the length of the string.

print(s[-6:-1])  # Output: World
print(s[-6:])    # Output: World!

print(s[0:5:2])

# The slice starts at index 0, ends at index 5, and takes every second character.

print(s[::-1]) 

# The step -1 reverses the string.

s = "abcdefgh"
print(s[::2])
#Extracts Every Second Character

print(s[1:7:2])  # Output: bdf

# Combining Start, End, and Step

print(s[5:2]) #output: empty string

# if start is greater than end with a positive step, the result is an empty string

# if step is 0, it raises a valueError because step cannot be 0

#PRACTICAL EXAMPLES

filename = 'document.txt'
extension = filename[-3:]

print(extension) #Output: txt

url = 'https://www.example.com'
protocol = url[0:5]
domain = url[12:]
print(protocol) #Output: https
print(domain) #Output: example.com

sentence = 'Goodbye, World!'

reversed_sentence  = ' '.join(word[::-1] for word in sentence.split())
print(reversed_sentence)






