import sfml as sf

def open_file(file):
    f = open(file, 'r')
    lines = f.readlines()
    result = []
    for line in lines:
        tb = line.split( )
        result.append(tb)
    return(result)

def iso(result, hight, lenght, img):
    y = 0
    tab2 = []
    cte1 = 0.7
    cte2 = 0.7
    for a in result:
        y = y + 1 * int(lenght / len(result)) * 0.7
        x = 0
        for z in a:
            x = x + 1 * int (hight / len(a)) * 0.7
            x_iso = int(cte1 * int(x) - cte2 * int(y) + int(hight / 2))
            y_iso = int(-int(z) + (cte1 / 2) * int(x) + (cte2 / 2) * int(y))
            tab2.append([x_iso, y_iso])
            if (int(z) <= 0):
                img[x_iso, y_iso] = sf.Color.WHITE
            elif (int(z) > 0):
                img[x_iso, y_iso] = sf.Color.RED
    for x in range(0, len(tab2) - 1):
        v1 = sf.Vector2(tab2[x][0], tab2[x][1])
        v2 = sf.Vector2(tab2[x + 1][0], tab2[x + 1][1])
        draw_lines(v1, v2, img)
    for y in range (0, len(tab2) - len(result)):
        v1 = sf.Vector2(tab2[y][0], tab2[y][1])
        v2 = sf.Vector2(tab2[y + len(result)][0], tab2[y + len(result)][1])
        draw_lines(v2, v1, img)
    return (tab2)

def draw_lines(v1, v2, img):
    x1 = v1.x
    y1 = v1.y
    x2 = v2.x
    y2 = v2.y
    x = x1
    while x2 > x:
        y = y1+((y2-y1)*(x-x1)/(x2-x1))
        img[x, y] = sf.Color.WHITE
        x = x + 1

def main():
    window = sf.RenderWindow(sf.VideoMode(900, 900), "FDF")
    window.framerate_limit = 60
    img = sf.Image.create(800, 800, sf.Color.TRANSPARENT)
    result = open_file("elem2.fdf")
    iso(result, 800, 800, img)
    tex = sf.Texture.from_image(img)
    spr = sf.Sprite(tex)
    while window.is_open:
        for event in window.events:
            if sf.Keyboard.is_key_pressed(sf.Keyboard.ESCAPE):
                window.close()
            if type(event) is sf.CloseEvent:
                window.close()
        window.clear(sf.Color.BLACK)
        window.draw(spr)
        window.display()
main()