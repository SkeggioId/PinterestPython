import random
import string

def generate_palindrome(length=5):
    # Generate the first half of the palindrome
    half = ''.join(random.choices(string.ascii_lowercase, k=length // 2))
    # Complete the palindrome by mirroring the first half
    # If the length is odd, include the middle character twice
    palindrome = half + (half[-1] + half[:-1])[::-1] if length % 2 else half[::-1]
    return palindrome

# Display the generated palindrome
print(generate_palindrome(5))
