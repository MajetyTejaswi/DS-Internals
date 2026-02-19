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
    
#Concepts
def twonums(nums, target):
    seen={}
    for i, x in enumerate(nums):
        need=target-x
        if need in seen:
            return [seen[need],i]
        seen[x]=i 
        
    return None
    
print(twonums([1,3,4,5,7],5))


def two_nums(nums, target):
    seen=set()
    for x in nums:
        need=target-x
        if need in seen:
            return [need,x]
        seen.add(x)
    return None
print


def validpara(s):
    stack=[]
    pairs={')':'(', ']':'['}
    for ch in s:
        if ch in "([":
            stack.append(ch)
        elif ch in pairs:
            if not stack or stack[-1]!=pairs[ch]:
                return False
            stack.pop()
    return not stack
    
print(validpara("([)]"))
    
    
    
def longstring(s):
    last={}
    left=0
    best=0
    
    for i, ch in enumerate(s):
        if ch in last and last[ch]>=left:
            left=last[ch]+1 
        last[ch]=i
        
        best=max(best, i-left+1)
    return best
    
print(longstring("abcdbc"))


def reversestring(s):
    word=s.split()
    return " ".join(reversed(word))
print(reversestring("tejaswi majety"))


def reverseletter(s):
    return s[::-1]
print(reverseletter("LOVE"))

def reverse_each_word(s):
    return " ".join(w[::-1] for w in s.split())
print(reverse_each_word("hello world"))

def mergelist(a,b):
    i=j=0
    out=[]
    while i<len(a) and j<len(b):
        if a[i]<b[j]:
            out.append(a[i])
            i+=1
        else:
            out.append(b[j])
            j+=1
    out.extend(a[i:])
    out.extend(b[j:])
    return out
print(mergelist([1,3,5],[2,4,6]))



def anagram(words):
    groups={}
    for w in words:
        key=tuple(sorted(w))
        groups.setdefault(key, []).append(w)
    return list(groups.values())
print(anagram(["eat","ate", "tan", "nat", "tea"]))

from collections import defaultdict
def anagram(word):
    group=defaultdict(list)
    for w in word:
        key="".join(sorted(w))
        group[key].append(w)
    return list(group.values())
print(anagram(["eat","ate", "tan", "nat", "tea", "yup"]))