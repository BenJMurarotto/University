years = 1961:1971;
deaths = [850 798 818 903 1026 1042 1022 1069 1070 1135 1096];

p = polyfit(years,deaths,1);

slope = p(1)
intercept = p(2)

% Generate the line of best fit
fitted_line = polyval(p, years);

% Plot the line of best fit
plot(years, fitted_line, '-r', 'LineWidth', 2);

% Add labels and title
xlabel('Year');
ylabel('Number of Fatal Road Accidents');
title('Fatal Road Accidents in NSW (1961-1971)');
legend('Data Points', 'Line of Best Fit', 'Location', 'NorthWest');

% Display the slope and intercept
fprintf('Slope: %.2f\n', slope);
fprintf('Intercept: %.2f\n', intercept);