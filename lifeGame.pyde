# Conway's Game of Life
#
# Date:     2015-12-07
# Version:  0.0.2
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

def setup():
    # 初期設定
    global pushedColor, liveColor
    size(1000, 1100)
    background(20)
    pusshedColor = color(244)
    liveColor = color(220)
    stroke(70)
    fill(200)
    frameRate(8)
    background(20)

def mousePressed():
    # ステータス判定
    global status, cellX, cellY, liveP
    print len(liveP)
    if mouseY > width + 1:
        if mouseX > width / 2:
            if status == "initialized":
                status = "running"
            elif status == "running":
                liveP = []
                status = "finished"
            elif status == "finished":
                status = "pre"
    # セルの初期値インプット
    elif status == "pre" or status == "initialized":
        cellX = int(mouseX // 25)
        cellY = int(mouseY // 25)
        if [cellX, cellY] in liveP:
            liveP.remove([cellX, cellY])
        else:
            liveP.append([cellX, cellY])

def draw():
    global status, liveP, message1, message2, message3, button1, button2, button3, liveN
    background(20)
    print status
    # 格子を引く
    for i in range(0, width + 1, 25):
        line(i, 0, i, width + 1)
    for j in range(0, width + 1, 25):
        line(0, j, width + 1, j)
    line(width / 2, width, width / 2, height)
    # ステータスを表示
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

def printCell():
    # 生きてるセルを描画
    global liveP, cellSize
    print liveP
    for live in liveP:
        rect(live[0] * 25, live[1] * 25, cellSize, cellSize)

def liveordead():
    # 死活判定
    ## 生存セルとその近傍セルをリストアップ
    global liveP, liveN
    neighbor = []
    neighborU = []
    for cell1 in liveP:
        neighbor.append([cell1[0] - 1, cell1[1] - 1])
        neighbor.append([cell1[0] - 1, cell1[1]])
        neighbor.append([cell1[0] - 1, cell1[1] + 1])
        neighbor.append([cell1[0], cell1[1] - 1])
        neighbor.append([cell1[0], cell1[1]])
        neighbor.append([cell1[0], cell1[1] + 1])
        neighbor.append([cell1[0] + 1, cell1[1] - 1])
        neighbor.append([cell1[0] + 1, cell1[1]])
        neighbor.append([cell1[0] + 1, cell1[1] + 1])
    tmp1 = []
    tmp2 = []
    tmp3 = []
    for a in neighbor:
        tmp1.append(setID(a[0], a[1]))
    tmp2 = set(tmp1)
    for b in tmp2:
        tmp3.append(resolveID(b))
    for cell2 in tmp3:
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

def setID(cX, cY):
    cid = str(cX) + "_" + str(cY)
    return cid

def resolveID(cellID):
    tmp = cellID.split("_")
    rlist = [int(tmp[0]), int(tmp[1])]
    return rlist
