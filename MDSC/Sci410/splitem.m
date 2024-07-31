function [onevec, twovec] = splitem(vec)
%splitem(vec) = [onevec , twovec]
% splitem takes an array and returns that array split into one with the odd
% numbers and one with the even numbers of the original array.
onevec = [];
twovec = [];
    for ii = vec
        if ii == 0
           continue
        elseif mod(ii, 2) == 0
            onevec = [onevec, ii];
        else
            twovec = [twovec, ii];
        end
    end
    disp('Even Numbers')
    disp(onevec)
    disp('Odd Numbers')
    disp(twovec)
end
