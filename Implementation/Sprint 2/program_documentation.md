# Program Documentation
## Added This Milestone
- [Food](https://github.com/alexpeters25/Python/blob/main/Implementation/Sprint%202/Code/food.py)
  - this class controls variables pertaining food
  - variables:
    - __radius: stores radius of food
    - __curr_pos: stores the foods current position
  - functions:
    - this functions only has getters and setters as of milestone two
- [driver.py](https://github.com/alexpeters25/Python/blob/main/Implementation/Sprint%202/Code/driver.py)
  - [main()](https://github.com/alexpeters25/Python/blob/main/Implementation/Sprint%202/Images/main_s2.png)
    - program stops if snake.get_curr_direction is set to stop
    - additionally sets food variable using initialize()
  - [initialize()](https://github.com/alexpeters25/Python/blob/main/Implementation/Sprint%202/Images/initialize_s2.png)
    - now also initializes food
  - [render()](https://github.com/alexpeters25/Python/blob/main/Implementation/Sprint%202/Images/render_s2.png)
    - now also renders an apple as a circle, this does not have any interactivity as of milestone two
  - [border()](https://github.com/alexpeters25/Python/blob/main/Implementation/Sprint%202/Images/border_s2.png)
    - this function checks if the snakes position has exceeded the bounds of the window, and changes __curr_direction inside of the snake variable to "stop", which exits the game in the main loop
## Changed This Milestone
- Python
  - [increased movement distance to match the length of the body](https://github.com/alexpeters25/Python/blob/main/Implementation/Sprint%202/Images/change_head_pos_s2.png) to make turning cleaner later on
- [driver.py](https://github.com/alexpeters25/Python/blob/main/Implementation/Sprint%202/Code/driver.py)
  - [movement now only occurs every 100ms](https://github.com/alexpeters25/Python/blob/main/Implementation/Sprint%202/Images/movement_timer_s2.png)
