# Program Documentation
## Added this milestone
  - [Food](https://github.com/alexpeters25/Python/blob/main/Implementation/Sprint%203/Code/food.py)
    - [position_change()](https://github.com/alexpeters25/Python/blob/main/Implementation/Sprint%203/Images/pos_change_s3.png)
      - changes the position of the apple to a random position
      - new position will be in line with what the snake can collect,
      - new position will additionally be the border and not where the snake is already
  - [driver.py](https://github.com/alexpeters25/Python/blob/main/Implementation/Sprint%203/Code/driver.py)
    - [apple_collision()](https://github.com/alexpeters25/Python/blob/main/Implementation/Sprint%203/Images/apple_collision_s3.png)
      - accepts a list of rects from the snake, a snake class variable, and a food class variable
      - checks if the snake is colliding with a collidepoint located at the position of the food
## Changed this milestone
  - driver
    - [render()](https://github.com/alexpeters25/Python/blob/main/Implementation/Sprint%203/Images/render_s3.png)
      - changed how rendering works for collision
        - now stores rects drawn for the snake in the list snakes_squares
        - now stores the circle for the apple inside the variable apple
