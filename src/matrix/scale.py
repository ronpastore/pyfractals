from config import MATRIX_SIZE

def scale( n, radius, zoom_modifier):
    n = float(n)
    if radius == "X":
        lowest =  (-2.5 * zoom_modifier) - zoom_modifier 
        highest =(1.0 * zoom_modifier ) - zoom_modifier
            
    elif radius == "Y":
        lowest = (-1.5 * zoom_modifier ) - zoom_modifier
        highest =( 1.5 * zoom_modifier) - zoom_modifier

    return n * (highest - lowest) / (MATRIX_SIZE - 1)  + lowest

"""
def scale2(n, radius, zoom_modifier):
    cx= 175.0
    cy = 262.0
    
    if radius == "X":
        lowest =  (-2.5 * zoom_modifier) - zoom_modifier 
        highest =(1.0 * zoom_modifier ) - zoom_modifier
        
        return cx + (n/MATRIX_SIZE - 0.5)*(1.0 - (-2.5) )
    if radius == "Y":
        lowest = (-1.5 * zoom_modifier ) - zoom_modifier
        highest =( 1.5 * zoom_modifier) - zoom_modifier
        
        return cy + (n/MATRIX_SIZE - 0.5)*(1.5-(-1.5) )     
"""    