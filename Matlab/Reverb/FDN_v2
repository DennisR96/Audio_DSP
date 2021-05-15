%% Feedback Delay Network
clc; clear; 
tic;
%% Input
fs = 44100;
x = [1,zeros(1, fs)];
y = zeros(1,length(x));
%% Paramters
% A: Feedback Matrix
gain = 0.97
A(1,:)=[0 1 1 0]; 
A(2,:)=[-1 0 0 -1]; 
A(3,:)=[1 0 0 -1]; 
A(4,:)=[0 1 -1 0];
A=A*(1/sqrt(2)) * gain;
% B: Input Gain Matrix
B = [1 1 1 1];
% C: Output Gain Matrix
C = [0.8 0.8 0.8 0.8];
% D: Direct Gain Matrix
D = 0.3;
% M: Delay Matrix
M = [149 211 263 293];
% s: Delay Lines
s(1,:) = zeros(1,length(x)+max(M));
s(2,:) = zeros(1,length(x)+max(M));
s(3,:) = zeros(1,length(x)+max(M));
s(4,:) = zeros(1,length(x)+max(M));
N = length(C);
%% Signal Processing
for n=1:length(x)
    for i=1:N
        y(n) = y(n) + (C(i)*s(i,n) + D * x(n));
        for j=1:N
            s(i,n+M(i))= s(i,n+M(i)) + (A(i,j)*s(j,n)+B(i) * x(n));
        end
    end
end
y = y / max(y);
toc
sound(y,fs);

