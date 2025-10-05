<<<<<<< HEAD
text = """This is a sample text for analysis. It contains multiple sentences and various words. Some words are repeated to test the frequency analysis. This tool helps writers understand their writing style and improve readability."""

chars_With_Spaces = len(text)
spaces_Count = text.count(" ")
chars_without_spaces = chars_With_Spaces - spaces_Count
sentences_Count = text.count(".")
Words_Count = len(text.split())
Avg_Word_Length = chars_without_spaces / Words_Count
Avg_Words_per_Sentence = Words_Count / sentences_Count


print(f"-Characters with spaces are:{chars_With_Spaces} chars.")
print(f"-Blankt spaces count:{spaces_Count}")
print(f"-Characters without spaces:{chars_without_spaces}")
print(f"-Sentences count:{sentences_Count}")
print(f"-Words count:{Words_Count}")
print(f"-Average word length is:{round(Avg_Word_Length, 2)} characters.")
print(f"-Avrage words per sendance is:{Avg_Words_per_Sentence} words.")

# text2 = ["Ali.", "Menna."]


# remove dots to enable detect similar words
def remove_dots(txt):
    for i in range(0, len(txt)):
        if txt[i][-1] == ".":
            txt[i] = txt[i][:-1]
    return txt


def common_words_detecter(txt):
    text_in_lower_case = txt.lower()
    txt_in_list = text_in_lower_case.split()
    txt_without_dots = remove_dots(txt_in_list)
    # create dictionary and every word turn to a key and the vlaue represent
    # how many time repteated
    common_words_dic = {}
    for word in txt_without_dots:
        if word in common_words_dic:
            common_words_dic[word] = common_words_dic.get(word) + 1
        else:
            common_words_dic[word] = 1

    return common_words_dic


res = common_words_detecter(text)
converted = sorted(res.items(), key=lambda item: item[1], reverse=True)
sorted = dict(converted)

print(sorted)
print("#" * 40)

print(common_words_detecter(text))


# text_list_lower = text.lower().split()

# for word in words:
#     if word[-1] == ".":
#         word = word[]
# print(words)

# words = ["Ali", "Hassen", "Ali", "Ali", "Hassen", "Menna", "Alaa", "Hussien"]
# names = {}
# index = 1
# for word in words:
#     if word in names:
#         names[word] = names.get(word) + 1

#     else:
#         names[word] = 1
# print(names)

lines = """ mmmmmmmmdsmm.ssdsdsdmsmmsmmdmmsm.
sdhshhshhshhhhhhdhshhs.
hssmmsssss.ssmmmsmmsmsms.
smmsmsmmsmmsmmsmmsmsmmsmsm

hshshhhhhs.

"""
# splitlines = text.splitlines()
# print(splitlines)
=======
text = """This is a sample text for analysis. It contains multiple sentences and various words. Some words are repeated to test the frequency analysis. This tool helps writers understand their writing style and improve readability."""

chars_With_Spaces = len(text)
spaces_Count = text.count(" ")
chars_without_spaces = chars_With_Spaces - spaces_Count
sentences_Count = text.count(".")
Words_Count = len(text.split())
Avg_Word_Length = chars_without_spaces / Words_Count
Avg_Words_per_Sentence = Words_Count / sentences_Count


print(f"-Characters with spaces are:{chars_With_Spaces} chars.")
print(f"-Blankt spaces count:{spaces_Count}")
print(f"-Characters without spaces:{chars_without_spaces}")
print(f"-Sentences count:{sentences_Count}")
print(f"-Words count:{Words_Count}")
print(f"-Average word length is:{round(Avg_Word_Length, 2)} characters.")
print(f"-Avrage words per sendance is:{Avg_Words_per_Sentence} words.")

# text2 = ["Ali.", "Menna."]


# remove dots to enable detect similar words
def remove_dots(txt):
    for i in range(0, len(txt)):
        if txt[i][-1] == ".":
            txt[i] = txt[i][:-1]
    return txt


def common_words_detecter(txt):
    text_in_lower_case = txt.lower()
    txt_in_list = text_in_lower_case.split()
    txt_without_dots = remove_dots(txt_in_list)
    # create dictionary and every word turn to a key and the vlaue represent
    # how many time repteated
    common_words_dic = {}
    for word in txt_without_dots:
        if word in common_words_dic:
            common_words_dic[word] = common_words_dic.get(word) + 1
        else:
            common_words_dic[word] = 1

    return common_words_dic


res = common_words_detecter(text)
converted = sorted(res.items(), key=lambda item: item[1], reverse=True)
sorted = dict(converted)

print(sorted)
print("#" * 40)

print(common_words_detecter(text))


# text_list_lower = text.lower().split()

# for word in words:
#     if word[-1] == ".":
#         word = word[]
# print(words)

# words = ["Ali", "Hassen", "Ali", "Ali", "Hassen", "Menna", "Alaa", "Hussien"]
# names = {}
# index = 1
# for word in words:
#     if word in names:
#         names[word] = names.get(word) + 1

#     else:
#         names[word] = 1
# print(names)

lines = """ mmmmmmmmdsmm.ssdsdsdmsmmsmmdmmsm.
sdhshhshhshhhhhhdhshhs.
hssmmsssss.ssmmmsmmsmsms.
smmsmsmmsmmsmmsmmsmsmmsmsm

hshshhhhhs.

"""
# splitlines = text.splitlines()
# print(splitlines)
>>>>>>> fb12890 (Add grade caluclator)
