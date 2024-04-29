CXX = g++
CXXFLAGS = -O3 -std=c++20

cpp_pi_calc_monte_carlo: cpp_pi_calc_monte_carlo.cpp
	$(CXX) $(CXXFLAGS) -o $@ $^

.PHONY: clean
clean:
	rm -f cpp_pi_calc_monte_carlo
