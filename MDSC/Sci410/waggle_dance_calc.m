load('waggle_dances_florea.mat'); %load data

pollenDist = durationToDistance(durations_pollen); 
nopollenDist = durationToDistance(durations_no_pollen); %conversion of durations using durationToDistance function

[pollenX, pollenY] = convertToCoordinates(pollenDist, angles_pollen);
[nopollenX, nopollenY] = convertToCoordinates(nopollenDist, angles_no_pollen);

subplot(1, 2, 1); %scatter plot showing map of bees from origin
hold on;
plot(pollenX, pollenY, 'r.'); 
plot(nopollenX, nopollenY, 'b.');
plot(0, 0, 'k.');
xlabel('X');
ylabel('Y');
title('Waggle Dance Journeys');
legend('Pollen Carrying Bees', 'Non-Pollen Carrying Bees', 'Colony');

combinedX = [pollenX(:); nopollenX(:)]; %converting to column vectors
combinedY = [pollenY(:); nopollenY(:)];

subplot(1, 2, 2); %density histogram
histogram2(combinedX, combinedY, 'FaceColor', 'flat');
xlabel('X');
ylabel('Y');
title('Site Density');
colorbar;