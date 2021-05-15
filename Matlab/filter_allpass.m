function [out, buffer] = allpass(in,buffer,g,delay,n)
%% Allpass
    out = g*in + buffer(delay,1);
    buffer = [in + -g*out ; buffer(1:end-1,1)];
end
