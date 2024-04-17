addpath '..\'
n_iterations = 10;

tic
for i = 1:n_iterations
    pi_calc();
end
final_time = toc;
disp("Matlab:")
fprintf("\t%s\n", scientific_time(final_time / n_iterations))