import math
from display import *


  # IMPORANT NOTE

  # Ambient light is represeneted by a color value

  # Point light sources are 2D arrays of doubles.
  #      - The fist index (LOCATION) represents the vector to the light.
  #      - The second index (COLOR) represents the color.

  # Reflection constants (ka, kd, ks) are represened as arrays of
  # doubles (red, green, blue)

AMBIENT = 0
DIFFUSE = 1
SPECULAR = 2
LOCATION = 0
COLOR = 1
SPECULAR_EXP = 4

#lighting functions
def get_lighting(normal, view, ambient, light, areflect, dreflect, sreflect ):
    normalize(view)
    normalize(normal)
    normalize(light[LOCATION])
    iambient = calculate_ambient(ambient, areflect)
    idiffuse = calculate_diffuse(light, dreflect, normal)
    ispecular = calculate_specular(light, sreflect, view, normal)
    
    rgb=[0, 0, 0]
    for i in range(3):
        rgb [i]=int (iambient[i]+idiffuse[i]+ispecular[i])
    return limit_color(rgb)

def calculate_ambient(alight, areflect):
    ambi=[0,0,0]
    for i in range(3):
         ambi[i] = alight[i]* areflect[i]
    return ambi

def calculate_diffuse(light, dreflect, normal):
    NL = dot_product(normal,light[LOCATION])
    diff = [0,0,0]
    for i in range(3):
         diff[i] = light[COLOR][i] * dreflect[i] * NL
    return diff
    
def calculate_specular(light, sreflect, view, normal):
    NL = dot_product(normal,light[LOCATION])
    r=[0,0,0]
    for i in range(3):
        r[i]=2*normal[i]*(NL) - light[LOCATION][i]
    cos_alpha =  dot_product(r,view) ** SPECULAR_EXP
    spec =[0,0,0]
    for i in range(3):
        spec[i] =  light[COLOR][i] * sreflect[i] * (cos_alpha)
    return spec

def limit_color(color):
    for i in color:
        if i>255:
            i=255
        elif i<0:
            i=0
    return color
        

#vector functions
#normalize vetor, should modify the parameter
def normalize(vector):
    magnitude = math.sqrt( vector[0] * vector[0] +
                           vector[1] * vector[1] +
                           vector[2] * vector[2])
    for i in range(3):
        vector[i] = vector[i] / magnitude

#Return the dot porduct of a . b
def dot_product(a, b):
    return a[0] * b[0] + a[1] * b[1] + a[2] * b[2]

#Calculate the surface normal for the triangle whose first
#point is located at index i in polygons
def calculate_normal(polygons, i):

    A = [0, 0, 0]
    B = [0, 0, 0]
    N = [0, 0, 0]

    A[0] = polygons[i+1][0] - polygons[i][0]
    A[1] = polygons[i+1][1] - polygons[i][1]
    A[2] = polygons[i+1][2] - polygons[i][2]

    B[0] = polygons[i+2][0] - polygons[i][0]
    B[1] = polygons[i+2][1] - polygons[i][1]
    B[2] = polygons[i+2][2] - polygons[i][2]

    N[0] = A[1] * B[2] - A[2] * B[1]
    N[1] = A[2] * B[0] - A[0] * B[2]
    N[2] = A[0] * B[1] - A[1] * B[0]

    return N
