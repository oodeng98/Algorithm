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
        atoms[(x, y)] = (direction, energy)
        atoms_lst.append((x, y))

    distances = {}
    for i in range(N):
        for j in range(i+1, N):
            x1, y1 = atoms_lst[i]
            x2, y2 = atoms_lst[j]
            xdistance = abs(x1 - x2)
            ydistance = abs(y1 - y2)
            if xdistance == 0 or ydistance == 0 or xdistance == ydistance:
                distance = xdistance + ydistance
                if distance in distances:
                    distances[distance].append([(x1, y1), (x2, y2)])
                else:
                    distances[distance] = [[(x1, y1), (x2, y2)]]

    distances_lst = sorted(list(distances.keys()))
    for d in distances_lst:
        temp_lst = set()
        for at1, at2 in distances[d]:
            if at1 not in atoms or at2 not in atoms:
                continue
            x1, y1 = at1
            x2, y2 = at2
            d1 = atoms[at1][0]
            d2 = atoms[at2][0]
            if x1 == x2 and ((y1 < y2 and d1 == 0 and d2 == 1) or (y2 < y1 and d1 == 1 and d2 == 0)):
                temp_lst.add(at1)
                temp_lst.add(at2)
            if y1 == y2 and ((x1 < x2 and d1 == 3 and d2 == 2) or (x2 < x1 and d1 == 2 and d2 == 3)):
                temp_lst.add(at1)
                temp_lst.add(at2)

            if abs(x1 - x2) != abs(y1 - y2):
                continue

            if x1 < x2:
                if d1 == 3 and ((y1 < y2 and d2 == 1) or (y2 < y1 and d2 == 0)):
                    temp_lst.add(at1)
                    temp_lst.add(at2)
                elif d2 == 2 and ((y1 < y2 and d1 == 0) or (y2 < y1 and d1 == 1)):
                    temp_lst.add(at1)
                    temp_lst.add(at2)
            else:
                if d1 == 2 and ((y1 < y2 and d2 == 1) or (y2 < y1 and d2 == 0)):
                    temp_lst.add(at1)
                    temp_lst.add(at2)
                elif d2 == 3 and ((y1 < y2 and d1 == 0) or (y2 < y1 and d1 == 1)):
                    temp_lst.add(at1)
                    temp_lst.add(at2)
        for atom in temp_lst:
            total_energy += atoms[atom][1]
            del atoms[atom]
    print(f"#{t} {total_energy}")