import sys

sys.stdin = open('input.txt')


T = int(input())
for t in range(1, T+1):
    N = int(input())
    atoms = {}
    atoms_lst = []
    total_energy = 0
    for _ in range(N):
        x, y, direction, energy = map(int, input().split())
        atoms[(x, y)] = [direction, energy]
        atoms_lst.append((x, y))

    distances = {}
    distances_lst = set()
    for i in range(N):
        for j in range(i+1, N):
            x1, y1 = atoms_lst[i]
            x2, y2 = atoms_lst[j]
            distance = abs(x1 - x2) + abs(y1 - y2)
            distances_lst.add(distance)
            if distance in distances:
                distances[distance].append([(x1, y1), (x2, y2)])
            else:
                distances[distance] = [[(x1, y1), (x2, y2)]]

    distances_lst = sorted(list(distances_lst))
    crush_lst = {}
    for d in distances_lst:  # 가까운 애들부터
        temp_crust_lst = set()
        for atom1, atom2 in distances[d]:
            if atom1 not in atoms or atom2 not in atoms:
                continue
            x1, y1 = atom1
            x2, y2 = atom2
            if x1 == x2:
                if y1 < y2 and atoms[atom1][0] == 0 and atoms[atom2][0] == 1:
                    temp_crust_lst.add(atom1)
                    temp_crust_lst.add(atom2)
                elif y2 < y1 and atoms[atom1][0] == 1 and atoms[atom2][0] == 0:
                    temp_crust_lst.add(atom1)
                    temp_crust_lst.add(atom2)
            if y1 == y2:
                if x1 < x2 and atoms[atom1][0] == 3 and atoms[atom2][0] == 2:
                    temp_crust_lst.add(atom1)
                    temp_crust_lst.add(atom2)
                elif x2 < x1 and atoms[atom1][0] == 2 and atoms[atom2][0] == 3:
                    temp_crust_lst.add(atom1)
                    temp_crust_lst.add(atom2)

            if abs(x1 - x2) != abs(y1 - y2):  # 이젠 같은 선분 위에 있지 않으므로 x와 y좌표간의 값의 차이가 동일해아함
                continue
            if x1 < x2:
                if atoms[atom1][0] == 3: # x1이 우측으로 가는 애이면
                    if y1 < y2 and atoms[atom2][0] == 1:
                        temp_crust_lst.add(atom1)
                        temp_crust_lst.add(atom2)
                    elif y2 < y1 and atoms[atom2][0] == 0:
                        temp_crust_lst.add(atom1)
                        temp_crust_lst.add(atom2)
                elif atoms[atom2][0] == 2:  # x2가 좌측으로 가는 애라면?
                    if y1 < y2 and atoms[atom1][0] == 0:
                        temp_crust_lst.add(atom1)
                        temp_crust_lst.add(atom2)
                    elif y2 < y1 and atoms[atom1][0] == 1:
                        temp_crust_lst.add(atom1)
                        temp_crust_lst.add(atom2)
            else:  # x2 < x1
                if atoms[atom1][0] == 2: # x1이 좌측으로 가는 애이면
                    if y1 < y2 and atoms[atom2][0] == 1:
                        temp_crust_lst.add(atom1)
                        temp_crust_lst.add(atom2)
                    elif y2 < y1 and atoms[atom2][0] == 0:
                        temp_crust_lst.add(atom1)
                        temp_crust_lst.add(atom2)
                elif atoms[atom2][0] == 3:  # x2가 우측으로 가는 애라면
                    if y1 < y2 and atoms[atom1][0] == 0:
                        temp_crust_lst.add(atom1)
                        temp_crust_lst.add(atom2)
                    elif y2 < y1 and atoms[atom1][0] == 1:
                        temp_crust_lst.add(atom1)
                        temp_crust_lst.add(atom2)
        for atom in temp_crust_lst:
            total_energy += atoms[atom][1]
            del atoms[atom]
    print(f"#{t} {total_energy}")