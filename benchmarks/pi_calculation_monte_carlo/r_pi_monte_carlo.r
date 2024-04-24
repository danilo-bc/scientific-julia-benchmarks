library(rbenchmark)

pi_calc <- function() {
    j <- 0
    i <- 1
    n <- 1e7
    while (i <= n) {
        x <- runif(1)
        y <- runif(1)
        i <- i + 1
        if (x^2 + y^2 <= 1) {
            j <- j+1
        }
    }
    pi <- j/n*4
    return(pi)
}

print("Regular R:")
bench_pi <- benchmark(pi_calc(), iterations = 1, quiet = TRUE)
print(bench_pi)