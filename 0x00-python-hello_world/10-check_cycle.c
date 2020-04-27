#include "lists.h"

/**
* check_cycle - checks for cycle in cingly linked list
* Return: 0 for no cycle, 1 for cycle
* @list: the linked list to check
*/
int check_cycle(listint_t *list)
{
	listint_t *turt = list, *hare = list;

	if (list == NULL)
		return (0);
	hare = hare->next;
	if (hare == NULL)
		return (0);
	while (turt != NULL && hare != NULL)
	{
		if (hare == turt)
			return (1);
		turt = turt->next;
		hare = hare->next;
		if (hare == NULL)
			return (0);
		hare = hare->next;
	}
	return (0);
}
