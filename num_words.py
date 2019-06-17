def convert_num_to_words(num):
    dt = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
           6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten',
           11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen',
           15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen',
           19: 'nineteen', 20: 'twenty', 30: 'thirty', 40: 'forty',
           50: 'fifty', 60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety'}

    if num < 0:
        print("invalid")

    if num < 20:
        return dt[num]

    elif num < 100:
        if num % 10 == 0:
            return dt[num]
        else:
            return dt[num // 10 * 10] + ' ' + dt[num % 10]
    elif num < 1000:
        if num % 100 == 0:
            return dt[num // 100] + ' hundred'
        else:
            return dt[num // 100] + ' hundred and ' + convert_num_to_words(num % 100)

    elif num < 100000:
        if num % 1000 == 0:
            return convert_num_to_words(num // 1000) + ' thousand'
        else:
            return convert_num_to_words(num // 1000) + ' thousand and ' + convert_num_to_words(num % 1000)
    elif num < 1000000:
        if num % 100000 == 0:
            return convert_num_to_words(num // 100000) + ' Lakh'
        else:
            return convert_num_to_words(num // 100000) + ' Lakh and ' + convert_num_to_words(num % 100000)
    elif num < 10000000:
        if num % 1000000 == 0:
            return convert_num_to_words(num // 1000000) + ' Million'
        else:
            return convert_num_to_words(num // 1000000) + ' Million and ' + convert_num_to_words(num % 1000000)
    elif num < 1000000000:
        if num % 100000000 == 0:
            return convert_num_to_words(num // 10000000) + ' Billion'
        else:
            return convert_num_to_words(num // 10000000) + ' Billion and ' + convert_num_to_words(num % 10000000)

if __name__ == "__main__":

    n = int(input("Enter a number : "))
    print(n, ":" ,convert_num_to_words(n))
