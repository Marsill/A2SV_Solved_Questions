from collections import Counter

t = int(input())

for _ in range(t):
    
    source = input()
    target = input()
    
    target_freq = Counter(target)
    source_freq = Counter(source)
    
    result = []
    remaining_chars = []
    
    if all(source_freq[ch] <= target_freq[ch] for ch in source):
        
        for ch in source_freq:
            target_freq[ch] -= source_freq[ch]
        
        sorted_chars = sorted(target_freq.keys())
        i = 0
        j = 0
        
        for ch in sorted_chars:
            for _ in range(target_freq[ch]):
                remaining_chars.append(ch)
        
        while i < len(source) and j < len(remaining_chars):
            if source[i] <= remaining_chars[j]:
                result.append(source[i])
                i += 1
            else:
                result.append(remaining_chars[j])
                j += 1
        
        result.extend(source[i:])
        result.extend(remaining_chars[j:])
        
        print("".join(result))
    
    else:
        print("Impossible")