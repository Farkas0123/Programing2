import string
from itertools import islice
import random

class TextAnalyzer:
    def __init__(self, file_path):
        self.file_path = file_path
        self.text = ''
        self.cleaned_text = ''
        self.word_counts = {}
        self.markov_chain = {}

    def read_text(self):
        lines = []
        with open(self.file_path,'r',encoding='utf-8') as f:
            for line in f:
                lines.append(line.strip())
        self.text = ' '.join(lines)

    def clean_and_preprocess(self):
        self.text = self.text.lower()
        translator = str.maketrans('', '', string.punctuation)
        self.cleaned_text = self.text.translate(translator)

        
    def extract_words(self):
        return self.cleaned_text.split()
        
    def count_word_frequencies(self):
        words = self.extract_words()
        for word in words:
            if word in self.word_counts:
                self.word_counts[word] += 1
            else:
                self.word_counts[word] = 1
    
    def build_markov_chain(self):
        l = self.extract_words()
        for i in range(len(l)-1):
            if l[i] in self.markov_chain.keys():
                if l[i+1] in self.markov_chain[l[i]].keys():
                    self.markov_chain[l[i]][l[i+1]] += 1
                else: 
                    self.markov_chain[l[i]][l[i+1]] = 1
            else:
                self.markov_chain[l[i]] = {l[i+1]: 1}
        
    def predict_next_word(self, current_word, k):
        if not self.markov_chain:
            self.build_markov_chain()
        if current_word in self.markov_chain:
            # Get the next possible words sorted by their frequencies in descending order
            next_words_sorted = sorted(self.markov_chain[current_word].items(), key=lambda x: x[1], reverse=True)
            top_k_next_words = next_words_sorted[:k]
            
            # Randomly choose from the top k most likely next words
            if top_k_next_words:
                next_word = random.choice(top_k_next_words)[0]
                return next_word
            else:
                return "No prediction available"
        else:
            return "No prediction available"



for novel in ['pg1080.txt','pg84.txt','pg1232.txt']:
    file_path = novel
    analyzer = TextAnalyzer(file_path)
    analyzer.read_text()
    analyzer.clean_and_preprocess()
    analyzer.count_word_frequencies()

    def generate_story(text_analyzer, start_words, story_length=30, k=3):
        story = start_words
        prev = start_words.split()[len(start_words.split())-1]

        for i in range(30):
            next = text_analyzer.predict_next_word(prev, 5)
            story += ' '+next
            prev = next
        return story

    # Assuming 'analyzer' is your TextAnalyzer object and has already processed a text
    start_words = "Once upon a time"  # Example starting words
    story = generate_story(analyzer, start_words)
    print(story)