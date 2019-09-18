#  Buổi 2: Linear Regression 

## Absolute Trick
- If the point is above the line:
`y = (w1 +α⋅p)⋅x+(d+α)` 

- If the point is bellow the line:
`y = (w1 −α⋅p)⋅x+(d−α)` 

### Why do we need the p?
- If p is on the left of the y-axis, it's a negative number. Therefore we rotate the line in the correct direction.
- If the distance to the y-axis is small, we want to add a small number. Otherwise, we are going to add a large number.

![](https://www.upsieutoc.com/images/2019/09/19/Screen-Shot-2019-09-19-at-12.20.53-AM.png)

## Squared Trick
Idea: If the point is close to the line, we want to move the line more than when it's close.

`(y = (w1 +p(q−q′)α)⋅x+(d+(q−q′)α)`  

![](https://www.upsieutoc.com/images/2019/09/19/imagee424c0d476b032c5.png)

## Linear Regression Warnings
### Linear Regression Works Best When the Data is Linear
Linear regression produces a straight line model from the training data. If the relationship in the training data is not really linear, you'll need to either make adjustments (transform your training data), add features or use another kind of model.
### Linear Regression is Sensitive to Outliers
Linear regression tries to find a 'best fit' line among the training data. If your dataset has some outlying extreme values that don't fit a general pattern, they can have a surprisingly large effect.

## Link Slide
https://docs.google.com/presentation/d/1aMM4wcAT3ksin5265UIcy8ZTirIuxIEFriXUzUlMJtA/edit?usp=sharing

## Note dành cho các bạn
 - Hãy làm bài tập đầy đủ


### Chúc các bạn học tập tốt <3