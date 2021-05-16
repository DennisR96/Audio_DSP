%% Raumakustik
clc; clear;
%% Impulsantwort
[h, fs] = audioread('h1.wav');
N = length(h);
x = linspace(1,N/fs,N);
t = N/fs;
%% EDC - Early Decay Curve
f_EDC = figure('Name','Early Decay Curve');
h_2=h.^2;
A = cumtrapz(h_2);
B = fliplr(cumtrapz(fliplr(h_2')));
L = 10*log10(B(1:N)./A(N));
plot(x,L);
grid();
title("EDC - Energy Decay Curve");
ylabel('Energy in [dB]');
xlabel('Time in [s]');

%% 
f_EDR = figure('Name', 'Early Decay Relief ')
window = (hann(1024).^4);
[S,F,T]=spectrogram(B,window,round(0.75*length(window)),512,fs);
EDR_spect = 20*log10(abs(S));
mesh(T,F,EDR_spect);
xlabel('Time in s')
ylabel('Frequency')
zlabel('Energy in dB')
