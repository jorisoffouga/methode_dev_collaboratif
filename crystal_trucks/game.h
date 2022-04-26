#ifndef GAME_H
#define GAME_H

#include <stdint.h>
#include "stm32f4xx_hal.h"

/* standard library */
void srand(unsigned int seed);
int rand(void);
int putchar(int c);
int puts(char *text);
char *itoa(int value, char *str, int base); /* only base=10 and value>=0 is supported */

/* game specific */
#define MAX_NB_TRUCKS (9)
#define MAX_WIDTH (30)
#define MAX_HEIGHT (20)
void init_game(
    unsigned int seed, UART_HandleTypeDef huart2, uint8_t *nb_trucks,
    uint8_t *width, uint8_t *height, uint8_t *cristals);
void display_cristals(uint8_t width, uint8_t height, uint8_t *cristals);

#endif
