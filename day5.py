import csv

# prep data
all_rows = []
with open('input5.txt') as f:
    reader = csv.reader(f, delimiter='\n')
    for row in reader:
        if row:
            all_rows.append(row[0].split())

coords = []

for row in all_rows:
    coord1 = row[0].split(',')
    coord2 = row[2].split(',')
    coord1 = [int(coord1[0]), int(coord1[1])]
    coord2 = [int(coord2[0]), int(coord2[1])]
    coords.append([coord1, coord2])

# create list of only horizontal/vertical lines
orth_coords = []
for coord_pair in coords:
    if coord_pair[0][0] == coord_pair[1][0] or coord_pair[0][1] == coord_pair[1][1]:
        orth_coords.append(coord_pair)

# calculate lines
overlap = {}
for coord_pair in coords:
    x1 = coord_pair[0][0]
    y1 = coord_pair[0][1]
    x2 = coord_pair[1][0]
    y2 = coord_pair[1][1]
    # orthogonal lines
    if x1 == x2 or y1 == y2:
        if x1 == x2:
            min, max = (y1, y2) if y1 < y2 else (y2, y1)
            x_same = True
        else:
            min, max = (x1, x2) if x1 < x2 else (x2, x1)
            x_same = False
        for i in range(min, max + 1):
            if x_same:
                if (x1, i) in overlap:
                    overlap[(x1, i)] += 1
                else:
                    overlap[(x1, i)] = 1
            else:
                if (i, y1) in overlap:
                    overlap[(i, y1)] += 1
                else:
                    overlap[(i, y1)] = 1
    # diagonal lines
    else:
        distance = abs(x1 - x2)
        for i in range(distance + 1):
            if x1 < x2 and y1 < y2:
                to_add = (x1 + i, y1 + i)
            elif x1 > x2 and y1 < y2:
                to_add = (x2 + i, y2 - i)
            elif x1 > x2 and y1 > y2:
                to_add = (x2 + i, y2 + i)
            else:
                to_add = (x1 + i, y1 - i)
            if to_add in overlap:
                overlap[to_add] += 1
            else:
                overlap[to_add] = 1


# count number of points with > 1 crossing lines
count = 0
for key in overlap:
    if overlap[key] > 1:
        count += 1

print(count)
