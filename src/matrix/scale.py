from config import MATRIX_SIZE

def scale( n, radius, zoom_modifier):
    n = float(n)
    if radius == "X":
        lowest =  -2.5 * zoom_modifier
        highest =1.0 * zoom_modifier
            
    elif radius == "Y":
        lowest = -1.5 * zoom_modifier
        highest = 1.5 * zoom_modifier

    return n * (highest - lowest) / (MATRIX_SIZE - 1)  + lowest
