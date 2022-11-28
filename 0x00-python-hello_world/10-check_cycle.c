#include <stdio.h>
#include "lists.h"

/**
 * check_cycle - checks if singly linked list has cycle in it
 * @list: list to be checked
 *
 * Return: 0 if the list has no cycle, otherwise 1
 */
int check_cycle(listint_t *list)
{
	listint_t *head, *tail;

	if (list == NULL)
		return (0);
	head = tail = list;
	while (tail != NULL && tail->next != NULL)
	{
		head = head->next;
		tail = tail->next->next;
		if (head == tail)
			return (1);
	}
	return (0);
}
