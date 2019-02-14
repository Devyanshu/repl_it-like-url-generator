from nouns import nouns
from adjectives import adjectives
from random import choice


def generate(number=1):
    for _ in range(number):
        adj_1 = choice(adjectives)
        adj_2 = choice(adjectives)
        while adj_2 == adj_1:
            adj_2 = choice(adjectives)
        noun = choice(nouns)
        yield adj_1.title() + adj_2.title() + noun.title()


def generate_list(number):
    return list(generate(number))


if __name__ == "__main__":
    for url in generate():
        print(url)
    print(generate_list(5))
