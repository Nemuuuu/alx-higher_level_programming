#include "lists.h"
#include <stdio.h>
listint_t *insert_node(listint_t **head, int number)
{
    listint_t *temp, *temp2, *temp3;
    temp = malloc(sizeof(listint_t));
    temp->n = number;
    temp->next = NULL;
    if (head == NULL)
        head = temp;
    else{
        temp2 = head;
        while (temp->n > temp2->n)
        {
            temp3 = temp2;
            temp2 = temp2->next;
        }
        temp->next = temp2;
        temp3->next = temp;
    }
}
