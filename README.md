Theseus README:
Author: Alex Whelan

Theseus is a simple maze-solving algorithm that will take an inputted maze and solve it.
It first checks to see if the agent's location is at an edge, and therefore an exit, and if so it completes the loop.
if not at an exit, it finds the agent and the available options (left, right, up or down). Any options that are walls are not considered,
and then highest priority is allocated to never-explored open paths, and then subsequently already-walked-down paths. From the option list,
the next step in the maze is randomly chosen, so it does not always find the shortest solution. Once a step is taken, it updates the maze with 
the new information (new location of agent and knowledge of where the agent has been), and another iteration is completed until the agent
reaches an exit and breaks the loop. 

Input: The maze should be inputted in a specific format: Wall = 'X', open path = 'O', and agent starting location = 'S'. 
	The algorithm prompts you to input this line-by-line in a seperate function called createmaze, which returns a maze variable
	(a correctly formatted maze).

Output: The function Theseus prints to the screen the journey of the agent stepwise, and prints a message when the maze is solved. 
	It returns a maze variable with the completed maze. A '1' in the maze indicates the path of the agent. 

Typical usage: maze = createmaze()
		finished_maze = Theseus(maze)

Future additions: 
	Finding the shortest path - This algorithm could be easily altered to find the shortest path by first scanning the maze and assigning
					the highest value to the open path at the exit, and then for each path adjacent to that square it would
					assign a smaller value. This would ensure a gradient of sorts that would propagate through the maze
					until all paths were assigned a value. Then, it would be trivial to follow the highest-value direction
					to the end of the maze. if two squares were equal in value this would mean they were equally close to
					exit so randomly choosing would not be a problem. 
	Finding all paths - The Theseus algorithm will find all paths by default as it prefers new paths to paths it's already been down. 
				However, if it reaches the exit before all paths have been discovered, it could miss one. Finding all paths
				would require either doubling back once an exit is found, or by using the value method outlined above, it could
				choose the lowest value when at an intersection and then double back on itself and choose the higher-value path. 
	Optimising - This algorithm is slow because of the stepwise nature of it. It could be improved by scanning the entire maze and 
			producing an entire path in one go. Then once the path is complete, it could simply draw it onto the maze.	
			Additionally, the printing to screen at each iteration and the high number of variables stored in memory will increase
			the computational demand of the algorithm. These could be removed or tidied up in future versions to improve efficiency.
	3D mazes - This would either be extremely trivial, as Python (and I know Tensorflow also) can deal with high dimensionality within data	
			types, or very hard. 

NB: At present, the algorithm does not distinguish between paths it's been down once, and more than once, so with large mazes it's possible
it could get stuck or waste time going down paths it's already been down. Future improvements using the memory of the agent could imrpove this
so it can tell when it's been in one area for too long. 
