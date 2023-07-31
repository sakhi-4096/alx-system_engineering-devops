#include <stdio.h> /* printf */
#include <stdlib.h> /* exit */
#include <unistd.h> /* fork, sleep */

/**
 * infinite_while - Create infinite sleep loop
 *
 * Return: 0
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main	- Create 5 zombie processes
 * Return: infinite_while zombies
 */
int main(void)
{
	pid_t zombiePID;
	unsigned int i;

	for (i = 0; i < 5; i++)
	{
		zombiePID = fork();
		if (zombiePID == 0)
			exit(0);
		else
			printf("Zombie process created, PID: %d\n", zombiePID);
	}

	return (infinite_while());
}
