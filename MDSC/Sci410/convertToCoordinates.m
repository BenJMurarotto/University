function [x, y] = convertToCoordinates(distance, angle)
    %[x, y] = convertToCoordinates(distance, angles)
    x = distance .* sind(angle);
    y = distance .* cosd(angle);
end