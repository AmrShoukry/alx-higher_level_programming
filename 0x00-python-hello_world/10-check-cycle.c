#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * print_listint - prints all elements of a listint_t list
 * @h: pointer to head of list
 * Return: number of nodes
 */
size_t print_listint(const listint_t *h)
{
	const listint_t *current;
	unsigned int n; /* number of nodes */

	current = h;
	n = 0;
	while (current != NULL)
	{
		printf("%i\n", current->n);
		current = current->next;
		n++;
	}

	return (n);
}

/**
 * add_nodeint - adds a new node at the beginning of a listint_t list
 * @head: pointer to a pointer of the start of the list
 * @n: integer to be included in node
 * Return: address of the new element or NULL if it fails
 */
listint_t *add_nodeint(listint_t **head, const int n)
{
	listint_t *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = n;
	new->next = *head;
	*head = new;

	return (new);
}

/**
 * free_listint - frees a listint_t list
 * @head: pointer to list to be freed
 * Return: void
 */
void free_listint(listint_t *head)
{
	listint_t *current;

	while (head != NULL)
	{
		current = head;
		head = head->next;
		free(current);
	}
}

/**
 * check_cycle - check for cycles
 * @list: head of linked list
 * Return: 0 for no circles, 1 for circles
 */


int check_cycle(listint_t *list)
{
/*	listint_t *current_one = list->next;
	listint_t *current_two = list->next->next;
	
	while (current_one != current_two)
	{
		if (current_one == NULL || current_two == NULL)
			return (0);
		current_one = current_one->next;
		current_two = current_two->next->next;
	}
	return (1);
*/
	int n = 0;
	int i = 0;
	int *arr = malloc(sizeof(int) * 1);
	listint_t *current = list;

	while (current != NULL)
	{
		arr[n] = current->n;
		for (i = 0; i < n; i++)
			if (current->n == arr[i])
				return (1);
		arr = realloc(arr, (++n + 1) * sizeof(int));
		current = current->next;
	}
	return (0);
}
