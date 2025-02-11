import random
import os

def generate_text_with_typos(num_lines, comma_frequency, typo_level):
    if not os.path.exists('phrases.txt'):
        print('phrases.txt does not exist. Please create this file and add some lines to it.')
        return

    with open('phrases.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()

    lines = [line.strip() for line in lines]

    generated_text = []
    used_lines = []

    typo_percentages = {
        1: 0.01,  # 1% слов с опечатками
        2: 0.02,  # 2% слов с опечатками
        3: 0.1    # 10% слов с опечатками
    }

    for i in range(num_lines):
        available_lines = [line for line in lines if line not in used_lines]

        if available_lines:
            next_line = random.choice(available_lines)

            if i > 0 and i % comma_frequency == 0:
                generated_text.append(',')

            words = next_line.split()

            if typo_level > 0:
                words_with_typos = []

                for word in words:
                    if random.random() < typo_percentages[typo_level]:
                        typo_word = generate_typo(word)
                        words_with_typos.append(typo_word)
                    else:
                        words_with_typos.append(word)

                line_with_typos = ' '.join(words_with_typos)
                generated_text.append(line_with_typos)
            else:
                generated_text.append(next_line)

            used_lines.append(next_line)
        else:
            break

    generated_text = ' '.join(generated_text)

    with open('generated.txt', 'w', encoding='utf-8') as f:
        f.write(generated_text)

    print(generated_text)

def generate_typo(word):
    typo_variations = {
        'a': ['s', 'z', 'q'],
        'b': ['v', 'n', 'g'],
        'c': ['x', 'v', 'd'],
        'd': ['s', 'f', 'e'],
        'e': ['w', 'r', 's'],
        'f': ['d', 'g', 't'],
        'g': ['f', 'h', 'y'],
        'h': ['g', 'j', 'u'],
        'i': ['o', 'u', 'k'],
        'j': ['h', 'k', 'u'],
        'k': ['j', 'l', 'i'],
        'l': ['k', 'p', 'o'],
        'm': ['n', 'b', 'h'],
        'n': ['m', 'b', 'j'],
        'o': ['i', 'p', 'l'],
        'p': ['o', 'l', '0'],
        'q': ['w', 's', 'a'],
        'r': ['e', 't', 'd'],
        's': ['a', 'd', 'z'],
        't': ['r', 'y', 'f'],
        'u': ['y', 'i', 'j'],
        'v': ['c', 'b', 'g'],
        'w': ['q', 'e', 's'],
        'x': ['z', 'c', 'd'],
        'y': ['t', 'u', 'h'],
        'z': ['x', 'a', 's']
    }

    possible_typos = typo_variations.get(word[-1], [])
    typo_word = list(word)

    if possible_typos:
        random_typo = random.choice(possible_typos)
        typo_word[-1] = random_typo

    return ''.join(typo_word)

def print_beautiful_text(text):
    square_size = len(text) + 4

    print("\u250f" + "\u2501" * square_size + "\u2513")
    print("\u2503 " + text.strip() + " \u2503")
    print("\u2517" + "\u2501" * square_size + "\u251b")

def print_logo():
    logo = """
     ██╗  ██╗ █████╗ ██████╗ ██████╗ ██╗ ███████╗
     ██║  ██║██╔══██╗██╔══██╗██╔══██╗██║ ██╔════╝
     ███████║███████║██████╔╝██████╔╝██║ ███████╗
     ██╔══██║██╔══██║██╔═══╝ ██╔═══╝ ██║ ╚════██║
     ██║  ██║██║  ██║██║     ██║     ██║ ███████║
     ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝     ╚═╝ ╚══════╝
"""
    print(logo)
    print("TROLLING")

def get_user_input(prompt, validate_fn):
    while True:
        try:
            value = validate_fn(input(prompt))
            return value
        except ValueError as e:
            print(e)

def main():
    while True:
        print_logo()

        num_lines = get_user_input('введи сколько нужно строк: ', lambda x: int(x) if int(x) > 0 else ValueError('Пожалуйста, введите корректное количество строк (целое число больше 0).'))
        comma_frequency = get_user_input('Через сколько строк нужно ставить запятую (Рекомендовано через 20 строк): ', lambda x: int(x) if int(x) > 0 else ValueError('Пожалуйста, введите корректное значение для частоты запятых (целое число больше 0).'))
        typo_level = get_user_input('Введите уровень опечаток (от 1 до 3): ', lambda x: int(x) if int(x) in [1, 2, 3] else ValueError('Пожалуйста, введите корректный уровень опечаток (1, 2 или 3).'))

        generate_text_with_typos(num_lines, comma_frequency, typo_level)

        print("bye bye")
        restart = get_user_input('Введите 7 для перезапуска, или любое другое число для выхода: ', lambda x: int(x))

        if restart != 7:
            break

if __name__ == "__main__":
    main()
