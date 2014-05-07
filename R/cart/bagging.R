data(iris)
t <- bagging(Species~Petal.Width+Sepal.Width, data=iris, coob=T)
print(t)
print(length(t$mtrees))
p <- predict(t)
plot(Petal.Width~Sepal.Width, data=iris, col=(as.integer(iris$Species)+1), pch=19, cex=1.0,
     main="True")
dev.new()
plot(Petal.Width~Sepal.Width, data=iris, col=(as.integer(iris$Species)+1), pch=19, cex=1.0,
     main="Prediction")
