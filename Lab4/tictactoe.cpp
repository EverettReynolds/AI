#include <iostream>
#include <string>
#include<cstdlib>
using namespace std;

enum Player {
	Human = -1,
	Blank = 0,
	Computer = 1
};

void printBoard(Player board[]);
void playGame(Player board[]);
int humanMove(Player board[]);
int roboMove(Player board[]);
Player check(Player board[]);

/*
 *
 *    In your playGame method, you will set up a loop like this :
 *    while (true)
 *    {
 *    		Human makes move & check for winner
 *    		Machine makes best move & check for winner
 *    		Exit when winner found
 *    }
 *
 *    When human selects, remember to input-- to be in range on your array.
 *
 *    HINT when human moves:
 *                    Player human = Human;
 *                    board[input] = human;
 *    HINT when computer moves:
 *                    Player computer = Computer;
 *                    board[input] = computer;
 *

 *
 * */

void playGame( Player board[] )
{

	int moveNum = 0;

	while(true)
	{
		int human = humanMove(board);
		while(human = -1)
		{
			human = humanMove(board);
		}
		
		board[human] = Human;
		moveNum = moveNum + 1;
		printBoard(board);

		if(check(board) == Human)
		{
			cout << " The Human Has Won! " << endl;
			exit(0);
		}
		
		int comp = roboMove(board);
		board[comp] = Computer;
		printBoard(board);

		if(check(board) == Computer)
		{
			cout << " The Computer Has Won! " << endl;
			exit(0);
		}
		if(moveNum >= 5)
		{
			break;
		}



	}
	if(moveNum >= 5)
	{
		cout << " No More Moves can Be Made, It is A Draw." << endl;
	}

}

int humanMove( Player board[] )
{
	int hum;
	cout << "Where Is Your Next Move?" << endl;
	cin >> hum;

	if(board[hum-1] == 0)
	{
		return hum-1;
	}
	if(hum > 8)
	{
		cout << "You Made An Invalid Move, Try Again." << endl;
		return -1;
	}
	else
	{
		cout << "You Made An Invalid Move, Try Again." << endl;
		return -1;
	}
	return hum;
}

int roboMove( Player board[] )
{
	int robo;
	//if()
	return robo;
}

Player check( Player board[] )
{
	Player play;

	if(board[0] == -1 && board[3] == -1 && board[6] == -1)
	{
		play = Human;
	}
	else if(board[1] == -1 && board[4] == -1 && board[7] == -1)
	{
		play = Human;
	}
	else if(board[2] == -1 && board[5] == -1 && board[8] == -1)
	{
		play = Human;
	}
	else if(board[0] == -1 && board[1] == -1 && board[2] == -1)
	{
		play = Human;
	}
	else if(board[3] == -1 && board[4] == -1 && board[5] == -1)
	{
		play = Human;
	}
	else if(board[6] == -1 && board[7] == -1 && board[8] == -1)
	{
		play = Human;
	}
	else if(board[0] == -1 && board[4] == -1 && board[8] == -1)
	{
		play = Human;
	}
	else if(board[2] == -1 && board[4] == -1 && board[6] == -1)
	{
		play = Human;
	}
	else if(board[0] == 1 && board[3] == 1 && board[6] == 1)
	{
		play = Computer;
	}
	else if(board[1] == 1 && board[4] == 1 && board[7] == 1)
	{
		play = Computer;
	}
	else if(board[2] == 1 && board[5] == 1 && board[8] == 1)
	{
		play = Computer;
	}
	else if(board[0] == 1 && board[1] == 1 && board[2] == 1)
	{
		play = Computer;
	}
	else if(board[3] == 1 && board[4] == 1 && board[5] == 1)
	{
		play = Computer;
	}
	else if(board[6] == 1 && board[7] == 1 && board[8] == 1)
	{
		play = Computer;
	}
	else if(board[0] == 1 && board[4] == 1 && board[8] == 1)
	{
		play = Computer;
	}
	else if(board[2] == 1 && board[4] == 1 && board[6] == 1)
	{
		play = Computer;
	}
	else
	{
		play = Blank;
	}



	return play;
}


int main() {
	char play = 'Y';

	while(play == 'Y') {
		Player board[9] = {Blank,Blank,Blank,Blank,Blank,Blank,Blank,Blank,Blank};
		printBoard(board);
		playGame(board);
		cout << "Do you want to play again? (Y/N) ";
		cin >> play;
		cout << endl;
	}
	return 0;
}

void printBoard(Player board[]) {
	
	for(int i = 0; i < 9; i++) {
		if((i == 2) || (i == 5) || (i == 8)) {
			if(board[i] == -1)
				cout << " X";
			else if (board[i] == 1)
				cout << " O";
			else
				cout << "  ";
		} else {
			if(board[i] == -1)
                                cout << "  X |";
                        else if (board[i] == 1)
                                cout << "  O |";
                        else
                                cout << "    |";
		}
		if(((i+1)%3 == 0) && (i != 8)) {
			cout << endl << "----|----|----" << endl;
		}
		if(i == 8)
			cout << endl;
	}

}
