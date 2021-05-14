function [y, buffer] = buffer_circ(x,buffer,delay,n)
len = length(buffer);                   % Length Buffer
indexC = mod(n-1,len) + 1;              % Circular Index
indexD = mod(n-delay-1,len) + 1;        % Delay Index
y = buffer(indexD,1);                   % Output
buffer(indexC,1) = x;                   % Buffer 
end

% %%Example
% clc; clear;                         % Clear Console
% x = [1,0,0,0,0,0,0]';               % Input: (N,1)
% N = length(x);                      % Array Size
% N_b = 6;                            % Buffer Size
% buffer = zeros(N_b,1);              % Buffer
% delay = 3;                          % Delay
% y = zeros(N,1);                     % Output: (N,1)
% for n = 1:N
%     [y(n,1),buffer] = buffer_circ(x(n,1),buffer,delay,n);
% end 

