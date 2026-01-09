# Dictionary 
# Word Frequency Counter - Text Analysis


def word_frequency(text):
    # Clean and split text
    words = text.lower().replace(",", "").replace(".", "").split()
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    
    return freq


def top_k_words(freq, k):
    sorted_words = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    return sorted_words[:k]


def find_unique_words(freq): #Find words that appear only once
    return [word for word, count in freq.items() if count == 1]

if __name__ == "__main__":
    print("REAL-WORLD: Word Frequency Analysis")
    
    text = """
    Python is a great programming language. 
    Python is easy to learn. Python is used for web development, 
    data science, machine learning and automation. 
    Data science and machine learning are growing fields.
    """
    
    print("\n📝 Input Text:")
    print(text.strip())
    
    # Get word frequency
    freq = word_frequency(text)
    print("\n Word Frequency:")
    for word, count in sorted(freq.items()):
        print(f"   '{word}': {count}")
    
    # Top 5 words
    print("\n Top 5 Most Frequent Words:")
    for word, count in top_k_words(freq, 5):
        print(f"   '{word}' → {count} times")
    
    # Unique words
    unique = find_unique_words(freq)
    print(f"\n Unique Words (appear once): {unique}")
    
