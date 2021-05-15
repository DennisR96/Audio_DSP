%% Allpass
function [out, buffer] = allpass(in,buffer,g,delay,n)
    out = g*in + buffer(delay,1);
    buffer = [in + -g*out ; buffer(1:end-1,1)];
end
  
%% Example
% clear; clc;
% in = [1;zeros(100,1)];
% buffer = zeros(5,1);
% delay = 2;
% g = 0.5;
% N = length(in);
% out = zeros(length(in),1);
% for n = 1:N
%     [out(n,1), buffer] = allpass(in(n,1),buffer,g,delay,n);
% end
% freqz(out);

