import os
import re
import subprocess
import nltk

nltk.download('punkt_tab')
def preprocess_text_en(text: str) -> list[str]: # Remove the paragraph indices
    # Clean the text
    text = text.replace('\n', ' ')
    text = re.sub(r'[\d+]', ' ', text)

    # Split the sentences
    sents = nltk.sent_tokenize(text) # Split the sentences

    return sents


def preprocess_text_cn(text: str) -> list[str]:
    # Clean the text
    for c in ['\n', '\u3000']:
        text = text.replace(c, ' ')
    text = text.replace('……', '。')
    text = re.sub(r'[\d+]', ' ', text)

    # Split the sentences
    sents = []
    sent = ''
    i = 0
    while i < len(text):
        sent += text[i]
        if text[i] in ['。', '！', '？', '；']:
            if i < len(text) - 1 and text[i + 1] == '”':
                i += 1
                sent += text[i]
            sents.append(sent.strip())
            sent = ''
        i += 1

    return sents

def concat_audios(directory: str, output_fname: str) -> None:
    """
    Concatenate all .wav audio files in a given list and output it as a new .wav audio file.
    This function uses ffmpeg in shell. Therefore, ffmpeg must be installed.
    :param directory:
    :param output_fname:
    :return:
    """
    fnames = [fname for fname in os.listdir(directory) if fname.endswith('.wav')]
    fnames.sort(key=lambda x: int(x[:x.find('.')]))
    fnames = [f"file '{fname}'\n" for fname in fnames]

    with open(f"{directory}/concat_list.txt", 'w') as file:
        print(''.join(fnames), file=file)

    try:
        subprocess.run(
            f"ffmpeg -y -f concat -safe 0 -i '{directory}'/concat_list.txt -c copy '{output_fname}'.wav",
            check=True,
            shell=True,
        )
    except Exception as e:
        print(e)

def clean_directory(directory: str) -> None:
    try:
        for f in os.listdir(directory):
                os.remove(f"{directory}/{f}")
        os.rmdir(directory)
    except Exception as e:
        if type(e) is FileNotFoundError:
            pass