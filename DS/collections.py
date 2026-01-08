# Collections Module - Deque
# Day 1: Sliding Window with Deque

from collections import deque


"""
DEQUE (Double-Ended Queue)
===========================
- Fast O(1) append/pop from BOTH ends
- maxlen: auto-removes oldest when full
- Perfect for sliding window problems
"""


def sliding_window_example():
    """
    Real-world: Moving average calculation (stock prices, metrics)
    """
    print("\n" + "=" * 50)
    print("Sliding Window - Moving Average")
    print("=" * 50)
    
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


# ============================================
# DEMO
# ============================================

if __name__ == "__main__":
    print("\n" + "█" * 50)
    print("DEQUE - Sliding Window")
    print("█" * 50)
    
    sliding_window_example()
    
    print("\n" + "█" * 50)
    print("✅ Key Takeaway:")
    print("   • deque with maxlen: perfect for sliding window")
    print("   • O(1) append, auto-removes oldest element")
    print("█" * 50 + "\n")

