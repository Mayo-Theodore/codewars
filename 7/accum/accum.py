class Accum():

    def capitalize(self, word):
        return word.upper()
    
    def hyphen(self, word):
        return '-'.join(word.upper())

    def accum(self, word):
        new_str = ""
        for index, w in enumerate(word.lower()):
            if w == word[0]:
                new_str += word[0].upper() + "-"
            else:
                new_str += word[index] * (index + 1) + "-"
        return new_str[:-1].title()
        

        #         for i in word:
        #     print(i)
        #     if i == word[-1]:
        #         new_str += word[word.index(i)] * (word.index(i) + 1)
        #     else:
        #         new_str += word[word.index(i)] * (word.index(i) + 1) + "-"
        # return new_str.title()






        # for i in word:
        #     print(i)
        #     if i == word[-1]:
        #         new_str += word[word.index(i)] * (word.index(i) + 1)
        #     else:
        #         new_str += word[word.index(i)] * (word.index(i) + 1) + "-"
        # return new_str.title()


        # for i in word:
        #     if word.index(i) > 2:
        #         print([char * 7 for char in word])
        # print("".join([char*3 for char in word]))
        # return ''.join([char*n for char in word])
         



        #     word = word[:word.index(i)] + i + word[word.index(i):]
        # return word
    
