#include <stdio.h>
#include <stack>
using namespace std;

int main() {
    stack<int> s;
    int K;
    int num;
    int stack_size;
    int sum = 0;

    scanf("%d", &K); // scanf를 사용하여 입력받을 정수의 개수를 입력 받음

    for (int i = 0; i < K; i++) {
        scanf("%d", &num); // 숫자를 scanf를 이용하여 입력 받음
        if (num == 0) { // 0이면 
            s.pop(); // top(0 이전)에 있는 숫자를 pop
        } else {
            s.push(num); // 0이 아니면 stack에 push
        }
    }

    stack_size = s.size(); // 스택의 크기를 얻어옴
    for (int i = 0; i < stack_size; i++) {
        sum += s.top(); // top에 있는 숫자를 하나씩 꺼내가며 더하기
        s.pop(); // 꺼낸 후 pop
    }

    printf("%d", sum); // 결과를 printf를 이용하여 출력

    return 0;
}
