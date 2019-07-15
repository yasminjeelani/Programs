def checkvowels(st,vowel):
    result = [i for i in st if i in vowel]
    print("number of vowels: ",len(result))
    print(result)

if __name__ == "__main__":
    word = input("enter a word: ")
    vowel = "AaEeIiOoUu"
    checkvowels(word,vowel)