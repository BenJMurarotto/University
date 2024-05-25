% Importing table data
utah_h = readtable('Utah_H_Playoffs.csv');
utah_a = readtable('Utah_A_Playoffs.csv');
boston_a = readtable('Boston_A_Playoffs.csv');
boston_h = readtable('Boston_H_Playoffs.csv');
la_a = readtable('LAL_A_Playoffs.csv');
la_h = readtable('LAL_H_Playoffs.csv');
indiana_a = readtable('Pacers_A_Playoffs.csv');
indiana_h = readtable('Pacers_H_Playoffs.csv');
indiana_hstat = readtable('Pacers_H_stats.csv');
indiana_astat = readtable('Pacers_A_stats.csv');
la_astat = readtable('LAL_A_stats.csv');
la_hstat = readtable('LAL_H_stats.csv');
utah_hstat = readtable('Utah_H_stats.csv');
utah_astat = readtable('Utah_A_stats.csv');
boston_astat = readtable('Boston_A_stats.csv');
boston_hstat = readtable('Boston_H_stats.csv');

% Join relevant tables
hg_indi = join(indiana_h, indiana_hstat, Keys='Rk');
ag_indi = join(indiana_a, indiana_astat, Keys='Rk');
hg_bost = join(boston_h, boston_hstat, Keys='Rk');
ag_bost = join(boston_a, boston_astat, Keys='Rk');
hg_utah = join(utah_h, utah_hstat, Keys='Rk');
ag_utah = join(utah_a, utah_astat, Keys='Rk');
hg_LA = join(la_h, la_hstat, Keys='Rk');
ag_LA = join(la_a, la_astat, Keys='Rk');

% Extracting relevant data
% Field goal percentages
indi_a_FGper = mean(ag_indi.FG_);
indi_h_FGper = mean(hg_indi.FG_);
bost_a_FGper = mean(ag_bost.FG_);
bost_h_FGper = mean(hg_bost.FG_);
la_a_FGper = mean(ag_LA.FG_);
la_h_FGper = mean(hg_LA.FG_);
utah_h_FGper = mean(hg_utah.FG_);
utah_a_FGper = mean(ag_utah.FG_);

% Turnovers
indi_a_TO = mean(ag_indi.TOV);
indi_h_TO = mean(hg_indi.TOV);
bost_a_TO = mean(ag_bost.TOV);
bost_h_TO = mean(hg_bost.TOV);
la_a_TO = mean(ag_LA.TOV);
la_h_TO = mean(hg_LA.TOV);
utah_a_TO = mean(hg_utah.TOV);
utah_h_TO = mean(ag_utah.TOV);

% Personal Fouls
indi_a_PF = mean(ag_indi.PF);
indi_h_PF = mean(hg_indi.PF);
bost_a_PF = mean(ag_bost.PF);
bost_h_PF = mean(hg_bost.PF);
la_a_PF = mean(ag_LA.PF);
la_h_PF = mean(hg_LA.PF);
utah_a_PF = mean(hg_utah.PF);
utah_h_PF = mean(ag_utah.PF);

% Combine data into arrays for comparison
teams = {'INDI', 'BOST', 'LA', 'UTAH'};
FG_per_away = [indi_a_FGper, bost_a_FGper, la_a_FGper, utah_a_FGper];
FG_per_home = [indi_h_FGper, bost_h_FGper, la_h_FGper, utah_h_FGper];
TO_away = [indi_a_TO, bost_a_TO, la_a_TO, utah_a_TO];
TO_home = [indi_h_TO, bost_h_TO, la_h_TO, utah_h_TO];
PF_away = [indi_a_PF, bost_a_PF, la_a_PF, utah_a_PF];
PF_home = [indi_h_PF, bost_h_PF, la_h_PF, utah_h_PF];

% Calculate differences
FG_per_diff = (FG_per_home - FG_per_away)*100;
TO_diff = TO_home - TO_away;
PF_diff = PF_home - PF_away;

% Display differences
disp('Differences (Home - Away)');
disp(table(teams', FG_per_diff', TO_diff', PF_diff', ...
    'VariableNames', {'Team', 'FG_Percentage_Difference', 'TO_Difference', 'PF_Difference'}));

% Plot visualisation
figure;

% Field Goal Percentage
subplot(3,1,1);
b1 = bar([FG_per_away; FG_per_home]');
title('Field Goal Percentage');
set(gca, 'XTickLabel', teams);
legend('Away', 'Home');
set(gca, 'Position', [0.1, 0.72, 0.85, 0.2]);

% Bar tips for Field Goal Percentage
for k = 1:length(b1)
    xtips1 = b1(k).XEndPoints;
    ytips1 = b1(k).YEndPoints;
    labels1 = string(b1(k).YData);
    text(xtips1, ytips1, labels1, 'VerticalAlignment', 'bottom', 'HorizontalAlignment', 'center');
end

% Turnovers
subplot(3,1,2);
b2 = bar([TO_away; TO_home]');
title('Turnovers');
set(gca, 'XTickLabel', teams);
legend('Away', 'Home');
set(gca, 'Position', [0.1, 0.42, 0.85, 0.2]);

% Bar tips for Turnovers
for k = 1:length(b2)
    xtips2 = b2(k).XEndPoints;
    ytips2 = b2(k).YEndPoints;
    labels2 = string(b2(k).YData);
    text(xtips2, ytips2, labels2, 'VerticalAlignment', 'bottom', 'HorizontalAlignment', 'center');
end

% Personal Fouls
subplot(3,1,3);
b3 = bar([PF_away; PF_home]');
title('Personal Fouls');
set(gca, 'XTickLabel', teams);
legend('Away', 'Home');
set(gca, 'Position', [0.1, 0.12, 0.85, 0.2]);

% Bar tips for Personal Fouls
for k = 1:length(b3)
    xtips3 = b3(k).XEndPoints;
    ytips3 = b3(k).YEndPoints;
    labels3 = string(b3(k).YData);
    text(xtips3, ytips3, labels3, 'VerticalAlignment', 'bottom', 'HorizontalAlignment', 'center');
end
