#include <cs50.h>
#include <stdio.h>

int main(void)
{

    int initial_size, final_size, years = 0;
    // TODO: Prompt for start size
    do
    {
        initial_size = get_int("Start Size: ");
    }
    while (initial_size < 9);

    // TODO: Prompt for end size
    do
    {
        final_size = get_int("End Size: ");
    }
    while (final_size < initial_size);

    // TODO: Calculate number of years until we reach threshold
    while (initial_size < final_size)
    {
        initial_size += initial_size / 3 - initial_size / 4;
        years++;
    }
    // TODO: Print number of years
    printf("Years: %i\n", years);
}
