/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_nbrlen.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: motoure <marvin@42.fr>                     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2020/02/23 09:03:09 by motoure           #+#    #+#             */
/*   Updated: 2020/02/23 09:04:05 by motoure          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "lprintf.h"

int	ft_nbrlen(int n)
{
	int count;

	count = 0;
	if (n == 0)
		return (1);
	n = n < 0 ? ~n + 1 : n;
	while (n)
	{
		count++;
		n /= 10;
	}
	return (count);
}
