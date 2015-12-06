# Conway's Game of Life
#
# Date:     2015-12-06
# Version:  0.0.1
#
# 初期変数
message1 = "Select the initial cell before push START."
message2 = "Running..."
message3 = "All cells are dead. "
button1 = "START"
button2 = "END"
button3 = "RETRY"
status = "pre"
cellX = 0
cellY = 0
cellLive = []
cellLiveN = []
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
    # ステータス値の設定
    global status, cellX, cellY, cellLive
    print len(cellLive)
    if mouseY > width + 1:
        if mouseX > width / 2:
            if status == "initialized":
                status = "running"
            elif status == "running":
                cellLive = []
                status = "finished"
            elif status == "finished":
                status = "pre"
    # セルの初期値インプット
    elif status == "pre" or status == "initialized":
        cellX = int(mouseX // 25)
        cellY = int(mouseY // 25)
        if [cellX, cellY] in cellLive:
            cellLive.remove([cellX, cellY])
        else:
            cellLive.append([cellX, cellY])

def draw():
    global status, cellLive, message1, message2, message3, button1, button2, button3, liveNext
    background(20)
    print status
    # 格子を引く
    for i in range(0, width + 1, 25):
        line(i, 0, i, width + 1)
    for j in range(0, width + 1, 25):
        line(0, j, width + 1, j)
    line(width / 2, width, width / 2, height)
    # ステータスを表示
    if status == "pre" and len(cellLive) > 0:
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
        if len(cellLive) == 0:
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
    global cellLive, cellSize
    print cellLive
    for cell in cellLive:
        rect(cell[0] * 25, cell[1] * 25, cellSize, cellSize)

def liveordead():
    # 死活判定
    ## 生存セルとその近傍セルをリストアップ
    global cellLive, liveNext
    neighbor = []
    for cell in cellLive:
        if cell[0] > 0:
            if cell[0] != int(width // 25 - 1):
                if cell[1] > 0:
                    if cell[1] != int(width // 25 - 1):
                        neighbor.append([cell[0] - 1, cell[1] - 1])
                        neighbor.append([cell[0] - 1, cell[1]])
                        neighbor.append([cell[0] - 1, cell[1] + 1])
                        neighbor.append([cell[0], cell[1] - 1])
                        neighbor.append([cell[0], cell[1]])
                        neighbor.append([cell[0], cell[1] + 1])
                        neighbor.append([cell[0] + 1, cell[1] - 1])
                        neighbor.append([cell[0] + 1, cell[1]])
                        neighbor.append([cell[0] + 1, cell[1] + 1])
                        continue
                    neighbor.append([cell[0] - 1, cell[1] - 1])
                    neighbor.append([cell[0] - 1, cell[1]])
                    neighbor.append([cell[0], cell[1] - 1])
                    neighbor.append([cell[0], cell[1]])
                    neighbor.append([cell[0] + 1, cell[1] - 1])
                    neighbor.append([cell[0] + 1, cell[1]])
                    continue
                neighbor.append([cell[0] - 1, cell[1]])
                neighbor.append([cell[0] - 1, cell[1] + 1])
                neighbor.append([cell[0] + 1, cell[1]])
                neighbor.append([cell[0] + 1, cell[1] + 1])
                neighbor.append([cell[0], cell[1]])
                neighbor.append([cell[0], cell[1] + 1])
                continue
            if cell[1] > 0:
                if cell[1] != int(width // 25 - 1):
                    neighbor.append([cell[0] - 1, cell[1] - 1])
                    neighbor.append([cell[0] - 1, cell[1]])
                    neighbor.append([cell[0] - 1, cell[1] + 1])
                    neighbor.append([cell[0], cell[1] - 1])
                    neighbor.append([cell[0], cell[1]])
                    neighbor.append([cell[0], cell[1] + 1])
                    continue
                neighbor.append([cell[0] - 1, cell[1]])
                neighbor.append([cell[0] - 1, cell[1] - 1])
                neighbor.append([cell[0], cell[1] - 1])
                neighbor.append([cell[0], cell[1]])
                continue
            neighbor.append([cell[0] - 1, cell[1]])
            neighbor.append([cell[0] - 1, cell[1] + 1])
            neighbor.append([cell[0], cell[1]])
            neighbor.append([cell[0], cell[1] + 1])
            continue
        if cell[1] > 0:
            if cell[1] != int(width // 25 - 1):
                neighbor.append([cell[0], cell[1] - 1])
                neighbor.append([cell[0], cell[1]])
                neighbor.append([cell[0], cell[1] + 1])
                neighbor.append([cell[0] + 1, cell[1] - 1])
                neighbor.append([cell[0] + 1, cell[1]])
                neighbor.append([cell[0] + 1, cell[1] + 1])
                continue
            neighbor.append([cell[0], cell[1] - 1])
            neighbor.append([cell[0], cell[1]])
            neighbor.append([cell[0] + 1, cell[1] - 1])
            neighbor.append([cell[0] + 1, cell[1]])
            continue
        neighbor.append([cell[0], cell[1]])
        neighbor.append([cell[0], cell[1] + 1])
        neighbor.append([cell[0] + 1, cell[1]])
        neighbor.append([cell[0] + 1, cell[1] + 1])
    tmp1 = []
    neighborU = []
    for a in neighbor:
        tmp1.append(cellID(a[0], a[1]))
    tmp1U = set(tmp1)
    for b in tmp1U:
        neighborU.append(resolvID(b))
    ## 生存セル及びその近傍セルの死活を判定
    cellLiveN = []
    for dcell in neighborU:
        ldlist = []
        if dcell[0] > 0:
            if dcell[0] != int(width // 25 - 1):
                if dcell[1] > 0:
                    if dcell[1] != int(width // 25 - 1):
                        ldlist.append([dcell[0] - 1, dcell[1] - 1])
                        ldlist.append([dcell[0] - 1, dcell[1]])
                        ldlist.append([dcell[0] - 1, dcell[1] + 1])
                        ldlist.append([dcell[0], dcell[1] - 1])
                        ldlist.append([dcell[0], dcell[1]])
                        ldlist.append([dcell[0], dcell[1] + 1])
                        ldlist.append([dcell[0] + 1, dcell[1] - 1])
                        ldlist.append([dcell[0] + 1, dcell[1]])
                        ldlist.append([dcell[0] + 1, dcell[1] + 1])
                    else:
                        ldlist.append([dcell[0] - 1, dcell[1] - 1])
                        ldlist.append([dcell[0] - 1, dcell[1]])
                        ldlist.append([dcell[0], dcell[1] - 1])
                        ldlist.append([dcell[0], dcell[1]])
                        ldlist.append([dcell[0] + 1, dcell[1] - 1])
                        ldlist.append([dcell[0] + 1, dcell[1]])
                else:
                    ldlist.append([dcell[0] - 1, dcell[1]])
                    ldlist.append([dcell[0] - 1, dcell[1] + 1])
                    ldlist.append([dcell[0] + 1, dcell[1]])
                    ldlist.append([dcell[0] + 1, dcell[1] + 1])
                    ldlist.append([dcell[0], dcell[1]])
                    ldlist.append([dcell[0], dcell[1] + 1])
            elif dcell[1] > 0:
                if dcell[1] != int(width // 25 - 1):
                    ldlist.append([dcell[0] - 1, dcell[1] - 1])
                    ldlist.append([dcell[0] - 1, dcell[1]])
                    ldlist.append([dcell[0] - 1, dcell[1] + 1])
                    ldlist.append([dcell[0], dcell[1] - 1])
                    ldlist.append([dcell[0], dcell[1]])
                    ldlist.append([dcell[0], dcell[1] + 1])
                else:
                    ldlist.append([dcell[0] - 1, dcell[1]])
                    ldlist.append([dcell[0] - 1, dcell[1] - 1])
                    ldlist.append([dcell[0], dcell[1] - 1])
                    ldlist.append([dcell[0], dcell[1]])
            else:
                ldlist.append([dcell[0] - 1, dcell[1]])
                ldlist.append([dcell[0] - 1, dcell[1] + 1])
                ldlist.append([dcell[0], dcell[1]])
                ldlist.append([dcell[0], dcell[1] + 1])
        elif dcell[1] > 0:
            if dcell[1] != int(width // 25 - 1):
                ldlist.append([dcell[0], dcell[1] - 1])
                ldlist.append([dcell[0], dcell[1]])
                ldlist.append([dcell[0], dcell[1] + 1])
                ldlist.append([dcell[0] + 1, dcell[1] - 1])
                ldlist.append([dcell[0] + 1, dcell[1]])
                ldlist.append([dcell[0] + 1, dcell[1] + 1])
            else:
                ldlist.append([dcell[0], dcell[1] - 1])
                ldlist.append([dcell[0], dcell[1]])
                ldlist.append([dcell[0] + 1, dcell[1] - 1])
                ldlist.append([dcell[0] + 1, dcell[1]])
        else:
            ldlist.append([dcell[0], dcell[1]])
            ldlist.append([dcell[0], dcell[1] + 1])
            ldlist.append([dcell[0] + 1, dcell[1]])
            ldlist.append([dcell[0] + 1, dcell[1] + 1])
        match = 0
        for p in ldlist:
            if cellLive.count(p) == 1:
                match += 1
        if dcell in cellLive:
            if match == 3 or match == 4:
                cellLiveN.append(dcell)
        else:
            if match == 3:
                cellLiveN.append(dcell)
    cellLive = cellLiveN

def cellID(cX, cY):
    cid = str(cX) + "-" + str(cY)
    return cid

def resolvID(cellID):
    tmp = cellID.split("-")
    rlist = [int(tmp[0]), int(tmp[1])]
    return rlist
