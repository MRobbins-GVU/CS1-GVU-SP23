# HINT: You should not need to modify pig_latin at all.
def pig_latin(word):
    vowels = "aeiouAEIOU"
    first_letter = word[0]
    second_letter = word[1]
    
    # Option 1: Word starts with a consonant and a vowel
    if first_letter.upper() not in "AEIOU" and second_letter.upper() in "AEIOU":
        partial_word = word[1:]
        return partial_word + first_letter + "ay"
    
    # Option 2: Word starts with two consonants
    if first_letter not in vowels and second_letter not in vowels:
        partial_word = word[2:]
        return partial_word + first_letter + second_letter + "ay"
    
    # Option 3: Word starts with a vowel  
    if word[0] in vowels:
        return word + "way"
# HINT: You should not have to modify above here at all


def translate(phrase):
    split_phrase_list = phrase.split(" ")
    translated_phrase = ""
    
    #TODO use the for loop to go through 'split_phrase_list' word by word.
    for ? in ? :
        #TODO call pig_latin on the single word in the list, save the result to a variable
        
        #TODO add that variable to the end of translated_phrase, with a space
    
    #Hint: it is possible to do this with a list and then join, if you prefer.
    #       If so, ignore my hints about adding to translated_phrase, and 
    #       Add the translated words to a list instead. Either is fine.
    return translated_phrase
    
def main():

    phrase1 = "Hurray it is the end"
    print(translate(phrase1))

    phrase2 = "Keep being awesome"
    print(translate(phrase2))    
    
    #TODO: test your own phrase with at least one word that starts with two consonants 

    
    
    
main()
