%
nmax = input('please enter the final time (in years): ');

%preallocate space for juv breeding adult and elderly pops

J = NaN(1, nmax);
A = NaN(1, nmax);
E = NaN(1, nmax);

% set initial pop 
J(1) = 50;
A(1) = 100;
E(1) = 10;

%loop to update pops

for n = 1:nmax-1
    J(n+1) = 0.3*J(n) + 2*A(n);
    A(n+1) = 0.5*J(n) + 0.85*A(n);
    E(n+1) = 0.1*A(n) + 0.8*E(n);


end
tyears = 1:nmax;

figure(1);clf;hold on
plot(tyears, J,'b')
plot(tyears, A, 'r')
plot(tyears, E, 'k')
xlabel('Years', 'FontSize',24)
ylabel('Population')
set(gca,'FontSize',18)
legend('Juvenile', 'Adult', 'Elderly')
