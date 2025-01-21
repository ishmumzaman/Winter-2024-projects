# 2D Banana Attack Game

This project is a humorous 2D game created using the pygame library. (Initial idea was to make a Space Invasion like game)The main idea came from a personal interest in game development and a desire to learn how pygame works. The player sprite is a picture of me, and the enemy sprite is a picture of a friend. I made this project as a birthday gift, where a banana projectile is used to shoot my friend’s image. Through making this project, I gained a deeper understanding of how event loops, collisions, sprite movement, and sound playback function in pygame.

## Summary of the Game

1) The game displays a background image and plays background music continuously.  
2) The player sprite can move left and right at the bottom of the screen.  
3) The enemy sprites move horizontally and descend slightly each time they reach the left or right boundary.  
4) The player shoots banana bullets, and each successful collision with an enemy increases the score.  
5) If an enemy reaches the bottom of the screen, the game ends with a “GAME OVER” message.  

## Main Components

### Pygame Initialization and Screen Setup

The script calls pygame.init() to initialize the library. It then creates an 800 by 600 pixel window using pygame.display.set_mode(). The window title, icon, and background image are also set here.

### Player Movement

The player’s (my) image is loaded and displayed at a chosen position near the bottom of the screen. Horizontal movement is controlled by a variable that updates the player’s x coordinate in the main loop. There are checks to ensure the player sprite remains within screen boundaries.

### Enemy Behavior

Multiple enemy sprites are stored in lists for their images, x positions, y positions, x movements, and y movements. Each enemy moves horizontally, reversing direction upon hitting a boundary. They also move downward slightly after each reversal. If an enemy’s y coordinate reaches a certain limit, the game ends.

### Shooting Bananas

Pressing the spacebar triggers a banana projectile. Only one banana is active at a time. Its position is tracked through the bullet_x and bullet_y variables. When the bullet moves off the top of the screen, it is reset to the player’s position and becomes inactive until the player fires again.

### Collisions and Scoring

Distance-based collision detection is handled by a function that computes the Euclidean distance between the centers of two sprites. If this distance is below a certain threshold, a collision is declared, leading to an increase in the score and a reset of the bullet and enemy positions.

### Sound Effects and Music

Background music loops continuously using mixer.music.play(-1). Additional sound effects are triggered on firing the banana and on successful enemy hits.

### Ending the Game

The game loop constantly checks for the player closing the window and for enemy sprites reaching the bottom of the screen. If an enemy crosses the bottom limit, all enemies move far out of the visible area and a “GAME OVER” message is displayed.

## Possible Enhancements

1) Adding more variety in enemy types, possibly with different movement speeds or patterns.  
2) Creating a start menu or pause menu for a more polished feel.  
3) Including multiple levels with increasing difficulty.  
4) Using sprite animations for both player and enemies.  
5) Keeping track of high scores and providing a scoreboard.

## Learning Outcomes

In building this game, I learned the basics of pygame, including game loops, event handling, collision detection, and audio playback. The project served as a fun introduction to game development and offered a chance to customize all visuals and sounds, ultimately producing a humorous shooter game.
