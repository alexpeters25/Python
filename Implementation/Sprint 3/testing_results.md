# Milestone Three Testing Results
## Functional Requirements Tests
- Desired results: Apple is collectable, Apple respawns after being collected, the score increases when apple is collected
  - Test: Snake touches apple
    - Result: When snake touches apple it disappears
    - Result: After disappearing the apple respawns elsewhere
    - Result: The score increments, and is visible in the window name. However, on devices with smaller screens the window name is not visible. This will be improved in the future.
## Security Requirements Tests
- Desired Results: Apple is accessible when respawning, Score only increments once and does not cause issues in program, and all previously implemented features function
  - Test: collect apples and note any invalid spawns
    - Result: collected 50 apples, no invalid spawns. This test will be repeated since there is not very much valid space currently it will be easier to test once the snake increases in size.
  - Test: manually increase score to see if it affects the programs function
    - [Result: When the score grows too large it simply trails off the window with a ...](https://github.com/alexpeters25/Python/blob/main/Implementation/Milestone%203/Images/Screenshot%202025-04-02%20134212.png) and program continues to function as intended
  - Test: Play game and note any oddities that do not work as intended
    - Result: It's too difficult for the snake to glide on the edge of the border ([example](https://github.com/alexpeters25/Python/blob/main/Implementation/Milestone%203/Images/Screenshot%202025-04-02%20134704.png), fixed by increasing valid play area by one pixel)
