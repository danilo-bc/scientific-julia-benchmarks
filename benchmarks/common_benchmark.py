def scientific_time(time_in_seconds):
    """String of time converted to closest scientific representation

    Args:
        time_in_seconds (double): time in seconds

    Returns:
        str: Converted time. e.g., 0.005 => 5 ms
    """
    powers = [(1e-12, 'ps'), (1e-9, 'ns'), (1e-6, 'μs'), (1e-3, 'ms'), (1, 's'), (60, 'min'), (3600, 'hr'), (86400, 'day')]
    
    closest_power = min(powers, key=lambda x: abs(time_in_seconds - x[0]))
    return f"{time_in_seconds / closest_power[0]:.3f} {closest_power[1]}"