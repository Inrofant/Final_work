def filter_short_strings(strings):
    short_strings = []
    for string in strings:
        if len(string) <= 3:
            short_strings.append(string)
    return short_strings

def main():
    strings = input("Введите строки, разделенные пробелом: ").split()
    filtered_strings = filter_short_strings(strings)
    print("Строки длиной не более 3 символов:")
    for string in filtered_strings:
        print(string)

if __name__ == "__main__":
    main()