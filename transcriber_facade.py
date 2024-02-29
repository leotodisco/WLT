import whisper
from audio_processing import taglia_audio

def write_to_txt(result, output_path):
    max_words_per_line = 16

    with open(output_path, 'w', encoding='utf-8') as file:
        words = result.split()
        for i in range(0, len(words), max_words_per_line):
            line = ' '.join(words[i:i + max_words_per_line])
            file.write(line + '\n')

def do_transcribe(model, path, lang):
    print("trascrivo...")
    
    result = model.transcribe(path, language=lang)
    result_path = "trascrizione.txt"
    write_to_txt(result["text"], result_path)
    
    
def create_model(size, lang):
    model = whisper.load_model(size)
    return model
