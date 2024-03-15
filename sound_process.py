
import os
import subprocess

import librosa
import pydiogment.auga,pydiogment.augf,pydiogment.augt,pydiogment.utils.io
import matplotlib.pyplot as plt
import numpy as np
import ffmpeg
import utils
from pydiogment.utils.io import read_file,write_file
from scipy.io.wavfile import read, write
from scipy.signal import lfilter
from scipy.fft import fft
from scipy.signal.windows import hamming


def optimization(song_name):
    if os.path.isfile(song_name + "song_plus.wav"):
        os.remove(song_name + "song_plus.wav")

    song_name = song_name + ".wav"
    if os.path.isfile(song_name):
        wav_data, _ = librosa.load(song_name, sr=16000, mono=True)

        #pree_data = librosa.effects.preemphasis(wav_data,return_zf=False)
        pree_data,scr = convert_vol(wav_data)
        #pree_data = convert_gain(pree_data)
        #data = librosa.effects.harmonic(pree_data)
        #data = librosa.effects.percussive(data)

        output_file_path = os.path.dirname(song_name)
        name_attribute = "song_plus.wav"
        data = convert_format(pree_data)
        write_file(output_file_path=output_file_path,
                              input_file_name=song_name,
                              name_attribute=name_attribute,
                              sig=data,
                              fs=16000)


        return True
    return False

def show_song():
    wav_data, _ = librosa.load("Alonesong_plus.wav", sr=16000, mono=True)
    wav_data_raw, _ = librosa.load("Alone.wav", sr=16000, mono=True)

    plt.subplot(2, 2, 1)
    #plt.specgram(wav_data, Fs=16000, scale_by_freq=True, sides='default', cmap="jet")
    #plt.title("pre_emphasis", fontsize=15)
    plt.title("Volume boost", fontsize=15)
    time = np.arange(0, len(wav_data)) * (1.0 / 16000)
    plt.xlabel('/s', fontsize=15)
    plt.ylabel('/Hz', fontsize=15)
    plt.plot(time, wav_data)

    plt.subplot(2, 2, 2)
    #plt.specgram(wav_data_raw, Fs=16000, scale_by_freq=True, sides='default', cmap="jet")
    plt.title("original", fontsize=15)
    time2 = np.arange(0, len(wav_data_raw)) * (1.0 / 16000)
    plt.xlabel('/s', fontsize=15)
    plt.ylabel('/Hz', fontsize=15)
    plt.plot(time2, wav_data_raw)

    plt.tight_layout()
    plt.show()
    return True

def convert_format(wav_data):
    #max_val = np.max(wav_data)
    max_16bit = 2 ** 15
    wav_data = wav_data * max_16bit
    wav_data = wav_data.astype(np.int16)
    return wav_data


def convert_gain(wav_data,gain = 2):
    wav_data = np.copy(wav_data)
    wav_data = wav_data * (1 ** (gain / 1.0))
    wav_data = np.minimum(np.maximum(-1.0, wav_data), 1.0)
    wav_data /= np.mean(np.abs(wav_data))
    return wav_data

def convert_vol(wav_data, dB = 2):
    rmswav = (wav_data ** 2).mean() ** 0.5
    scalar = 10 ** (dB / 20) / (rmswav + np.finfo(np.float32).eps)
    wav = wav_data * scalar
    return wav, scalar
