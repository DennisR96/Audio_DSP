function [y, buffer] = lowp(x,buffer,n)
% Simple Low Pass Filter 
% Circular Buffer
delay = 1;                              % Delay 
len = length(buffer);                   % Length Buffer
indexC = mod(n-1,len) + 1;              % Circular Index
indexD = mod(n-delay-1,len) + 1;        % Delay Index
y = buffer(1,indexD) ;                  % Output
buffer(1,indexC) = x;                   % Buffer 
% Lowpass               
y = y + x;                              % y(n) = x(n) + x(n-1)

end
