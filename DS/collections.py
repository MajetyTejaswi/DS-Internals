# Collections Module - Deque & OrderedDict

from collections import deque, OrderedDict
"""
DEQUE (Double-Ended Queue)
===========================
- Fast O(1) append/pop from BOTH ends
- maxlen: auto-removes oldest when full
- Perfect for sliding window problems

ORDEREDDICT
===========
- Maintains insertion order (Python 3.7+ regular dict also does this)
- Useful for move_to_end() method - reorder items
"""


def sliding_window_example():
    """
     Moving average calculation (stock prices, metrics)
    """
    print("Sliding Window - Moving Average")
    prices = [100, 102, 98, 105, 110, 108, 115, 112]
    window_size = 3
    
    window = deque(maxlen=window_size)
    moving_averages = []
    
    print(f"Stock prices: {prices}")
    print(f"Window size: {window_size}\n")
    
    for i, price in enumerate(prices):
        window.append(price)
        if len(window) == window_size:
            avg = sum(window) / window_size
            moving_averages.append(avg)
            print(f"Day {i+1}: window={list(window)} → avg={avg:.2f}")
    
    print(f"\nMoving averages: {[f'{x:.2f}' for x in moving_averages]}")


def recent_items_example():
    """
    Recently accessed items (e.g., recent files, recent searches)
    """
    print("\nRecently Accessed Items")
    
    recent = OrderedDict()
    
    # Access items
    items = ["file1.txt", "file2.py", "file1.txt", "file3.md", "file2.py"]
    
    print(f"Access sequence: {items}\n")
    
    for item in items:
        if item in recent:
            recent.move_to_end(item)  # Move to most recent
        else:
            recent[item] = True
        
        # Keep only last 3
        if len(recent) > 3:
            oldest = next(iter(recent))
            recent.pop(oldest)
        
        print(f"Accessed '{item}' → Recent: {list(recent.keys())}")
    
    print(f"\nFinal recent items (newest first): {list(reversed(recent.keys()))}")


if __name__ == "__main__":
    print("=" * 50)
    print("COLLECTIONS MODULE")
    print("=" * 50)
    
    print("\n1. DEQUE - Sliding Window")
    print("-" * 50)
    sliding_window_example()
    
    print("\n" + "=" * 50)
    print("2. ORDEREDDICT - Recent Items")
    print("-" * 50)
    recent_items_example()
    
    print("\n" + "=" * 50)
    print("✅ Key Takeaways:")
    print("   • deque: perfect for sliding window, O(1) operations")
    print("   • OrderedDict: track recent items with move_to_end()")
    print("=" * 50)

 

