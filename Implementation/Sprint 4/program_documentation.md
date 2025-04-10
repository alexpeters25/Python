# Program Documentation
## Added this milestone
- Python
  - Variables
    - __previous_position: stores the previous position of the end of the snake
  - Functions
    - [change_body_positions](https://github.com/alexpeters25/Python/blob/main/Implementation/Milestone%20Four/Images/change_body_positions.png)
      - Passes coordinates down the individual snake body parts so the body will follow the head.
    - [increase_size](https://github.com/alexpeters25/Python/blob/main/Implementation/Milestone%20Four/Images/increase_size.png)
      - Increases the size of the snake by appending a new position using the previous_position variable
## Changed this milestone
- Python
  - [change_head_pos](https://github.com/alexpeters25/Python/blob/main/Implementation/Milestone%20Four/Images/change_head_pos.png)
    - Now stores previous position at begining of function inside the previous_position variable
    - Now calls change_body_position() inside all cases, this ensures the body only moves when curr_direction is not "none"
- Driver
  - [apple_collision](https://github.com/alexpeters25/Python/blob/main/Implementation/Milestone%20Four/Images/apple_collision.png)
    - Now also calls snake.increase_size to increase the size of the snake
