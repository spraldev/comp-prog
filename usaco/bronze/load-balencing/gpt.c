#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <limits.h>

#define MIN(a,b) ((a) < (b) ? (a) : (b))

typedef struct {
    int x;
    int y;
} Cow;

typedef struct {
    int index;
    int diff;
} Candidate;

// Comparison function for qsort (integers)
int cmp_int(const void *a, const void *b) {
    int arg1 = *(const int *)a;
    int arg2 = *(const int *)b;
    return (arg1 > arg2) - (arg1 < arg2);
}

// Comparison function for qsort (Candidate based on diff)
int cmp_candidate(const void *a, const void *b) {
    Candidate *ca = (Candidate *)a;
    Candidate *cb = (Candidate *)b;
    return ca->diff - cb->diff;
}

// Count the maximum number of cows in any quadrant given a fence position (x, y)
int count_points(double x, double y, Cow *cows, int N) {
    int q1 = 0, q2 = 0, q3 = 0, q4 = 0;
    for (int i = 0; i < N; i++) {
        if (cows[i].x > x && cows[i].y > y)
            q1++;
        else if (cows[i].x < x && cows[i].y > y)
            q2++;
        else if (cows[i].x < x && cows[i].y < y)
            q3++;
        else
            q4++;
    }
    int max_q = q1;
    if (q2 > max_q) max_q = q2;
    if (q3 > max_q) max_q = q3;
    if (q4 > max_q) max_q = q4;
    return max_q;
}

// Count the absolute difference between the number of cows on the right and left of x
int count_points_x(double x, Cow *cows, int N) {
    int right = 0, left = 0;
    for (int i = 0; i < N; i++) {
        if (cows[i].x > x)
            right++;
        else
            left++;
    }
    return abs(right - left);
}

// Count the absolute difference between the number of cows above and below y
int count_points_y(double y, Cow *cows, int N) {
    int above = 0, below = 0;
    for (int i = 0; i < N; i++) {
        if (cows[i].y > y)
            above++;
        else
            below++;
    }
    return abs(above - below);
}

int solve(int N, Cow *cows) {
    // Allocate arrays for x and y values.
    int *x_vals = malloc(N * sizeof(int));
    int *y_vals = malloc(N * sizeof(int));
    for (int i = 0; i < N; i++) {
        x_vals[i] = cows[i].x;
        y_vals[i] = cows[i].y;
    }
    
    // Sort the coordinate arrays.
    qsort(x_vals, N, sizeof(int), cmp_int);
    qsort(y_vals, N, sizeof(int), cmp_int);
    
    int candidate_count = N - 1;  // number of adjacent pairs
    
    // Allocate candidate arrays for x and y.
    Candidate *x_res = malloc(candidate_count * sizeof(Candidate));
    Candidate *y_res = malloc(candidate_count * sizeof(Candidate));
    
    for (int i = 1; i < N; i++) {
        double xMid = ((double)x_vals[i] - x_vals[i - 1]) / 2.0 + x_vals[i - 1];
        x_res[i - 1].index = i;  // index in the sorted x_vals array
        x_res[i - 1].diff = count_points_x(xMid, cows, N);
    }
    
    for (int i = 1; i < N; i++) {
        double yMid = ((double)y_vals[i] - y_vals[i - 1]) / 2.0 + y_vals[i - 1];
        y_res[i - 1].index = i;  // index in the sorted y_vals array
        y_res[i - 1].diff = count_points_y(yMid, cows, N);
    }
    
    // Sort candidate arrays based on their difference value.
    qsort(x_res, candidate_count, sizeof(Candidate), cmp_candidate);
    qsort(y_res, candidate_count, sizeof(Candidate), cmp_candidate);
    
    int xCount = MIN(800, candidate_count);
    int yCount = MIN(800, candidate_count);
    
    // Build the final candidate fence positions.
    int *x_final = malloc(xCount * sizeof(int));
    int *y_final = malloc(yCount * sizeof(int));
    
    for (int i = 0; i < xCount; i++) {
        int index = x_res[i].index;
        x_final[i] = x_vals[index];
    }
    for (int i = 0; i < yCount; i++) {
        int index = y_res[i].index;
        y_final[i] = y_vals[index];
    }
    
    // Sort the final candidate positions.
    qsort(x_final, xCount, sizeof(int), cmp_int);
    qsort(y_final, yCount, sizeof(int), cmp_int);
    
    int result = INT_MAX;
    // Evaluate each pair of candidate fence positions.
    for (int i = 1; i < xCount; i++) {
        double xMid = ((double)x_final[i] - x_final[i - 1]) / 2.0 + x_final[i - 1];
        for (int j = 1; j < yCount; j++) {
            double yMid = ((double)y_final[j] - y_final[j - 1]) / 2.0 + y_final[j - 1];
            int cur = count_points(xMid, yMid, cows, N);
            if (cur < result)
                result = cur;
        }
    }
    
    // Free allocated memory.
    free(x_vals);
    free(y_vals);
    free(x_res);
    free(y_res);
    free(x_final);
    free(y_final);
    
    return result;
}

int main(void) {
    FILE *fin = fopen("balancing.in", "r");
    if (!fin) {
        fprintf(stderr, "Error opening input file.\n");
        return 1;
    }
    FILE *fout = fopen("balancing.out", "w");
    if (!fout) {
        fprintf(stderr, "Error opening output file.\n");
        fclose(fin);
        return 1;
    }
    
    int N;
    fscanf(fin, "%d", &N);
    Cow *cows = malloc(N * sizeof(Cow));
    for (int i = 0; i < N; i++) {
        fscanf(fin, "%d %d", &cows[i].x, &cows[i].y);
    }
    fclose(fin);
    
    int result = solve(N, cows);
    fprintf(fout, "%d\n", result);
    fclose(fout);
    
    free(cows);
    return 0;
}
