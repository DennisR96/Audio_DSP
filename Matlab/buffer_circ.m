function [out, buffer] = buffer_circ(in,buffer,delay,n)
%% buffer_circular
len = length(buffer);                   % Length Buffer
indexC = mod(n-1,len) + 1;              % Circular Index
indexD = mod(n-delay-1,len) + 1;        % Delay Index
out = buffer(indexD,1);                   % Output
buffer(indexC,1) = x;                   % Buffer 
end
