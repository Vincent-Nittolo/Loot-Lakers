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

## Non-Functional Requirements
### Performance and Scalability
| ID | Requirement |
| :-------------: | :----------: |
| NFR1 |The background music should loop seamlessly without noticeable breaks or interruptions.|
| NFR2 | The background color change should take no more than 1 second to update after the user selects a new color.|
| NFR3 | The game shall provide an option to adjust the screen size dynamically to suit the user’s preferred resolution, without affecting the game’s performance. |
| NFR4 | The game shall allow the user to adjust the music volume seamlessly without noticeable delay or performance degradation.|
| NFR5 | The system should be able to scale to accommodate up to 4 users at once, ensuring smooth gameplay and low latency.|

# Software Artifacts
These are our software artifacts that we used throughout the development of the project.
* [Link to our Burn Down chart](BurnDown.pdf)
* [Link to our Use Case Diagram](Loot-Lakers/artifacts/use_case_diagram/use_case_diagram.jpeg)
- Still need Class or Object Diagram
- Still need Sequence or Communication Diagram
