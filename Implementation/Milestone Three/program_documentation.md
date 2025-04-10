# Program Documentation
## Added this milestone
  - Food
    - position_change()
      - changes the position of the apple to a random position
      - new position will be in line with what the snake can collect,
      - new position will additionally be the border and not where the snake is already
  - driver
    - apple_collision()
      - accepts a list of rects from the snake, a snake class variable, and a food class variable
      - checks if the snake is colliding with a collidepoint located at the position of the food
## Changed this milestone
  - driver
    - render()
      - changed how rendering works for collision
        - now stores rects drawn for the snake in the list snakes_squares
        - now stores the circle for the apple inside the variable apple
