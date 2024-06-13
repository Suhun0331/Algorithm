#include <stdio.h>
#include <string>
#include <stack>
using namespace std;

int main(void) {
    int k;
    scanf("%d", &k);

    while (k > 0) {
        k--;
        char input[101]; // 충분히 큰 크기로 배열 선언
        scanf("%s", input); // C 스타일 문자열 입력

        stack<char> st;
        string answer = "YES";
        for (int i = 0; input[i] != '\0'; i++) {
            if (input[i] == '(') {
                st.push(input[i]);
            }
            else if (!st.empty() && input[i] == ')' && st.top() == '(') {
                st.pop();
            }
            else {
                answer = "NO";
                break;
            }
        }
        if (!st.empty()) answer = "NO";

        printf("%s\n", answer.c_str()); // C++ string을 C 스타일 문자열로 변환하여 출력
    }
    return 0;
}