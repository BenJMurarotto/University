load("measurement_data.mat");
[m1Len, m1Mean, m1Std, m1SE, m1UpperB, m1LowerB] = stdget(m1);
[m2Len, m2Mean, m2Std, m2SE, m2UpperB, m2LowerB] = stdget(m2);

figure;

subplot(1, 2, 1);
histogram(m1)
title('m1')
xlabel('x')
ylabel('y')

subplot(1, 2, 2);
histogram(m2)
title('m2')
xlabel('x')
ylabel('y')

m1table = table(m1Len, m1Mean, m1Std, m1SE, m1UpperB, m1LowerB, 'Variablenames', {'Length', 'Mean', 'StD', 'SE', 'CI+', 'CI-'})
m2table = table(m2Len, m2Mean, m2Std, m2SE, m2UpperB, m2LowerB, 'Variablenames', {'Length', 'Mean', 'StD', 'SE', 'CI+', 'CI-'})

