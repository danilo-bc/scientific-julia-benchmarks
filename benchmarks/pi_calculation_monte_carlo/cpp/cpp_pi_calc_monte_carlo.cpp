#include <iostream>
#include <random>
#include <string>
#include <algorithm>
#include <ctime>

std::string scientific_time(double time_in_seconds) {
    std::pair<double, std::string> powers[] = {
        {1e-12, "ps"},
        {1e-9, "ns"},
        {1e-6, "μs"},
        {1e-3, "ms"},
        {1, "s"},
        {60, "min"},
        {3600, "hr"},
        {86400, "day"}
    };

    auto closest_power = *std::min_element(std::begin(powers), std::end(powers),
                                           [=](const auto &a, const auto &b) {
                                               return std::abs(time_in_seconds - a.first) < std::abs(time_in_seconds - b.first);
                                           });

    return std::to_string(time_in_seconds / closest_power.first) + " " + closest_power.second;
}

double pi_calc_internal_rng() {
    int j = 0;
    int i = 1;
    int n = 10000000;

    std::default_random_engine generator(time(0));
    std::uniform_real_distribution<double> distribution(0.0,1.0);

    while (i <= n) {
        double x = distribution(generator);
        double y = distribution(generator);
        i = i + 1;
        if (x * x + y * y <= 1) {
            j = j + 1;
        }
    }
    double pi = (double) j / n * 4;
    return pi;
}

double pi_calc_external_rng(std::default_random_engine &generator, std::uniform_real_distribution<double> &distribution) {
    int j = 0;
    int i = 1;
    int n = 10000000;

    while (i <= n) {
        double x = distribution(generator);
        double y = distribution(generator);
        i = i + 1;
        if (x * x + y * y <= 1) {
            j = j + 1;
        }
    }
    double pi = (double) j / n * 4;
    return pi;
}

int main() {
    /*
    Pseudorandom number generator, because it's good enough for the application and fast.
    A "true" RNG like std::random_device is way slower and doesn't bring benefits to this.
    */     
    // Considering internal RNG for each iteration (real scenario for benchmark)
    int n_iterations = 50;
    std::cout << "C++ with internal RNG n_iter = "<< n_iterations <<":" << std::endl;
    double average_time = 0;
    for (int i = 0; i < n_iterations; ++i) {
        clock_t start = clock();
        pi_calc_internal_rng();
        clock_t end = clock();
        double elapsed_time = double(end - start) / CLOCKS_PER_SEC;
        average_time += elapsed_time;
    }
    std::cout <<"\t"<< scientific_time(average_time / n_iterations) << std::endl;
    // Considering externally provided RNG for all iterations (a bit of a stretch)
    n_iterations = 1000000;
    std::default_random_engine generator(time(0));
    std::uniform_real_distribution<double> distribution(0.0,1.0);
    std::cout << "C++ with external RNG n_iter = "<< n_iterations << ":" << std::endl;
    average_time = 0;
    for (int i = 0; i < n_iterations; ++i) {
        clock_t start = clock();
        pi_calc_external_rng(generator, distribution);
        clock_t end = clock();
        double elapsed_time = double(end - start) / CLOCKS_PER_SEC;
        average_time += elapsed_time;
    }
    std::cout <<"\t"<< scientific_time(average_time / n_iterations) << std::endl;
    return 0;
}
