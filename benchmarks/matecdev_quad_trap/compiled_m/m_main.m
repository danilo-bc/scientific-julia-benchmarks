n_iterations = 10000;

tic
for i = 1:n_iterations
    a = -1;
    b = 1;
    N = 10000;

    f_a = exp(1 * a) - 10;
    f_b = exp(1 * b) - 10;
    % quad_trap
    h = (b - a) / N;
    int = h * (f_a + f_b) / 2;
    for k = 1:N-1
        xk = (b - a) * k / N + a;
        f_xk = exp(1 * xk) - 10;
        int = int + h * f_xk;
    end
    r = int;
end

final_time = toc;
disp("Matlab:")
fprintf("\tQuadrature\t--");
time_per_it = final_time / n_iterations;

powers = [1e-12, 1e-9, 1e-6, 1e-3, 1, 60, 3600, 86400];
units = {'ps', 'ns', 'us', 'ms', 's', 'min', 'hr', 'day'};

[~, index] = min(abs(time_per_it - powers));

converted_time = time_per_it / powers(index);

time_string = sprintf('%.3f %s', converted_time, units{index});

fprintf("\t%s\n", time_string)