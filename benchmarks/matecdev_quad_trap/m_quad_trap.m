function result = m_quad_trap(f, a, b, N)
    h = (b - a) / N;
    int = h * (f(a) + f(b)) / 2;
    for k = 1:N-1
        xk = (b - a) * k / N + a;
        int = int + h * f(xk);
    end
    result = int;
end