from itertools import islice

from TTS.api import TTS

def split_bulk_file(file_path):
    nr_of_lines = 100
    files = []

    with open(file_path, encoding='utf8') as T:
        for i, lines in enumerate(iter(lambda: list(islice(T, nr_of_lines)), []), 1):

            out_file = file_path.replace(".txt", str(i) + ".txt")
            files.append(out_file)

            with open(out_file, "w", encoding='utf8') as f:
                f.writelines(lines)

    return files

def from_file(file_path):
    with open(file_path, 'r', encoding='utf8') as file:
        return file.read().replace('\n', ' ')


def read_to_file(file_path):
    tts = TTS("tts_models/pl/mai_female/vits")

    file_paths = split_bulk_file(file_path)

    for file_path in file_paths:
        content = from_file(file_path)

        tts.tts_to_file(text=content, file_path=file_path + '.wav')

read_to_file('resources/tts_input.txt')
