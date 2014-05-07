# Define class roc
setClass("roc", representation(fpr="numeric", tpr="numeric", call="call"))

roc <- function(p, y) {
  o <- order(p, decreasing=T)
  p <- p[o]
  y <- y[o]
  t <- table(p, y)
  fpr <- cumsum(t[,1]) / sum(t[,1])
  tpr <- cumsum(t[,2]) / sum(t[,2])
  # Create instance of class roc
  roc <- new("roc", fpr=fpr, tpr=tpr, call=sys.call())
  return (roc)
}

# Override the existing generic function show
# Reuse the interface show(object)
setMethod("show", "roc", function(object) {
          cat(sprintf("FPR: %.2f  TPR: %.2f\n", mean(object@fpr), mean(object@tpr)))
})

# Override the existing generic function plot
# Redefine the interface using signature(x="plot")
setMethod("plot", signature(x="roc"), function(x) {
          plot(x@fpr, x@tpr, t="l", lwd=2, col="darkgrey", xlab="FPR", ylab="TPR")
})

# Create new generic function
setGeneric("meanRoc", function(roc) {roc})

# Override new generic function
setMethod("meanRoc", "roc", function(roc) {
          cat(sprintf("FPR: %.2f   TPR: %.2f\n", mean(roc@fpr), mean(roc@tpr)))
})


neg <- cbind(rnorm(50, 3, 1), rnorm(50, 3, 1), 0)
pos <- cbind(rnorm(50, 4, 1), rnorm(50, 2.5, 1), 1)
d <- rbind(neg, pos)
d <- as.data.frame(d)
colnames(d) <- c("x1", "x2", "y")
gl <- glm(y ~ x1 + x2, data=d, family=binomial)
gl.p <- predict(gl, type="response")
r <- roc(gl.p, d$y)
r
