def isPalindrome(s):
    # Step 1: Remove non-alphanumeric characters and convert to lowercase
    cleaned_s = ''.join(char.lower() for char in s if char.isalnum())

    # Step 2: Check for Palindrome
    print(cleaned_s[:])
    print(cleaned_s[::])
    return cleaned_s == cleaned_s[::-1]

# Test cases
s = "race a car"
print(isPalindrome("race a car"))                  # Output: False
# print(isPalindrome(" "))                               # Output: True
