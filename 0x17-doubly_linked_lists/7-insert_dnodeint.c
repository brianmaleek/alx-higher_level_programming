#include "lists.h"

/**
 * insert_dnodeint_at_index - inserts a new node at a given position
 * @h: pointer to pointer to head of list
 * @idx: index of list where new node should be added
 * @n: value of new node
 * Return: address of new node or NULL if it failed
 */
dlistint_t *insert_dnodeint_at_index(dlistint_t **h, unsigned int idx, int n)
{
	dlistint_t *node, *current;

	if (h == NULL)
	{
		return (NULL);
	}
	if (idx == 0)
	{
		return (add_dnodeint(h, n));
	}
	current = *h;
	while (idx > 1)
	{
		if (current == NULL)
		{
			return (NULL);
		}
		current = current->next;
		idx--;
	}
	if (current == NULL)
	{
		return (NULL);
	}
	if (current->next == NULL)
	{
		return (add_dnodeint_end(h, n));
	}
	node = malloc(sizeof(dlistint_t));
	if (node == NULL)
	{
		return (NULL);
	}
	node->n = n;
	node->next = current->next;
	node->prev = current;
	current->next->prev = node;
	current->next = node;
	return (node);
}
