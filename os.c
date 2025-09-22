#include <stdio.h>
#include <stdlib.h>

typedef struct fcfs {
    int process;     // process id
    int burst;       // burst time
    int arrival;     // arrival time
    int completion;  // completion time
    int tat;         // turn around time
    int wt;          // waiting time
} fcfs;

int sort_by_arrival(fcfs arr[], int n);

int main(void) {
    int n;
    printf("Enter the number of processes: ");
    if (scanf("%d", &n) != 1 || n <= 0) {
        printf("Invalid number of processes.\n");
        return 1;
    }

    fcfs arr[n];
    for (int i = 0; i < n; ++i) {
        arr[i].process = i + 1; // give human-friendly process id
        printf("\nEnter data for process %d\n", arr[i].process);
        printf("Enter CPU Burst: ");
        scanf("%d", &arr[i].burst);
        printf("Enter Arrival Time: ");
        scanf("%d", &arr[i].arrival);
    }

    // sort by arrival time (FCFS)
    sort_by_arrival(arr, n);

    int current_time = 0;
    int sum_tat = 0, sum_wt = 0;

    printf("\nProcess\tBurst\tArrival\tCompletion\tTAT\tWT\n");
    for (int i = 0; i < n; ++i) {
        // if CPU is idle until this process arrives, jump time to arrival
        if (current_time < arr[i].arrival) {
            current_time = arr[i].arrival;
        }

        arr[i].completion = current_time + arr[i].burst;
        current_time = arr[i].completion;

        arr[i].tat = arr[i].completion - arr[i].arrival;
        arr[i].wt  = arr[i].tat - arr[i].burst;

        sum_tat += arr[i].tat;
        sum_wt  += arr[i].wt;

        printf("%d\t%d\t%d\t%d\t\t%d\t%d\n",
               arr[i].process, arr[i].burst, arr[i].arrival,
               arr[i].completion, arr[i].tat, arr[i].wt);
    }

    printf("\nAverage Turn Around Time: %.2f\n", (float)sum_tat / n);
    printf("Average Waiting Time    : %.2f\n", (float)sum_wt  / n);

    return 0;
}

int sort_by_arrival(fcfs arr[], int n) {
    for (int i = 0; i < n - 1; ++i) {
        for (int j = i + 1; j < n; ++j) {
            if (arr[i].arrival > arr[j].arrival) {
                fcfs tmp = arr[i];
                arr[i] = arr[j];
                arr[j] = tmp;
            }
        }
    }
    return 0;
}