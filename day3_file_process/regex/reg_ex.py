# import re
# # # Example 1: Matching a simple pattern
# # pattern = r'\d+'  # Matches one or more digits
# # text = "There are 123 apples"
# # match = re.search(pattern, text)
# # if match:
# #     print(f"Found a match: {match.group()}")  # Output: Found a match: 123

# # Example 2: Matching an email address
# # Matches an email address
# # pattern = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
# # text = "Please contact us at support@example.com"
# # match = re.search(pattern, text)
# # if match:
# #     # Output: Found a match: support@example.com
# #     print(f"Found a match: {match.group()}")

# # # Example 3: Finding all matches
# # pattern = r'\b\w{4}\b'  # Matches words with exactly 4 letters
# # text = "This is a test text with some four letter words like this and that"
# # matches = re.findall(pattern, text)
# # # Output: Found matches: ['This', 'test', 'text', 'with', 'some', 'four', 'like', 'this', 'that']
# # print(f"Found matches: {matches}")

# # # Example 4: Replacing text
# # pattern = r'\bfoo\b'  # Matches the word 'foo'
# # text = "foo is a placeholder word"
# # new_text = re.sub(pattern, 'bar', text)
# # # Output: Replaced text: bar is a placeholder word
# # print(f"Replaced text: {new_text}")

# # # Example 5: Splitting text
# # pattern = r'\s+'  # Matches one or more whitespace characters
# # text = "Split this text into words"
# # words = re.split(pattern, text)
# # # Output: Splitted words: ['Split', 'this', 'text', 'into', 'words']
# # print(f"Splitted words: {words}")

# # str = "steve 3434 joe555"
# # pattern = 'steve '
# # match = re.findall('[0-9]', str)
# # # match1 = re.findall(pattern, str)
# # print(match)
# # # print(match1)
# # import re


# # def is_valid_phone_number(phone_number):
# #     # Regex pattern to match a 10-digit phone number starting with 6, 7, 8, or 9
# #     pattern = r'^[6789]\d{9}$'
# #     return re.match(pattern, phone_number) is not None


# # # Take user input from the console
# # phone_number = input("Enter a 10-digit phone number: ")

# # # Check if the phone number is valid
# # if is_valid_phone_number(phone_number):
# #     print("The phone number is valid.")
# # else:
# #     print("The phone number is invalid.")

# # Take user input from the console
# email = input("Enter an email address: ")

# # Check if the email address is valid
# pattern = r'[a-z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
# if re.match(pattern, email):
#     print("The email address is valid.")
# else:
#     print("The email address is invalid.")
import re
import urllib
import urllib.request
import ssl

ssl._create_default_https_context = ssl._create_stdlib_context

# ctx=ssl.
u = urllib.request.urlopen(
    "https://www.redbus.in/info/contactus", context=None)
text = u.read()
pattern = "[0-9]{12}"
num = re.findall(pattern, str(text))
for n in num:
    print(num)
