#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Titel: Audiogramm v3
Autor: Dennis Räk
HAW Hamburg -- Tontechnik 2
"""

import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd


def Sinus(amp, f, fs, t):
    x = np.arange(0, t, 1 / fs)
    y = amp * np.sin(2 * np.pi * f * x)
    sd.play(y, fs)
    sd.wait()
    return 0

def Audiogramm():
    Ref = 0.0008  # 2kHz Referenzton
    dB = [i for i in np.arange(-90, 90, step=5)]  # Dezibel - Range
    dB = dB[::-1]  # Reverse Array
    Linear = [Ref * 10 ** (i / 20) for i in dB]  # Linear Array
    Freq_Array = [250, 500, 1000, 2000, 4000, 8000]  # Frequenz Array
    s = 0  # Start S
    LdB = 17
    Amp_Array = []
    Amp_Array_dB = []
    while s < 6:
        Freq = Freq_Array[s]
        Lin = Linear[LdB]
        Dezi = dB[LdB]
        print("Spiele {A} Hz Sinus mit {B} dB bzw. {C:.2f}".format(A=Freq, B=Dezi, C=Lin))
        Sinus(Lin, Freq, 48000, 3)
        Ergebnis = input("Höher (+5dB) [+] -- Tiefer (-5dB) [-] -- [H] Hörschwelle ")
        if Ergebnis == "+":
            LdB -= 1
        elif Ergebnis == "-":
            LdB += 1
        elif Ergebnis == "H":
            Amp_Array.append(Linear[LdB])
            Amp_Array_dB.append(dB[LdB])
            LdB = 17
            s += 1
    return Freq_Array, Amp_Array_dB

def Plot(Freq_Array, Amp_Array_dB):
    fig, ax = plt.subplots()
    ax.plot(Freq_Array, Amp_Array_dB, marker='o', Label="Audiogramm")
    ax.set_xscale("log")
    ax.set_ylabel("Hörschwelle [dBHL]")
    ax.set_xlabel("Frequenz [Hz]")
    ax.set_title("Audiogramm")
    ax.set_ylim(140, -20)
    plt.xticks(Freq_Array, ["250", "500", "1K", "2K", "4K", "8K"])
    plt.yticks([-10, 0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 120])
    plt.grid(True)
    plt.savefig("Audiogramm.png")
    plt.show()
    return 0


Freq_Array, Amp_Array_dB = Audiogramm()
print(Amp_Array_dB)
Plot(Freq_Array, Amp_Array_dB)