def findWords(st, length):
    resultWords = []
    words = st.split()
    for word in words:
        if len(word) > length and "ef" in word:
            resultWords.append(word)

    result = ' '.join(resultWords)
    return result


length = 5
st = "big white yousef"

print(findWords(st, length))