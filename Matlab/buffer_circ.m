function [y, buffer] = buffer_circ(x,buffer,delay,n)
len = length(buffer);                   % Length Buffer
indexC = mod(n-1,len) + 1;              % Circular Index
indexD = mod(n-delay-1,len) + 1;        % Delay Index
y = buffer(indexD,1);                   % Output
buffer(indexC,1) = x;                   % Buffer 
end

% %%Example
% clc; clear;                     % Clear Console
% x = [1,0,0,0,0,0,0];            % Input
% buffer = zeros(6,1);            % Buffer
% delay = 4;                      % Delay
% N = length(x);                  % Samples: Input
% y = zeros(N,1);                 % Output
% for n = 1:N
%     [y(n,1),buffer] = buffer_circ(x(1,n),buffer,delay,n);
% end 
