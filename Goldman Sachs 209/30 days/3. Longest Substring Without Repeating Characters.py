
def lengthOfLongestSubstring(s: str) -> int:
    # Initialize a set to store characters in the current window
    charSet = set()
    left = 0  # Left pointer for the sliding window
    maxLength = 0  # Maximum length of substring without repeating characters
    
    for right in range(len(s)):  # Right pointer iterates over the string
        # If character is already in the set, shrink the window from the left
        while s[right] in charSet:
            charSet.remove(s[left])
            left += 1
        
        # Add the current character to the set
        charSet.add(s[right])
        
        # Update the maximum length
        maxLength = max(maxLength, right - left + 1)
    
    return maxLength

# test
s = 'abcabcdefabcdaaaaj'
print(lengthOfLongestSubstring(s))