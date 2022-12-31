def text_indentation(text):
    if type(text) is not str: 
        raise TypeError("text must be a string")
    else:
        count = 0
        for i in text:
            count+=1
        j = 0
        while j < count:
            if text[j] == "." or text[j] == "?" or text[j] == ":":
                print(text[j],"\n\n",end="")
            else:
                print(text[j],end="")
            j+=1