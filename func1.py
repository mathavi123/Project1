def funct2(sentence:str, letters:str):
    return set(sentence).intersection(set(letters))


print (funct2('mathavi', 'mathavi balaji'))
