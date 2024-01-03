import re

try:
    with open('clippings.txt', 'r', encoding='utf-8') as file:
        content = file.read()
    pattern = re.compile(r'=+\n(.*?)=+', re.DOTALL)
    matches = pattern.findall(content)
    # print(matches)
    for index, phrase in enumerate(matches):
        print('Phrase #{}'.format(index + 1))
        # print('phrase: {}'.format(phrase))
        lines = phrase.strip().split('\n')  # Divide la frase en líneas separadas
        if len(lines) < 4:
            print('Invalid note!, phrase not found!')
            continue
        book = lines[0].strip()  # Título del libro
        date = lines[1].strip()  # Fecha de la nota
        quote = lines[3].strip()  # Cita
        print('Book: {}\nDate:{}\nQuote:{}\n'.format(book, date, quote))
        print('----------------------------------')
except FileNotFoundError:
    print('File not found!')
