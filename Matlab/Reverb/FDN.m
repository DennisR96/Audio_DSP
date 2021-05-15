%% Feedback Delay Network (N=4)
clc; clear;

%% Input
[test, m] = audioread("Snare1.wav");
x = test(:,1)'
x = [x,zeros(1,m*3)]
fs = 44100;

% x = zeros(1, fs);
% x(1) = 1;
y = zeros(1,length(x))

%% Parameter
gain = 0.97
a(1,:)=[0 1 1 0]; 
a(2,:)=[-1 0 0 -1]; 
a(3,:)=[1 0 0 -1]; 
a(4,:)=[0 1 -1 0];
a=a*(1/sqrt(2)) * gain;


b = [1 1 1 1];
c = [0.8 0.8 0.8 0.8];
d = 0.3;
M = [149 211 263 293]; 

s_1 = 0;
s_2 = 0;
s_3 = 0;
s_4 = 0;

for n=1:length(x)
    y(n) = c(1) * s_1(n) + d * x(n)...
        + c(2) * s_2(n) + d * x(n) ...
        + c(3) * s_3(n) + d * x(n) ...
        + c(4) * s_4(n) + d * x(n);
    
    
    s_1(n+M(1)) = a(1,1) * s_1(n) + b(1) * x(n) ...
        + a(1,2) * s_2(n) + b(1) * x(n) ...
        + a(1,3) * s_3(n) + b(1) * x(n) ...
        + a(1,4) * s_4(n) + b(1) * x(n);
   
    s_2(n+M(2)) = a(2,1) * s_1(n) + b(2) * x(n) ...
        + a(2,2) * s_2(n) + b(2) * x(n) ...
        + a(2,3) * s_3(n) + b(2) * x(n) ...
        + a(2,4) * s_4(n) + b(2) * x(n);
    
    s_3(n+M(3)) = a(3,1) * s_1(n) + b(3) * x(n) ...
        + a(3,2) * s_2(n) + b(3) * x(n) ...
        + a(3,3) * s_3(n) + b(3) * x(n) ...
        + a(3,4) * s_4(n) + b(3) * x(n);
    
    s_4(n+M(4)) = a(4,1) * s_1(n) + b(3) * x(n) ...
        + a(4,2) * s_2(n) + b(3) * x(n) ...
        + a(4,3) * s_3(n) + b(3) * x(n) ...
        + a(4,4) * s_4(n) + b(3) * x(n);
end

y = y / max(y);
sound(y,fs);
plot(y)
