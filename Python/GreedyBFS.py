import heapq

def greedy_best_first_search(shahar_map, shuru, manzil, doori_hint):
    visited = set()               # Jahan pehle hi gaye ho
    line = []                     # Priority queue (sabse close guess pehle)
    heapq.heappush(line, (doori_hint[shuru], shuru))  
    
    while line:
        _, abhi = heapq.heappop(line)  # Sabse close lagta node nikal lo
        print(f"🚶 Ja rahe hain: {abhi}")

        if abhi == manzil:
            print("🎯 Manzil mil gayi! Party time! 🎉")
            return True

        if abhi not in visited:
            visited.add(abhi)
            for padosi in shahar_map[abhi]:
                if padosi not in visited:
                    print(f"🔍 {padosi} dikh raha hai... (Hint: {doori_hint[padosi]})")
                    heapq.heappush(line, (doori_hint[padosi], padosi))

    print("😕 Manzil nahi mili, lagta wrong hints thi.")
    return False


# 🏙 City Map (Graph)
shahar_map = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['I'],
    'D': [],
    'E': ['D'],
    'F': []
}

# 🔮 Door ka guess (Heuristic)
doori_hint = {
    'A': 5,
    'B': 4,
    'C': 3,
    'D': 7,
    'E': 2,
    'F': 0
}

# 🚀 Search Start
greedy_best_first_search(shahar_map, shuru='A', manzil='F', doori_hint=doori_hint)
