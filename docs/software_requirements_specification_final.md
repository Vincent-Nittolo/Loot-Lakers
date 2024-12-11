# Overview
In this document you will find our functional and non-function requirements for our project Fortnite Monopoly.

# Software Requirements
For both our Functional and Non-Functional Requirements sections, we will have three categories/sections for particular features. Within each section, we will have atleast five requirements.

## Functional Requirements
### Graphical User Interface (GUI)
| ID | Requirement |
| :-------------: | :----------: |
| FR1| The GUI shall display animated dice rolls, and show the rolled value on the screen
| FR2| The GUI shall display an animated gameboard, where players' pieces are visually shown moving along the board, and each player's current position is highlighted in real-time.
| FR3| The GUI shall display a player selection screen at the start of the game, allowing the user to choose between 1 and 4 players.
| FR4|At the start of the game, the GUI shall display a character selection screen, allowing the user to choose from 4 unique characters. Once a character is selected, the user cannot select it again if it's already chosen.
| FR5| The GUI shall display an information section next to their icon, which shows the user's current health, balance, and other relevant statistics during gameplay. The health and money will update in real-time as the game progresses.
### Non-Player Character (CPU)
| ID | Requirement |
| :-------------: | :----------: |
| FR6| The CPU shall automatically roll the dice each turn.
| FR7| The CPU shall automatically purchase an available property.
| FR8| The CPU shall move around the game board automatically.
| FR9 |The CPU shall automatically use the characters(s) not chosen during the players selection screen.
| FR10|If the CPU lands on a property owned by the user, the CPU shall automatically transfer the rent amount to the user based on the property's rent value.
### Game Logic (Player Interactions)
| ID | Requirement |
| :-------------: | :----------: |
| FR11| Players shall be sent to jail when landing on "GO to jail", or when they roll doubles 3 times in a row. 
| FR12| Players shall have a live health bar that displays their health. When the health reaches 0, the player "dies" in the game.
| FR13| Players shall be able to roll the dice on their turn to progress throughout the board.
| FR14| Players shall be able to purchase spaces on the board, given they are unknowned, the player is currently located on the given space, and the player has enough materials.
| FR15| Players shall pay the owner of a space when it is landed on. This is the driving force of the game. If a player lands on a space owned by a different player and they do not have enough materials to pay, they shall lose a life, which will be noted with the health bar. 

## Non-Functional Requirements
### Performance and Scalability
| ID | Requirement |
| :-------------: | :----------: |
| NFR1 |The background music shall loop seamlessly without noticeable breaks or interruptions.|
| NFR2 | The background color change should take no more than 1 second to update after the user selects a new color.|
| NFR3 | The game shall provide an option to adjust the screen size dynamically to suit the user’s preferred resolution, without affecting the game’s performance. |
| NFR4 | The game shall allow the user to adjust the music volume seamlessly without noticeable delay or performance degradation.|
| NFR5 | The system should be able to scale to accommodate up to 4 users at once, ensuring smooth gameplay and low latency.|
### Settings and Rules
| ID | Requirement |
| :-------------: | :----------: |
| NFR6 | The settings shall allow the user to change the volume from 0(muted) to 100 in increments of 20.|
| NFR7 | The window size increase shall reveal a hidden easter egg found in the main game screen. This will allow the user to have more fun.|
| NFR8 | The easter egg shall play their given sound recordings when pressed. This will be used by the players for fun, potentially to taunt their friends or to add sound effects when something happens in the game. |
| NFR9 | The rules and settings screens shall adhere to the Fortnite theme, with the yellow and blue.|
| NFR10 | The rules shall explain how some of the spaces work, as well as how to win.|

# Software Artifacts
These are our software artifacts that we used throughout the development of the project.
* [Link to our Burn Down chart](BurnDown.pdf)
* [Link to our Use Case Diagram](../artifacts/use_case_diagram/use_case_diagram.jpeg)
* [Link to our Class Diagram](../artifacts/ClassDiagram.png)
- Still need Sequence or Communication Diagram
