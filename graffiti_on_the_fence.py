import sys
import math
from operator import itemgetter

debug = False

l = int(input())
n = int(input())

# Build reports
reports = []
for i in range(n):
    st, ed = [int(j) for j in input().split()]
    reports.append([st, ed])
    if debug:
        print(f"{st} {ed}")
        
reports = sorted(reports, key=itemgetter(0))
    
# Build painted fence sections
painted_fence = []
for report in reports:
    st = report[0]
    ed = report[1]
    append_painted_section = True
    for painted_section in painted_fence:
        if not (painted_section[0] <= st <= painted_section[1]):
            continue
        else:
            append_painted_section = False
            if ed > painted_section[1]:
                painted_section[1] = ed
        
    if append_painted_section:
        if debug:
            print(f"appended {st} {ed}")
        painted_fence.append([st, ed])
        
    
if debug:
    print("painted_fence", painted_fence)
    
# Iterate report to find unpainted sections
unpainted_sections = [[0,0]]
for painted_section in painted_fence:
    st_unpainted = unpainted_sections[-1][0]
    ed_unpainted = unpainted_sections[-1][1]
    st_painted = painted_section[0]
    ed_painted = painted_section[1]
    
    if st_unpainted >= st_painted:
        unpainted_sections[-1][0] = ed_painted
        continue
    
    if ed_unpainted < st_painted:
        unpainted_sections[-1][1] = st_painted
        unpainted_sections.append([ed_painted, 0])
    elif ed_unpainted < ed_painted:
        unpainted_sections[-1][1] = ed_painted
    
unpainted_sections[-1][1] = l
unpainted_sections = [section for section in unpainted_sections if section[0] != section[1]]

if debug:
    print("unpainted_sections", unpainted_sections)

# Output
if debug:
    print("first point", painted_fence[0][0])
    print("last point", painted_fence[-1][1])
    
    
if len(unpainted_sections) == 0:
    print("All painted")
else:
    for unpainted_section in unpainted_sections:
        st = unpainted_section[0]
        ed = unpainted_section[1]
        print(f"{st} {ed}")
