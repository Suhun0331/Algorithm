/////////////////////////////////////////////////////////////////////////////////////////////
// 기본 제공코드는 임의 수정해도 관계 없습니다. 단, 입출력 포맷 주의
// 아래 표준 입출력 예제 필요시 참고하세요.
// 표준 입력 예제
// int a;
// double b;
// char g;
// String var;
// long AB;
// a = sc.nextInt();                           // int 변수 1개 입력받는 예제 
// b = sc.nextDouble();                        // double 변수 1개 입력받는 예제
// g = sc.nextByte();                          // char 변수 1개 입력받는 예제
// var = sc.next();                            // 문자열 1개 입력받는 예제
// AB = sc.nextLong();                         // long 변수 1개 입력받는 예제
/////////////////////////////////////////////////////////////////////////////////////////////
// 표준 출력 예제
// int a = 0;                            
// double b = 1.0;               
// char g = 'b';
// String var = "ABCDEFG";
// long AB = 12345678901234567L;
//System.out.println(a);                       // int 변수 1개 출력하는 예제
//System.out.println(b); 		       						 // double 변수 1개 출력하는 예제
//System.out.println(g);		       						 // char 변수 1개 출력하는 예제
//System.out.println(var);		       				   // 문자열 1개 출력하는 예제
//System.out.println(AB);		       				     // long 변수 1개 출력하는 예제
/////////////////////////////////////////////////////////////////////////////////////////////
import java.util.*;
import java.io.*;

/*
   사용하는 클래스명이 Solution 이어야 하므로, 가급적 Solution.java 를 사용할 것을 권장합니다.
   이러한 상황에서도 동일하게 java Solution 명령으로 프로그램을 수행해볼 수 있습니다.
 */
class Solution
{
	public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int T = Integer.parseInt(br.readLine());

        for (int test_case = 1; test_case <= T; test_case++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int h = Integer.parseInt(st.nextToken());
            int w = Integer.parseInt(st.nextToken());

            char[][] field = new char[h][w];
            int[] tank = new int[3]; // x, y, 방향 (0:상, 1:하, 2:좌, 3:우)

            // 맵 입력 및 탱크 위치 확인
            for (int i = 0; i < h; i++) {
                String row = br.readLine();
                for (int j = 0; j < w; j++) {
                    field[i][j] = row.charAt(j);
                    if (field[i][j] == '^') {
                        tank[0] = i; tank[1] = j; tank[2] = 0;
                    } else if (field[i][j] == 'v') {
                        tank[0] = i; tank[1] = j; tank[2] = 1;
                    } else if (field[i][j] == '<') {
                        tank[0] = i; tank[1] = j; tank[2] = 2;
                    } else if (field[i][j] == '>') {
                        tank[0] = i; tank[1] = j; tank[2] = 3;
                    }
                }
            }

            int n = Integer.parseInt(br.readLine());
            String order = br.readLine();

            for (int k = 0; k < n; k++) {
                char cmd = order.charAt(k);

                if (cmd == 'U') {
                    tank[2] = 0;
                    field[tank[0]][tank[1]] = '^';
                    if (tank[0] - 1 >= 0 && field[tank[0] - 1][tank[1]] == '.') {
                        field[tank[0]][tank[1]] = '.';
                        tank[0]--;
                        field[tank[0]][tank[1]] = '^';
                    }
                } else if (cmd == 'D') {
                    tank[2] = 1;
                    field[tank[0]][tank[1]] = 'v';
                    if (tank[0] + 1 < h && field[tank[0] + 1][tank[1]] == '.') {
                        field[tank[0]][tank[1]] = '.';
                        tank[0]++;
                        field[tank[0]][tank[1]] = 'v';
                    }
                } else if (cmd == 'L') {
                    tank[2] = 2;
                    field[tank[0]][tank[1]] = '<';
                    if (tank[1] - 1 >= 0 && field[tank[0]][tank[1] - 1] == '.') {
                        field[tank[0]][tank[1]] = '.';
                        tank[1]--;
                        field[tank[0]][tank[1]] = '<';
                    }
                } else if (cmd == 'R') {
                    tank[2] = 3;
                    field[tank[0]][tank[1]] = '>';
                    if (tank[1] + 1 < w && field[tank[0]][tank[1] + 1] == '.') {
                        field[tank[0]][tank[1]] = '.';
                        tank[1]++;
                        field[tank[0]][tank[1]] = '>';
                    }
                } else if (cmd == 'S') {
                    if (tank[2] == 0) { // 상
                        for (int x = tank[0] - 1; x >= 0; x--) {
                            if (field[x][tank[1]] == '*') {
                                field[x][tank[1]] = '.';
                                break;
                            } else if (field[x][tank[1]] == '#') break;
                        }
                    } else if (tank[2] == 1) { // 하
                        for (int x = tank[0] + 1; x < h; x++) {
                            if (field[x][tank[1]] == '*') {
                                field[x][tank[1]] = '.';
                                break;
                            } else if (field[x][tank[1]] == '#') break;
                        }
                    } else if (tank[2] == 2) { // 좌
                        for (int y = tank[1] - 1; y >= 0; y--) {
                            if (field[tank[0]][y] == '*') {
                                field[tank[0]][y] = '.';
                                break;
                            } else if (field[tank[0]][y] == '#') break;
                        }
                    } else if (tank[2] == 3) { // 우
                        for (int y = tank[1] + 1; y < w; y++) {
                            if (field[tank[0]][y] == '*') {
                                field[tank[0]][y] = '.';
                                break;
                            } else if (field[tank[0]][y] == '#') break;
                        }
                    }
                }
            }

            sb.append("#").append(test_case).append(" ");
            for (int i = 0; i < h; i++) {
                for (int j = 0; j < w; j++) {
                    sb.append(field[i][j]);
                }
                sb.append("\n");
            }
        }

        System.out.print(sb);
    }
}