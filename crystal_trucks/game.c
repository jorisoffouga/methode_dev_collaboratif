#include "game.h"

/* https://en.wikipedia.org/wiki/Linear_congruential_generator glibc */
#define MODULUS (1 << 31)
#define MULTIPLIER (1103515245)
#define INCREMENT (12345)

static unsigned int prng;

void srand(unsigned int seed)
{
    prng = seed;
}

int rand(void)
{
    prng = (MULTIPLIER * prng + INCREMENT) % MODULUS;
    return (int)(prng & 0x7FFFFFFF);
}

static UART_HandleTypeDef huart;
int putchar(int c)
{
    unsigned char character = c;
    HAL_UART_Transmit(&huart, (uint8_t *)&character, 1, HAL_MAX_DELAY);
    return character;
}

int puts(char *text)
{
    while (*text)
        putchar(*text++);
    return 0;
}

char *itoa(int value, char *str, int base)
{
    if (base != 10 || value < 0)
    {
        while (1)
            ;
    }
    if (value == 0)
    {
        str[0] = '0';
        str[1] = 0;
    }
    else
    {
        uint8_t digits[32];
        uint8_t max_power = 0;
        uint8_t i;
        while (value)
        {
            digits[max_power++] = value % 10;
            value /= 10;
        }
        for (i = 0; i < max_power; i++)
            str[i] = digits[max_power - i - 1] + '0';
        str[max_power] = 0;
    }
    return str;
}

void display_cristals(uint8_t width, uint8_t height, uint8_t *cristals)
{
    puts("\r\n### Grid ###\r\n");
    for (int y = 0; y < height; y++)
    {
        for (int x = 0; x < width; x++)
        {
            uint8_t nb_cristals = cristals[x + y * width];
            if (nb_cristals)
                putchar('0' + nb_cristals);
            else
                putchar(' ');
        }
        puts("\r\n");
    }
    puts("### End Grid ###\r\n");
}

void init_game(unsigned int seed, UART_HandleTypeDef huart2, uint8_t *nb_trucks,
               uint8_t *width, uint8_t *height, uint8_t *cristals)
{
    char str[32];
    uint8_t x, y;
    huart = huart2;
    srand(seed);
    *nb_trucks = rand() % (MAX_NB_TRUCKS - 1) + 1;
    *width = rand() % (MAX_WIDTH - 10) + 10;
    *height = rand() % (MAX_HEIGHT - 10) + 10;
    for (y = 0; y < *height; y++)
        for (x = 0; x < *width; x++)
        {
            uint8_t nb_cristals = rand() % 5;
            if (nb_cristals < 3)
                cristals[x + y * *width] = nb_cristals;
            else
                cristals[x + y * *width] = 0;
        }
    puts("trucks: ");
    puts(itoa(*nb_trucks, str, 10));
    puts("\r\nwidth: ");
    puts(itoa(*width, str, 10));
    puts("\r\nheight: ");
    puts(itoa(*height, str, 10));
    display_cristals(*width, *height, cristals);
    puts("\r\nStart!\r\n");
}
