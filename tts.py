from itertools import islice

from TTS.api import TTS

polish_model = "tts_models/pl/mai_female/vits"
utf_8 = 'utf8'
padding = '-{:03}'
lines_per_file = 100

def read_to_file(file_path):
    tts = TTS(polish_model)

    file_paths = split_into_multiple_files(file_path)

    for path in file_paths:
        content = file_content_to_string(path)

        tts.tts_to_file(text=content, file_path=path + '.wav')


def split_into_multiple_files(input_file_path):
    out_paths = []

    with open(input_file_path, encoding=utf_8) as file:
        for i, lines in enumerate(iter(lambda: list(islice(file, lines_per_file)), []), 1):

            ith_out_path = input_file_path + padding.format(i)
            out_paths.append(ith_out_path)

            with open(ith_out_path, "w", encoding=utf_8) as f:
                f.writelines(lines)

    return out_paths


def file_content_to_string(file_path):
    with open(file_path, 'r', encoding=utf_8) as file:
        return file.read().replace('\n', ' ')


read_to_file('resources/tts_input.txt')
