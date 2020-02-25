/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   is_hidden.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: motoure <marvin@42.fr>                     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2020/02/23 09:31:11 by motoure           #+#    #+#             */
/*   Updated: 2020/02/23 09:31:17 by motoure          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "lprintf.h"

int	is_hidden(char *str)
{
	int i;

	i = 0;
	while (str[i])
	{
		if (!ft_isprint(str[i]))
			return (1);
		i++;
	}
	return (0);
}
