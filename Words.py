import nltk
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
from nltk.corpus import stopwords
import string


def calculate_word_frequencies(text):
    # Tokenize the text into words
    words = word_tokenize(text.lower())  # Convert to lowercase for case-insensitivity

    # Remove stopwords and punctuation
    stop_words = set(stopwords.words('english'))
    words = [word for word in words if word.isalnum() and word not in stop_words]

    # Calculate word frequencies
    freq_dist = FreqDist(words)
    return freq_dist

def main():
    # Sample text
    text = """This is a sample text. This text is meant to be used as an example for the word frequency counter. 
    It should help you understand how many times each word appears in a given piece of text."""

    # Calculate word frequencies
    word_frequencies = calculate_word_frequencies(text)

    # Output the word frequencies
    print("Word Frequencies:")
    for word, frequency in word_frequencies.items():
        print(f"{word}: {frequency}")

if __name__ == "__main__":
    main()
