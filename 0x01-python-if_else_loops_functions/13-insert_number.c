#include "lists.h"

/**
 * insert_node - insert node into the linked list
 * @head: head of list's value
 * Return: address of the new element or NULL if it fails
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current = *head;
	listint_t *previous = *head;
	listint_t *new = malloc(sizeof(listint_t));
	int found = 0;

	if (new == NULL)
		return (NULL);

	new->n = number;
	new->next = NULL;

	if (*head == NULL)
		*head = new;
	else
	{
		while (current != NULL)
		{
			if ((new->n) < (current->n))
			{
				if (current == *head)
				{
					new->next = *head;
					*head = new;
				}
				else
				{
					previous->next = new;
					new->next = current;
				}
				found = 1;
				break;
			}
			previous = current;
			current = current->next;
		}
		if (found == 0)
		{
			previous->next = new;
		}
	}

	return (new);
}

