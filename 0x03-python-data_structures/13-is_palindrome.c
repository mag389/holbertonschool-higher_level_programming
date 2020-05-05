#include "lists.h"
#include <stdio.h>
#include <stdlib.h>
#include <stddef.h>
int length(listint_t *head);
/**
* is_palindrome - checks if a linked list is a palindrome
* Return: 1 if it is, else 0
* @head: the head node of the linked list
*/
int is_palindrome(listint_t **head)
{
	listint_t *temp;
	int i, len, *stack;

	if (head == NULL || *head == NULL)
		return (1);
	len = length(*head);
	stack = malloc(sizeof(int) * len);
	if (stack == NULL)
		return (1);
	temp = *head;
	for (i = 0; i < len; i++)
	{
		stack[i] = temp->n;
		temp = temp->next;
	}
	temp = *head;
	for (i--; i > 0; i--)
	{
		if (temp->n != stack[i])
		{
			free(stack);
			return (0);
		}
		temp = temp->next;
	}
	free(stack);
	return (1);
}

/**
* length - gets length of linked list
* Return: the length
* @head: the head node
*/
int length(listint_t *head)
{
	int i;
	listint_t *temp = head;

	for (i = 0;; i++)
	{
		if (temp == NULL)
			return (i);
		temp = temp->next;
	}
}
