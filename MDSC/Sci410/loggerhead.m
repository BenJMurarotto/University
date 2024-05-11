hatch = 1445570;
sjuv = 1845597;
ljuv = 1845597;
subadult = 1845597;
adult = 17640;


years = input('How many years into the future would you like to project the population?:  ');

while isnumeric(years) && years <= 0
    disp('Error. Please input a positive integer!');
    years = input('How many years into the future would you like to project the population?:  ');
end

ipop = [hatch; sjuv; ljuv ; subadult; adult];
pop_mat = NaN(length(ipop), years + 1);
pop_mat(:, 1) = ipop;

p = [0.675, 0.047, 0.703, 0.019, 0.657];


for year = 1:years
    for i = 1:length(ipop)
        if i == length(ipop)
            growth_rate = 0.8091;
        else
            growth_rate = p(i);
        end
        pop_mat(i, year + 1) = pop_mat(i, year) * growth_rate;
    end
end

figure;
plot(0:years, pop_mat', '-o', 'LineWidth', 0.5);
xlabel('Years');
ylabel('Population');
title('Population Projection for Loggerhead Life Stages');
legend('Hatchlings', 'Small Juveniles', 'Large Juveniles', 'Subadults', 'Adults');
grid on;
