% Set up a vector containing the census years
years = 1957:2017;

% Generate random number of bites for each year
a = randi([0, 20], 1, length(years));
b = randi([0, 20], 1, length(years));

% Identify the maximum number of bites to help
% construct consistent bounds for both plots
Amax = max(a);
Bmax = max(b);
ABmax = max([Amax Bmax]);

figure(1); clf; hold on;

% Plot for state A
subplot(1, 2, 1); hold on;
bar(years, a);
xlabel('Year');
ylabel('Number of bites');
title('Snake bites in state A, 1957 to 2017');
axis([1957 2017 0 ABmax]);
box on;

% Plot for state B
subplot(1, 2, 2); hold on;
bar(years, b);
xlabel('Year');
ylabel('Number of bites');
title('Snake bites in state B, 1957 to 2017');
axis([1957 2017 0 ABmax]);
box on;
