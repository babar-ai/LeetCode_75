    if len(word1) != len(word2):
        while left < right:
            new_str += word1[left]
            new_str += word2[left]
            left += 1

        new_str += word1[right]
        new_str += word2[right]

        if len(word2) > len(word1):
            dif = len(word2) - len(word1)
    
            while dif < len(word2):
                new_str += word2[dif]
                dif += 1
            
            return new_str