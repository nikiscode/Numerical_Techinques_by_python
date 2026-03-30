#include <stdio.h>
#include <stdlib.h>
// Function to return maximum of two numbers
int max(int a, int b) {
    return (a > b) ? a : b;
}
// 0/1 Knapsack using Dynamic Programming
int knapSack(int capacity, int weight[], int value[], int n) {

    // Dynamically allocate DP table
    int **dp = (int **)malloc((n + 1) * sizeof(int *));
    for (int i = 0; i <= n; i++) {
        dp[i] = (int *)malloc((capacity + 1) * sizeof(int));
    }

    // Initialize DP table
    for (int i = 0; i <= n; i++) {
        for (int w = 0; w <= capacity; w++) {
            if (i == 0 || w == 0)
                dp[i][w] = 0;
            else if (weight[i - 1] <= w)
                dp[i][w] = max(value[i - 1] + dp[i - 1][w - weight[i - 1]],
                               dp[i - 1][w]);
            else
                dp[i][w] = dp[i - 1][w];
        }
    }

    int result = dp[n][capacity];

    // Free allocated memory
    for (int i = 0; i <= n; i++) {
        free(dp[i]);
    }
    free(dp);

    return result;
}

int main() {

    int n, capacity;

    printf("Enter number of items: ");
    if (scanf("%d", &n) != 1 || n <= 0) {
        printf("Invalid input!\n");
        return 1;
    }

    int *weight = (int *)malloc(n * sizeof(int));
    int *value  = (int *)malloc(n * sizeof(int));

    if (weight == NULL || value == NULL) {
        printf("Memory allocation failed!\n");
        return 1;
    }

    printf("Enter %d weights:\n", n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &weight[i]);
    }

    printf("Enter %d values/profits:\n", n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &value[i]);
    }

    printf("Enter knapsack capacity: ");
    scanf("%d", &capacity);

    int maxValue = knapSack(capacity, weight, value, n);

    printf("Maximum value = %d\n", maxValue);

    // Free memory
    free(weight);
    free(value);

    return 0;
}
