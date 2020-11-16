import tkinter as tk
import spacy 
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation



root = tk.Tk()

root.geometry("500x450")





#mylabel= tk.Label(root, text='SUMMARY', )
#mylabel.pack(pady=20)




def clear():
    T.delete(1.0, tk.END)

def get_text():
    #mylabel.config(text=T.get(1.0, tk.END))
    text = T.get(1.0, tk.END)
    stopwords = list(STOP_WORDS)
    stopwords
    len(stopwords)
    nlp = spacy.load('en')
    docx = nlp(text)
    for token in docx:print(token.text) 
    word_frequencies = {}
    for word in docx:
            if word.text.lower() not in stopwords:
                if word.text.lower() not in punctuation:
                    if word.text not in word_frequencies.keys():
                        word_frequencies[word.text]=1
                    else:
                        word_frequencies[word.text]+=1
                            
    maximum_freq = max(word_frequencies.values())


    for word in word_frequencies.keys():
        word_frequencies[word] = (word_frequencies[word]/maximum_freq)


    sentence_list = [ sentence for sentence in docx.sents ]

    sentence_scores = {}
    for sent in sentence_list:
        for word in sent:
            if word.text.lower() in word_frequencies.keys():
                #if len(sent.text.split(' ')) < 30:
                    if sent not in sentence_scores.keys():
                        sentence_scores[sent] = word_frequencies[word.text.lower()]
                    else:
                        sentence_scores[sent] += word_frequencies[word.text.lower()]


    from heapq import nlargest

    summarized_sentences = nlargest(5,sentence_scores,key=sentence_scores.get)


    final_text = [w.text for w in summarized_sentences ]


    summary= '\n'.join(final_text)

#len(text)





#len(summary)
    
    T2.insert(tk.END, summary)

T = tk.Text(root, height=10, width=70)
T.pack(pady=20)

#mylabel= tk.Label(root, text='SUMMARY', )
#mylabel.pack(pady=20)

button_frame = tk.Frame(root)
button_frame.pack()

clear_button = tk.Button(button_frame, text="clear screen", command=clear)
clear_button.grid(row=0, column=0)

submit_text_button = tk.Button(button_frame, text="submit for summary", command = get_text)
submit_text_button.grid(row=0, column=1, padx=20)

T2 = tk.Text(root, height=10, width=70)
T2.pack(pady=20)



#text=T.get("1.0",'end')
#print(text)
tk.mainloop()

