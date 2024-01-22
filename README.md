
## Game instruction
<ol>
  <li> game mode
  <ul>
    <li> press 'p' to play pvp mode
    <li> press 'b' to play ai mode
    <li> press 0, 1, 2, 3 to choose level of ai
  </ul>
  <li> game start
    <ul>
      <li> press 's' to switch first to play
      <li> press 'enter' to start
      <li> press 'r' to restart game
      <li> press 'n' to new game 
    </ul>

## Minimax
  * Basic minimax with alpha-beta prunning
  * I have used 2 heuristic functions to evaluate state of board which are naive and basic.
    * Naive evaluation take a board state and check if anyone wins:
      - If 'X' wins, +1 
      - If 'O wins, -1 
      - If no wins, 0
    * Basic evaluation:
      - +100 for each 3-in-a-line for X (-100 for O)
      - +10 for each 2-in-a-line (with a empty cell) for X (-10 for O)
      - +1 for each 1-in-a-line (with two empty cells) for X (-1 for O)
  * It is clear that basic evaluation is better than naive evaluation
## Future Work
  * Make a more efficiency heuristic function with threat-based evaluation
  * Make a AI can play NxN board
  * Implement more techniques to improve minimax:
    * Pre-sort options to be choose
    * Check for force moves
    * Implement AI algorithm parallelly 
  * Design game with better pattern: Command pattern, Strategy pattern