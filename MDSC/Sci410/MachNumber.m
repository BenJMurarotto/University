
while true
    speedOfCraft = input("Please provide the speed of the aircraft: ");
    speedOfSound = input("Please provide the speed of sound at the aircraft's current altitude: ");

    if isnumeric(speedOfCraft) && isnumeric(speedOfSound) && speedOfCraft > 0 && speedOfSound > 0
       machn = speedOfCraft/speedOfSound;

        if machn < 1
            disp("The flight is subsonic!")
        elseif machn == 0
            disp("The flight is transonic!")
        else
            disp("The flight is supersonic!")
        end
    break;
    else
        disp("Please input valid integers for speed of craft and speed of sound!")
    end  
end  
    
            