# Conway's Game of Life
#
# Date:     2015-12-08
# Version:  0.1.0
#
# 初期変数
message1 = "Select the initial cells before push START."
message2 = "Running..."
message3 = "All cells are dead. "
button1 = "START"
button2 = "END"
button3 = "RETRY"
status = "pre"
cellX = 0
cellY = 0
liveP = []
liveN = []
cellSize = 25

# 初期設定
def setup():
    size(1000, 1100)
    background(20)
    stroke(70)
    fill(200)
    frameRate(8)
    background(20)

# マウス操作
def mousePressed():
    ## ステータス入力
    global status, cellX, cellY, liveP
    if mouseY > width + 1:
        if mouseX > width / 2:
            if status == "initialized":
                status = "running"
            elif status == "running":
                liveP = []
                status = "finished"
            elif status == "finished":
                status = "pre"
    ## セル初期値入力
    elif status == "pre" or status == "initialized":
        cellX = int(mouseX // 25)
        cellY = int(mouseY // 25)
        if [cellX, cellY] in liveP:
            liveP.remove([cellX, cellY])
        else:
            liveP.append([cellX, cellY])

# メインのdraw
def draw():
    global status, liveP, liveN, message1, message2, message3, button1, button2, button3
    background(20)
    # 格子を引く
    for i in range(0, width + 1, 25):
        line(i, 0, i, width + 1)
    for j in range(0, width + 1, 25):
        line(0, j, width + 1, j)
    line(width / 2, width, width / 2, height)
    # ステータス分岐
    if status == "pre" and len(liveP) > 0:
        status = "initialized"
    if status == "pre" or status == "initialized":
        textSize(25)
        textAlign(LEFT)
        text(message1, 0, width, width / 2, height)
        if status == "initialized":
            textSize(50)
            textAlign(CENTER, CENTER)
            text(button1, (width / 4) * 3, (width + height) / 2)
            printCell()
    elif status == "running":
        if len(liveP) == 0:
            status = "finished"
        textSize(25)
        textAlign(LEFT)
        text(message2, 0, width, width / 2, height)
        textSize(50)
        textAlign(CENTER, CENTER)
        text(button2, (width / 4) * 3, (width + height) / 2)
        liveordead()
        printCell()
    elif status == "finished":
        textSize(25)
        textAlign(LEFT)
        text(message3, 0, width, width / 2, height)
        textSize(50)
        textAlign(CENTER, CENTER)
        text(button3, (width / 4) * 3, (width + height) / 2)

# 生きてるセルを描画
def printCell():
    global liveP, cellSize
    for cell in liveP:
        rect(cell[0] * 25, cell[1] * 25, cellSize, cellSize)

# 死活判定
def liveordead():
    ## 生存セルとその近傍セルをリストアップ
    global liveP, liveN
    neighbor = set()
    for cell1 in liveP:
        neighbor.add(setStr(cell1[0] - 1, cell1[1] - 1))
        neighbor.add(setStr(cell1[0] - 1, cell1[1]))
        neighbor.add(setStr(cell1[0] - 1, cell1[1] + 1))
        neighbor.add(setStr(cell1[0], cell1[1] - 1))
        neighbor.add(setStr(cell1[0], cell1[1]))
        neighbor.add(setStr(cell1[0], cell1[1] + 1))
        neighbor.add(setStr(cell1[0] + 1, cell1[1] - 1))
        neighbor.add(setStr(cell1[0] + 1, cell1[1]))
        neighbor.add(setStr(cell1[0] + 1, cell1[1] + 1))
    tmp1 = []
    for b in neighbor:
        tmp1.append(resolveStr(b))
    ## 枠外セルを除外
    neighborU = []
    for cell2 in tmp1:
        if cell2[0] >= 0 and cell2[0] < width // 25 and cell2[1] >= 0 and cell2[1] < width // 25:
            neighborU.append([cell2[0], cell2[1]])

    ## 生存セル及びその近傍セルの死活を判定
    liveN = []
    for cell3 in neighborU:
        cPoint = []
        cPoint.append([cell3[0] - 1, cell3[1] - 1])
        cPoint.append([cell3[0] - 1, cell3[1]])
        cPoint.append([cell3[0] - 1, cell3[1] + 1])
        cPoint.append([cell3[0], cell3[1] - 1])
        cPoint.append([cell3[0], cell3[1]])
        cPoint.append([cell3[0], cell3[1] + 1])
        cPoint.append([cell3[0] + 1, cell3[1] - 1])
        cPoint.append([cell3[0] + 1, cell3[1]])
        cPoint.append([cell3[0] + 1, cell3[1] + 1])
        match = 0
        for p in cPoint:
            if p in liveP:
                match += 1
        if cell3 in liveP:
            if match == 3 or match == 4:
                liveN.append(cell3)
        else:
            if match == 3:
                liveN.append(cell3)
    liveP = liveN

def setStr(cX, cY):
    cStr = str(cX) + "_" + str(cY)
    return cStr

def resolveStr(cStr):
    tmp = cStr.split("_")
    clist = [int(tmp[0]), int(tmp[1])]
    return clist
