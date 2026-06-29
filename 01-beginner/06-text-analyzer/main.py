from collections import Counter
import re
import string

read_text = ""

try:
  with open("./text.txt") as f:
    read_text = f.read()
except(FileNotFoundError):
  print("Cannot find the file you are looking for.")


if read_text: 

 sentence = re.split(r"[.!?]", read_text)
 sentences = [s.strip() for s in sentence if s.strip()]
 sentence_counter = Counter(sentences) 
 sentence_count = sum(sentence_counter.values())
 print(f"The sentences count : {sentence_count} ")



 cleaned_text = "".join(char for char in read_text if char not in string.punctuation)

 words = cleaned_text.lower().split()
 word_frequency = Counter(words)
 print(f"The words frequency : ",dict(word_frequency))


 total_chars = sum(len(word) for word in words)
 average_length = total_chars / len(words)
 print(f"The average word length : {average_length}")

 most_common = word_frequency.most_common(10)
 print(f"The 10 most common words : {most_common} ")


















