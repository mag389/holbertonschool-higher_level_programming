#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
* insert_node - insters node at sorted location
* Return: address of new node or null if it failed
* @head: the head of the list
* @number: number to use as alue for new node
*/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *current;

	current = *head;
	if (head == NULL)
		return (NULL);

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;
	new->next = NULL;

	if (*head == NULL)
		*head = new;
	else
	{
		while (current->next && current->n < new->n)
			current = current->next;
		if (current->next)
			new->next = current->next;
		current->next = new;
	}
	return (new);
}
