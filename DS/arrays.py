# Arrays - Two Pointer Technique
# Day 1: Opposite Ends Pattern (Left & Right Pointers)

from typing import List, Optional
def two_sum_sorted(arr: List[int], target: int) -> Optional[tuple]:
    """
    Find two numbers that sum to target in SORTED array.
    Time: O(n), Space: O(1)
    
    Logic: If sum < target, move left pointer right (need larger)
           If sum > target, move right pointer left (need smaller)
    """
    left, right = 0, len(arr) - 1
    
    while left < right:
        current_sum = arr[left] + arr[right]
        
        if current_sum == target:
            return (left, right)
        elif current_sum < target:
            left += 1      # Need larger sum
        else:
            right -= 1     # Need smaller sum
    
    return None


def valid_palindrome(s: str) -> bool:
    """
    Check if string is palindrome (ignore non-alphanumeric).
    Time: O(n), Space: O(1)
    
    Logic: Compare characters from both ends, move inward
    """
    left, right = 0, len(s) - 1
    
    while left < right:
        # Skip non-alphanumeric
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1
        
        if s[left].lower() != s[right].lower():
            return False
        
        left += 1
        right -= 1
    
    return True


def reverse_array_inplace(arr: List[int]) -> None:
    """
    Reverse array in-place using two pointers.
    Time: O(n), Space: O(1)
    
    Logic: Swap elements at left and right, move inward
    """
    left, right = 0, len(arr) - 1
    
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

if __name__ == "__main__":
    print("=" * 50)
    print("TWO POINTER - Opposite Ends Pattern")
    print("=" * 50)
    
    # Two Sum
    arr = [1, 2, 3, 4, 6]
    result = two_sum_sorted(arr, 6)
    print(f"\n1. Two Sum: {arr}, target=6")
    print(f"   Result: indices {result}")
    
    # Valid Palindrome
    s = "A man, a plan, a canal: Panama"
    print(f"\n2. Valid Palindrome: '{s}'")
    print(f"   Result: {valid_palindrome(s)}")
    
    # Reverse Array
    arr = [1, 2, 3, 4, 5]
    print(f"\n3. Reverse Array: {arr}")
    reverse_array_inplace(arr)
    print(f"   Result: {arr}")
    
  
