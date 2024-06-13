#include <stdio.h>
#include <string.h>

#define N 10000
int q[N];
int start = 0, end = 0, count = 0;

void push(int a) {
    if (count < N) { // 배열이 가득 찼는지 확인
        q[end] = a;
        end = (end + 1) % N; // end를 순환시키기
        ++count;
    }
}
void pop() {
    if (count != 0) {
        printf("%d\n", q[start]);
        start = (start + 1) % N; // start를 순환시키기
        --count;
    }
    else
        printf("-1\n");
}
void size() {
    printf("%d\n", count);
}
void empty() {
    printf("%d\n", count == 0 ? 1 : 0);
}
void front() {
    if (count != 0)
        printf("%d\n", q[start]);
    else
        printf("-1\n");
}
void back() {
    if (count != 0)
        printf("%d\n", q[(end - 1 + N) % N]); // end가 0이면 N-1이 되도록
    else
        printf("-1\n");
}

int main() {
    int n, in;
    char a[6];
    scanf("%d", &n);
    for (int i = 0; i < n; ++i) {
        scanf("%s", a);
        
        if (!strcmp(a, "push")) {
            scanf("%d", &in);
            push(in);
        }
        else if (!strcmp(a, "pop"))
            pop();
        else if (!strcmp(a, "size"))
            size();
        else if (!strcmp(a, "empty"))
            empty();
        else if (!strcmp(a, "front"))
            front();
        else if (!strcmp(a, "back"))
            back();
    }
    return 0;
}
