#include <stdio.h>
#include <conio.h>
#include <graphics.h>
#include <stdlib.h> // Required for exit function

#define SCREEN_WIDTH 640
#define SCREEN_HEIGHT 480
#define PADDLE_WIDTH 10
#define PADDLE_HEIGHT 60
#define BALL_SIZE 10

int paddle1_x = 20, paddle1_y = SCREEN_HEIGHT / 2 - PADDLE_HEIGHT / 2;
int paddle2_x = SCREEN_WIDTH - 30, paddle2_y = SCREEN_HEIGHT / 2 - PADDLE_HEIGHT / 2;
int ball_x = SCREEN_WIDTH / 2, ball_y = SCREEN_HEIGHT / 2;
int ball_dx = 2, ball_dy = 2;
int score1 = 0, score2 = 0;

void initGraphics() {
    int gd = DETECT, gm;
    initgraph(&gd, &gm, ""); // Path is not needed for Dev C++
}

void drawGame() {
    cleardevice(); // Clear screen

    // Draw paddles
    rectangle(paddle1_x, paddle1_y, paddle1_x + PADDLE_WIDTH, paddle1_y + PADDLE_HEIGHT);
    rectangle(paddle2_x, paddle2_y, paddle2_x + PADDLE_WIDTH, paddle2_y + PADDLE_HEIGHT);

    // Draw ball
    circle(ball_x, ball_y, BALL_SIZE);

    // Display scores
    char scoreText[50];
    sprintf(scoreText, "Player 1: %d  Player 2: %d", score1, score2);
    outtextxy(SCREEN_WIDTH / 2 - textwidth(scoreText) / 2, 10, scoreText);
}

void updateGame() {
    ball_x += ball_dx;
    ball_y += ball_dy;

    // Ball collision with top/bottom
    if (ball_y <= BALL_SIZE || ball_y >= SCREEN_HEIGHT - BALL_SIZE) {
        ball_dy = -ball_dy;
    }

    // Ball collision with paddles
    if ((ball_x <= paddle1_x + PADDLE_WIDTH && ball_y >= paddle1_y && ball_y <= paddle1_y + PADDLE_HEIGHT) ||
        (ball_x >= paddle2_x - BALL_SIZE && ball_y >= paddle2_y && ball_y <= paddle2_y + PADDLE_HEIGHT)) {
        ball_dx = -ball_dx;
    }

    // Ball out of bounds (score update)
    if (ball_x <= 0) {
        score2++;
        ball_x = SCREEN_WIDTH / 2;
        ball_y = SCREEN_HEIGHT / 2;
        ball_dx = -ball_dx;
    }
    if (ball_x >= SCREEN_WIDTH) {
        score1++;
        ball_x = SCREEN_WIDTH / 2;
        ball_y = SCREEN_HEIGHT / 2;
        ball_dx = -ball_dx;
    }
}

void handleInput() {
    if (kbhit()) {
        char ch = getch();
        // Exit game with 'Esc' key
        if (ch == 27) { // 27 is the ASCII code for the 'Esc' key
            closegraph(); // Close graphics mode
            exit(0);
        }
        // Move paddle1
        if (ch == 'w' && paddle1_y > 0) {
            paddle1_y -= 5;
        }
        if (ch == 's' && paddle1_y < SCREEN_HEIGHT - PADDLE_HEIGHT) {
            paddle1_y += 5;
        }
        // Move paddle2
        if (ch == 'i' && paddle2_y > 0) {
            paddle2_y -= 5;
        }
        if (ch == 'k' && paddle2_y < SCREEN_HEIGHT - PADDLE_HEIGHT) {
            paddle2_y += 5;
        }
    }
}

int main() {
    int result;

    initGraphics();

    result = graphresult(); // Check for initialization errors
    if (result != grOk) {
        printf("Graphics initialization error: %s\n", grapherrormsg(result));
        getch(); // Wait for a key press before closing
        return 1;
    }

    while (1) {
        drawGame();
        updateGame();
        handleInput();
        delay(20); // Control the game speed
    }

    closegraph(); // Close graphics mode
    return 0;
}

