
#include "lprintf.h"

int main(void)
{
    char *str = NULL;

    int i = 0;
    while (i < 3)
    {
        ft_putchar_str(&str, 31);
        i++;
    }
    ft_printf("%3.s", str);
}