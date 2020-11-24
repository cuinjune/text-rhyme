def text_from_sys_argv():
    import sys
    if len(sys.argv) == 1:
        print("Error: Please pass text as arguments.")
        exit()
    else:
        return sys.argv

# get text from system arguments
text_input = " ".join(text_from_sys_argv()[1:])
text_input_words = text_input.split()

# import pronouncing
import pronouncing

text_phones_list = list()

for w in text_input_words:
    rhymes = pronouncing.rhymes(w)
    if len(rhymes):
        text_phones_list.extend(rhymes)

# make it a unique list
text_phones_list = list(set(text_phones_list))

text_phones = " ".join(text_phones_list)

# parse text with spacy
import spacy
nlp = spacy.load('en_core_web_md')
doc_input = nlp(text_input)
doc_phones = nlp(text_phones)

# extract text units
words_input = [w for w in list(doc_input) if w.is_alpha]
entities_input = list(doc_input.ents)
words_phones = [w for w in list(doc_phones) if w.is_alpha]
entities_phones = list(doc_phones.ents)


import random

text_output = ""

for w in text_input_words:
    wt_found = [wt for wt in words_input if wt.text == w]
    et_found = [et for et in entities_input if et.text == w]
    found = False
    if len(wt_found):
        wt = wt_found[0]
        rhymes = pronouncing.rhymes(wt.text)
        random.shuffle(rhymes)
        for r in rhymes:
            rwt_found = [rwt for rwt in words_phones if rwt.text == r]
            if len(rwt_found):
                rwt = rwt_found[0]
                if rwt.pos_ == wt.pos_ and rwt.tag_ == wt.tag_:
                    t = rwt.text
                    if w[0].isupper():
                        t = t.capitalize()            
                    text_output = text_output + t + " "
                    found = True
                    break

    elif len(et_found):
        et = et_found[0]
        rhymes = pronouncing.rhymes(et.text)
        random.shuffle(rhymes)
        for r in rhymes:
            ret_found = [ret for ret in entities_phones if ret.text == r]
            if len(ret_found):
                ret = ret_found[0]
                if ret.label_ == et.label_:
                    t = ret.text
                    if w[0].isupper():
                        t = t.capitalize()
                    text_output = text_output + t + " "
                    found = True
                    break
    
    if found:
        continue
                
    text_output = text_output + w + " "



text_output = text_output[:-1]

print(text_output)



