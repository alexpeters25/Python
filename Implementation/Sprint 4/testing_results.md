# Milestone Four Testing Results
## Functional Requirements Testing
- Test: Control the snake to collect apples.
  - Result: When the snake collects apples it grows in size, working as intended.
  - Result: As snake is controlled it's body follows the path of the head, working as intended.
- Test: Attempt to turn into the opposite direction.
  - Result: Turning backwards does not work, except for right to left. This is planned to be fixed before the next milestone.
  - Result: If two directions are pressed in quick succession it is possible to turn 180 degrees on the spos. This will be fixed by applying the same time delay to input gathering as the actual movement.
## Security Requirements Testing
- Test: Collect apples and note if at any point the apple spawns inside of the snake, or if the snake length adding does not work as intended.
  - Result: Apples are currently able to spawn in the snake. We are not currently aware of why this is happening, but are in the process of troubleshooting it.
  - Result: At no point was there a gap in the body or the the tail spawned in an incorrect possition, working as intended.
- Test: Test if game ends when running into border.
  - Result: Game ends when expected while running into border.
- Test: Control snake and note if it's movement operates on the same grid as the pattern.
  - Result: Snakes squares are all rendered on the same grid as the pattern, working as intended.
