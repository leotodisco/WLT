import whisper 
import sys
from transcriber_facade import write_to_txt
from transcriber_facade import do_transcribe
from audio_processing import taglia_audio

def create_model(size, lang):
    model = whisper.load_model(size)
    return model

if __name__ == '__main__':
    if len(sys.argv) not in [4, 5]:
        print("Numero di argomenti non valido. Assicurati di fornire 3 o 4 argomenti.")
        exit()

    path_audio = sys.argv[1]
    size = sys.argv[2]
    lingua = sys.argv[3]
    #ottieni il formato del file audio e chiama il giusto ConverterStrategy
    #crea un command per incapsulare le richieste e il command chiama il giusto strategy
    
    if(size not in ["medium", "small", "base"]):
        print("Size del modello non valida")
        print("La size può essere tiny, small, medium, large")
        exit()

    if(lingua not in ["it", "en"]):
        print("Lingua non valida\nLa lingua italiana corrisponde a: it\nLa lingua inglese corrisponde a en.")
        exit()
        
    if len(sys.argv) == 5:
        split_time = int(sys.argv[4])
        path_audio = taglia_audio(path_audio, split_time)

    model = create_model(size=size)
    do_transcribe(model=model, path=path_audio, lang=lingua) 
    