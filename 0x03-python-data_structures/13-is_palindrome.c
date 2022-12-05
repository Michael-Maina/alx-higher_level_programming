#include "lists.h"
#include <stdio.h>

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: beginning node of linked list
 *
 * Return: 0 if not a palindrome, 1 if palindrome
 */

int is_palindrome(listint_t **head)
{
	listint_t *rev_list = NULL, *current, *new;
	int i = 0, j = 0, temp;

	current = *head;
	while (current != NULL)
	{
		i++;
		add_nodeint_end(&rev_list, current->n);
		current = current->next;
	}

	i--;
	while (i > 0)
	{
		j = 0;
		current = rev_list;
		while (j < i && current->next)
		{
			temp = current->n;
			current->n = current->next->n;
			current->next->n = temp;
			current = current->next;
			j++;
		}
		i--;
	}
	current = *head;
	new = rev_list;
	while (current != NULL)
	{
		if (current->n != new->n)
		{
			free_listint(rev_list);
			return (0);
		}
		current = current->next;
		new = new->next;
	}
	free_listint(rev_list);
	return (1);
}
