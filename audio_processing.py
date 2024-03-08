from pydub import AudioSegment

def crea_nome_file(percorso):
    parti_nome_file = percorso.split(sep='.')
    path_finale = "./"+parti_nome_file[1] + "_tagliato." + parti_nome_file[2]
    return path_finale


def taglia_audio(percorso:str, split_time:int):
    print("tagliando audio...")
    inizio_taglio = split_time*1000  # secondi per 1000
    audio = AudioSegment.from_file(percorso)
    audio_tagliato = audio[inizio_taglio:]
    
    path_finale = crea_nome_file(percorso)
    
    audio_tagliato.export(path_finale, format="mp3")
    return path_finale

def convert_from_m4a_to_mp3(percorso:str):
    print("converto audio...")
    audio = AudioSegment.from_file(percorso, format="m4a")
    mp3_path = "audio/" + percorso.split(sep='.')[1] + ".mp3"
    audio.export(mp3_path, format="mp3")
    
    return


def resample_to_16khz(path: str):
    audio = AudioSegment.from_file(path, format="m4a")
    audio = audio.set_frame_rate(16000)
    
    mp3_path = path.split(sep='.')[1] + ".wav"
    audio.export(mp3_path, format="wav")
    return mp3_path

