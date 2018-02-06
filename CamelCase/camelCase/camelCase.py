
def main():
    sentence = input('Enter your sentence: ')
    camelCased = camelCaseMethod(sentence)
    print(camelCased)


def camelCaseMethod(sentence):
    sentence = sentence.lower().title().replace(" ", '')
    sentence = sentence[0].lower() + sentence[1::]
    return sentence


if __name__ == '__main__':
    main()
