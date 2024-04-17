function result = m_g(p)
    result = m_quad_trap(@(x) exp(p * x) - 10, -1, 1, 10000);
end