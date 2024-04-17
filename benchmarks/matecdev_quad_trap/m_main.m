addpath '..\'
n_iterations = 100;

tic
for i = 1:n_iterations
    m_g(1);
end
final_time = toc;
disp("Matlab:")
fprintf("\tQuadrature\t--");
fprintf("\t%s\n", scientific_time(final_time / n_iterations))