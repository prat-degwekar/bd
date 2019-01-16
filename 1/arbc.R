library("arulesCBA")
data("iris")

# learn a classifier using automatic default discretization
classifier <- CBA(Species ~ ., data = iris, supp = 0.05, conf = 0.9)
print(classifier)
print(predict(classifier, head(iris)))

