# i日目（1 <=i<= N）の予定が S[i]（= 0, 1, 2） で与えられる。

# 初日：
    # 無地の T シャツ M 枚
    # ロゴ入りの T シャツ 0 枚←これが何枚必要かを推定するのがこの問題のメインポイント

# S[i] == 0:
    # 予定なし：使ったシャツを全て洗濯する。次の日からそのシャツは利用可能。この日はシャツを使わない。
# S[i] == 1:
    # 食事に出かける：無地の T シャツ 1 枚またはロゴ入りの T シャツ 1 枚が必要
# S[i] == 2:
    # 競プロする：ロゴ入りの T シャツ 1 枚が必要

# 一度着た T シャツは洗濯しないと着られない。    


# 問題：
    # スケジュールを遂行するために必要なロゴ入りの T シャツの最小枚数を求める
    # ただし、購入する必要がない場合は 0 を出力する。

N, M = map(int, input().split())
S = list(map(int, list(input())))

# print(S)

# 貪欲法でなんとかなる
# 1. 食事に出かけるときは、なるべく無地のシャツを使う。


# 無地のシャツの着用可能枚数：m
m = M
ans = 0 # 0 が出るたびに仕切り直し。最後に max を取る。
# 仕切り直しが入るまでの間、ロゴ入りのシャツの必要枚数を l とする。
l = 0

for i in range(N):
    if S[i] == 0:
        # 予定なし：使ったシャツを全て洗濯する。次の日からそのシャツは利用可能。この日はシャツを使わない。
        m = M
        ans = max(ans, l)
        l = 0


    elif S[i] == 1:
        # 食事に出かける：無地の T シャツ 1 枚またはロゴ入りの T シャツ 1 枚が必要
        if m > 0:
            m -= 1
        else:
            l += 1
    else:
        # 競プロする：ロゴ入りの T シャツ 1 枚が必要
        l += 1
    
ans = max(ans, l)

print(ans)
            
