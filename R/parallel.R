library(parallel)

data <- 1:10
fun <- function(i) {
  return (sqrt(data[i]))
}

data.fun <- mclapply(1:length(data), fun, mc.cores=3)

library(foreach)
data.fun2 <- foreach (i=1:10, .combine=rbind ) %do% {
  fun(i)
}
