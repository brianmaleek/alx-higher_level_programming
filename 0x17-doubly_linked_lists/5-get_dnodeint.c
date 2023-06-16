#include "lists.h"

/**
 * get_dnodeint_at_index - returns the nth node of a dlistint_t linked list
 * @head: pointer to head of list
 * @index: index of node to return
 * Return: nth node of a dlistint_t linked list or NULL if node does not exist
 */
dlistint_t *get_dnodeint_at_index(dlistint_t *head, unsigned int index)
{
	if (!head)
	{
		return (NULL);
	}
	while (index && head->next)
	{
		head = head->next;
		index--;
	}
	if (index == 0)
	{
		return (head);
	}
	return (NULL);
}
