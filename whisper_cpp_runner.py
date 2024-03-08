import os
import subprocess
from audio_processing import resample_to_16khz
import time
from dotenv import load_dotenv

load_dotenv()
path = os.getenv("WHISPERCPP_PATH")

path_audio_originale = "audio/iges_lezione4_parte2.m4a"

audio_samplato = resample_to_16khz(path_audio_originale)

argomenti = ["-m", os.getenv("MODEL_PATH"), "-f", audio_samplato, "--output-txt", "-l", "it" ]
print("trascrivo...")

start_time = time.time()
subprocess.run([path] + argomenti)
end_time = time.time()
print("\ntempo passato in minuti = ", (end_time-start_time)/60)