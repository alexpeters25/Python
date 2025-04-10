# Program Documentation
## Added This Milestone
- Food
  - this class controls variables pertaining food
  - variables:
    - __radius: stores radius of food
    - __curr_pos: stores the foods current position
  - functions:
    - this functions only has getters and setters as of milestone two
- driver.py
  - main()
    - program stops if snake.get_curr_direction is set to stop
    - additionally sets food variable using initialize()
  - initialize()
    - now also initializes food
  - render()
    - now also renders an apple as a circle, this does not have any interactivity as of milestone two
  - border()
    - this function check if the snakes position has exceeded the bounds of the window, and changes __curr_direction inside of the snake variable to "stop", which exits the game in the main loop
## Changed This Milestone
- Python
  - increased movement distance to match the length of the body to make turning cleaner later on
- driver.py
  - movement now only occurs every 100ms
