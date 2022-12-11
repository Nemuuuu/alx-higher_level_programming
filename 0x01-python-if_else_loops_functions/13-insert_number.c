#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: pointer to pointer
 * @number: inserting number
 * 
 * Return: the address of the new node, or NULL if it failed
*/
listint_t *insert_node(listint_t **head, int number)
{
    listint_t *temp, *temp2, *temp3;
    temp = malloc(sizeof(listint_t));
    temp->n = number;
    temp->next = NULL;
    temp2 = *head;
    while (temp2->n < temp->n)
    {
        temp3 = temp2;
        temp2 = temp2->next;
    }
    temp3->next = temp;
    temp->next = temp2;
return (*head);
}
