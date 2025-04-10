# Final Sprint Changes
## Feature Changes
- Adam's head added
  - Adams head now appears over snake head
    - Involves main(), initialize(), and render() from driver.py
- Music
  - Background music now plays thoughout gameplay
    - Localized inside main() from driver.py
- Visuals
  - Colors changed to fit UNK theme
    - Change inside render()
  - Apple changed to pixel apple
    - Image loaded in main(), rendered in render()
- Collision
  - Added snake collision
    - Done by comparing the head rect to a list of corrdinate collide points of the body 
    
## Bug Fixes
- Apple is no longer able to spawn inside snake
  - Was previously checking the wrong coordinates, since the snake and apple coordinates are off by 10
    - Added 10 during if statement check
  - Was only effectively only checking last body part 
    - Changed check to see if something is spawning on the wrong spot and reflaging randomizing if it is, instead of not spawning on the wrong spot and unflagging randomizing if it is
- Snake can no longer turn backwards
  - Previously could with two rapid inputs
    - Fixed by using an extra variable to set next direction and comparing it to current direction
  - Previously an oversight allowed snake to turn backwards in one direction
    - Fixed by swapping an "and" for an "or"
