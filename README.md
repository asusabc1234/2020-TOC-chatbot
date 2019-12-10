## Finite State Machine
![fsm](./img/show-fsm.png)

## Usage
The initial state is set to `user`.

Type "restart" will goback to user state

* user
	* Input: "picture"		
		* Reply: "選擇東區或西區"
		* 西區
			* 請選擇分組
				* northwest divition
					* jazz -> jazz's picture
					* nuggets -> nuggets' picture
					* thunders -> thunders' picture
					* timberwolves -> timberwolves' picture
					* trail blazers -> trail blazers' picture
				* pacific divition
					* clippers -> clippers' picture
					* kings -> kings' picture
					* lakers -> lakers' picture
					* suns -> suns' picture
					* warriors -> warriors' picture
				* southwest divition
					* mavericks -> mavericks' picture
					* grizzles -> grizzles' picture
					* pelicans -> pelicans' picture
					* rockets -> rockets' picture
					* spurs -> spurs' picture
		* 東區
			* 請選擇分組
				* atalantic divition
					* raptors -> raptors' picture
					* celtics -> celtics' picture
					* 76ers -> 76ers' picture
					* nets -> nets' picture
					* knics -> knics' picture
				* central divition
					* bucks -> bucks' picture
					* pacers -> pacers' picture
					* pistons -> pistons' picture
					* bulls -> bulls' picture
					* caveliers -> caveliers' picture
				* southeast divition
					* heats -> heats' picture
					* magic -> magic's picture
					* hornets -> hornets' picture
					* wizards -> wizards' picture
					* hawks -> hawks' picture					

	* Input: "highlight"
		* Reply: "https://www.youtube.com/watch?v=l0sSxqSUXJY"
