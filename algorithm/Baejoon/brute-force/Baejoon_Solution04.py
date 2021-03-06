# 지민이는 자신의 저택에서 MN개의 단위 정사각형으로 나누어져 있는 M*N 크기의 보드를 찾았다. 어떤 정사각형은 검은색으로 칠해져 있고, 나머지는 흰색으로 칠해져 있다. 지민이는 이 보드를 잘라서 8*8 크기의 체스판으로 만들려고 한다.
# 체스판은 검은색과 흰색이 번갈아서 칠해져 있어야 한다. 구체적으로, 각 칸이 검은색과 흰색 중 하나로 색칠되어 있고, 변을 공유하는 두 개의 사각형은 다른 색으로 칠해져 있어야 한다. 따라서 이 정의를 따르면 체스판을 색칠하는 경우는 두 가지뿐이다. 하나는 맨 왼쪽 위 칸이 흰색인 경우, 하나는 검은색인 경우이다.
# 보드가 체스판처럼 칠해져 있다는 보장이 없어서, 지민이는 8*8 크기의 체스판으로 잘라낸 후에 몇 개의 정사각형을 다시 칠해야겠다고 생각했다. 당연히 8*8 크기는 아무데서나 골라도 된다. 지민이가 다시 칠해야 하는 정사각형의 최소 개수를 구하는 프로그램을 작성하시오.
import sys


def check_BW(matrix):
    case1_not_match = 0
    case2_not_match = 0

    # case 1 시작점(0,0)이 W 인경우
    for x in range(8):
        for y in range(8):
            if ((x % 2 == 0) and (y % 2 == 0)) or ((x % 2 == 1) and (y % 2 == 1)):  # 행짝 열짝, 행홀 열홀
                if matrix[x][y] != "W":
                    case1_not_match += 1

            elif ((x % 2 == 1) and (y % 2 == 0) or (x % 2 == 0) and (y % 2 == 1)):  # 행홀 열짝, 행짝 열홀
                if matrix[x][y] != "B":
                    case1_not_match += 1

    # case 2 시작점(0,0)이 B 인경우
    for x in range(8):
        for y in range(8):
            if ((x % 2 == 0) and (y % 2 == 0)) or ((x % 2 == 1) and (y % 2 == 1)):  # 행짝 열짝, 행홀 열홀
                if matrix[x][y] != "B":
                    case2_not_match += 1

            elif ((x % 2 == 1) and (y % 2 == 0) or (x % 2 == 0) and (y % 2 == 1)):  # 행홀 열짝, 행짝 열홀
                if matrix[x][y] != "W":
                    case2_not_match += 1

    return min(case1_not_match, case2_not_match)


def solution():
    input_list = []
    M, N = map(int, sys.stdin.readline().split())
    for idx in range(M):
        input_list.append([i for i in sys.stdin.readline()][:-1])
    min_revise_cnt = 123041234723842
    for row in range(M - 7):
        for col in range(N - 7):
            print(row,col)
            # 8*8 매트릭스로 자르기
            slice_mat = [one_row[col:col + 8] for one_row in input_list[row:row + 8]]
            revise_cnt = check_BW(slice_mat)
            min_revise_cnt = min(min_revise_cnt, revise_cnt)

    return min_revise_cnt


print(solution())

