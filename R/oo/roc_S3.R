roc <- function(p, y) {
  o <- order(p, decreasing=T)
  p <- p[o]
  y <- y[o]
  t <- table(p, y)
  fpr <- cumsum(t[,1]) / sum(t[,1])
  tpr <- cumsum(t[,2]) / sum(t[,2])
  # Create a list
  roc <- list(fpr=fpr, tpr=tpr, call=sys.call())
  # Make this list an instance of class roc
  class(roc) <- "roc"
  return (roc)
}

# Method print of class roc
print.roc <- function(roc) {
  cat("Call: ", sprintf("%s", as.character(roc$call)), "\n")
}

# Method plot of class roc
plot.roc <- function(roc) {
  plot(roc$fpr, roc$tpr, t="l", lwd=2, col="darkgrey", xlab="FPR", ylab="TPR")
}

# Creating a new generic method
maxmean <- function(x, ...) UseMethod("maxmean", x) # create new generic method
maxmean.default <- function(x, y) max(mean(x), mean(y)) # overload method
maxmean.list <- function(x) max(mean(x$x), mean(x$y)) # overload method
maxmean(10:15, 6:10)
maxmean(list(x=1:5, y=10:15))
methods(maxmean)  # show methods



neg <- cbind(rnorm(50, 3, 1), rnorm(50, 3, 1), 0)
pos <- cbind(rnorm(50, 4, 1), rnorm(50, 2.5, 1), 1)
d <- rbind(neg, pos)
d <- as.data.frame(d)
colnames(d) <- c("x1", "x2", "y")
