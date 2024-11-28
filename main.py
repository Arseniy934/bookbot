def main():
    # file reading happens here
    with open("books/frankenstein.txt") as f:
        f_contents = f.read()
    # then we can use f_contents
    return f_contents

s = main()

def counter(s):
    book = s.split()
    return len(book)

def sym(s):
    st = s.lower()
    sl = {}
    for i in st:
        if i in sl:
            sl[i] +=1
        else:
            sl[i] = 1
    sl_list = list(sl.items())
    sorted_sl_list = sorted(sl_list, key = lambda item: item[1],reverse = True)
    sl1 = []
    for i in sorted_sl_list:
        if i[0].isalpha():
            sl1.append(i)
    
    for i in range(len(sl1)):
        character, count = sl1[i]
        print(f"The '{character}' character was found {count} times")


print('===Begin report of books/frankenstein.txt===')

print(f'{counter(s)} words found in the document')
sym(s)
print('===End report===')


