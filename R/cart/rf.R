library(randomForest)
data(iris)

rf <- NA
for (i in 1:10) {
  f <- randomForest(Species ~ Petal.Width + Petal.Length, data=iris, proximity=T)
  if (i == 1) {
    rf <- f
  } else {
    rf <- combine(rf, f)
  }
}

plot(Petal.Length~Petal.Width, data=iris, pch=19, col=(as.integer(iris$Species)+1))
cc <- classCenter(iris[, c("Petal.Width", "Petal.Length")], iris$Species, rf$prox)
points(cc, pch=21, cex=2, col=c(2, 3, 4))

new.data <- data.frame(
                       Petal.Length=rnorm(500, 3, 2), 
                       Petal.Width=rnorm(500, 1.5, 1))
p <- predict(rf, newdata=new.data)
dev.new()
plot(Petal.Length~Petal.Width, data=new.data, pch=19, col=(as.integer(p)+1))

cv <- rfcv(iris[,1:4], iris[,5])
plot(cv$n.var, cv$err, t="l", xlab="Variables used", ylab="Error")
