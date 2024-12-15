import sys
import bisect

def main():
    import sys
    Q = int(input())


    def parse_query():
        query = input().split()
        if len(query) == 1:
            return (int(query[0]),)
        else:
            return (int(query[0]), int(query[1]))

    sorted_plants = []
    new_plants = []
    add =0
    output = []
    for _ in range(Q):
        q = parse_query()
        cmd = str(q[0])
        if cmd == '1':
            # Type 1: 新しい植物を追加
            plant_base = -add
            new_plants.append(plant_base)
            
        elif cmd == '2':
            # Type 2: 全ての植物の高さを T 増加
            T = int(q[1])
            add += T
            
        elif cmd == '3':
            # Type 3: 高さが H 以上の植物を収穫
            H = int(q[1])
            threshold = H - add
            # new_plants をソートして sorted_plants とマージ
            if new_plants:
                new_plants.sort()
                merged = []
                i = j =0
                n = len(sorted_plants)
                m = len(new_plants)
                while i < n and j < m:
                    if sorted_plants[i] < new_plants[j]:
                        merged.append(sorted_plants[i])
                        i +=1
                    else:
                        merged.append(new_plants[j])
                        j +=1
                while i < n:
                    merged.append(sorted_plants[i])
                    i +=1
                while j < m:
                    merged.append(new_plants[j])
                    j +=1
                sorted_plants = merged
                new_plants = []
            # 収穫対象の植物を特定
            pos = bisect.bisect_left(sorted_plants, threshold)
            harvested = len(sorted_plants) - pos
            output.append(str(harvested))
            # 収穫済みの植物をリストから削除
            sorted_plants = sorted_plants[:pos]
            
    # 結果を一括で出力
    print('\n'.join(output))

if __name__ == "__main__":
    main()