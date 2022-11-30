#include "lists.h"
#include <stdio.h>
int insert_number(listint_t num)
{
    node *temp, *temp2, *temp3;
    temp = malloc(sizeof(listint_t));
    temp->data = num;
    temp->next = NULL;
    if (head == NULL)
        head = temp;
    else{
        temp2 = head;
        while (temp->data > temp2->data)
        {
            temp3 = temp2;
            temp2 = temp2->next;
        }
        temp->next = temp2;
        temp3->next = temp;
    }
}
