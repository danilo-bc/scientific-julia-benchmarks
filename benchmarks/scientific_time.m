function time_string = scientific_time(time_in_seconds)
    % Powers of time and their corresponding units
    powers = [1e-12, 1e-9, 1e-6, 1e-3, 1, 60, 3600, 86400];
    units = {'ps', 'ns', 'μs', 'ms', 's', 'min', 'hr', 'day'};

    % Find the closest power of time
    [~, index] = min(abs(time_in_seconds - powers));

    % Convert time to the closest power
    converted_time = time_in_seconds / powers(index);

    % Generate the time string
    time_string = sprintf('%.3f %s', converted_time, units{index});
end
