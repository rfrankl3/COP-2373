import re

def split_into_sentences(paragraph):
    sentences = re.split(r'(?<=[.!?])\s+', paragraph)
    sentences = [s.strip() for s in sentences if s.strip() != ""]
    return sentences


def display_sentences(sentences):
    print("\nIndividual Sentences:\n")

    for i, sentence in enumerate(sentences, start=1):
        print(f"Sentence {i}: {sentence}")

    print("\nTotal number of sentences:", len(sentences))


def main():
    paragraph = input("Enter a paragraph:\n")
    sentences = split_into_sentences(paragraph)
    display_sentences(sentences)


main()