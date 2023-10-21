# RODAR VÍDEOS ALEATÓRIOS:
import pathlib
import random
from pathlib import Path
from moviepy.editor import *

# SELEÇÃO DE DESENHOS:
p = Path('./videos')
videos = [f for f in p.iterdir() if f.is_dir()]

random.shuffle(videos)
print(videos)

listaReproducao = list()

for video in range(0, len(videos)):
    listaEpisodio = []
    for mp4_path in Path(videos[video]).glob('*.mp4'):
        print(mp4_path)
        listaEpisodio.append(mp4_path)
    random.shuffle(listaEpisodio)
    print(listaEpisodio)
    print(f'listaEpisodio0: {listaEpisodio[0]}')
    listaReproducao.append(listaEpisodio[0])

print(f'listaReproducao: {listaReproducao}')

for c in range(0, len(listaReproducao)):
    print(listaReproducao[c])
    clip = VideoFileClip(f'{listaReproducao[c]}')
    clip.preview()





