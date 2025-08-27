def count_vowels(text, vowel='aeiou'):
    count = 0
    for alpha in text:
       if alpha in vowel:
          count += 1
    #return count
    print(count)
count_vowels('python is fun')
