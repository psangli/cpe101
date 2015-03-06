#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Psangli
#
# Created:     14/02/2015
# Copyright:   (c) Psangli 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import collisions
import vector_math
from data import *
def main():
    pass
def cast_ray(ray,sphere_list,color,light,point):
    list = collisions.find_intersection_points(sphere_list,ray)

    if list != []:
        minDistance = vector_math.length_vector(vector_math.difference_vector(list[0][1],ray.pt))
        sphere = list[0][0];
        minIndex = 0
        for i in range (len(list)):
            if (vector_math.length_vector(vector_math.difference_vector(list[i][1],ray.pt)) < minDistance):
                minIndex = i
                minDistance = vector_math.length_vector(vector_math.difference_vector(list[i][1],ray.pt))
                sphere = list[i][0]
        normal = collisions.sphere_normal_at_point(list[minIndex][0],list[minIndex][1])
        scalar = vector_math.scale_vector(normal,.01)
        pe = vector_math.translate_point(list[minIndex][1],scalar)
        lDir = vector_math.normalize_vector(vector_math.vector_from_to(pe,light.pt))
        dot = vector_math.dot_vector(normal,lDir)
        reflectionVector = vector_math.difference_vector(lDir, vector_math.scale_vector(normal,(2 * dot)))
        vDir = vector_math.normalize_vector(vector_math.vector_from_to(point,pe))
        specular = vector_math.dot_vector(reflectionVector,vDir)

        r = 0
        g = 0
        b = 0

        if( dot > 0 ):
            peRay = vector_math.Ray(pe,lDir)
            obscure = collisions.find_intersection_points(sphere_list,peRay)
            if (obscure == []):
                r = r + dot*light.color.r*sphere.color.r*color.r*sphere.finish.diffuse
                g = g + dot*light.color.g*sphere.color.g*color.g*sphere.finish.diffuse
                b = b + dot*light.color.b*sphere.color.b*color.b*sphere.finish.diffuse

                if(specular > 0):
                    r = r + light.color.r*sphere.finish.specular*(specular**(1.0/sphere.finish.roughness))
                    g = g + light.color.g*sphere.finish.specular*(specular**(1.0/sphere.finish.roughness))
                    b = b + light.color.b*sphere.finish.specular*(specular**(1.0/sphere.finish.roughness))

        r = r + sphere.color.r*color.r*sphere.finish.ambient
        g = g + sphere.color.g*color.g*sphere.finish.ambient
        b = b + sphere.color.b*color.b*sphere.finish.ambient

        if (r>1):
            r = 1
        if (g>1):
            g = 1
        if (b>1):
            b = 1

        return Color(r,g,b)
    else:
        return Color(1, 1, 1)



def cast_all_rays(min_x, max_x, min_y, max_y, width, height, eye_point, sphere_list,color,light):
    differenceInx = (max_x - min_x)/float (width)
    differenceIny = (max_y - min_y)/float (height)
    for h in range(height):
        for w in range(width):
            x = min_x+differenceInx*w
            y = max_y-differenceIny*h
            z = 0
            ray = vector_math.Ray(eye_point,vector_math.difference_point(vector_math.Point(x,y,z),eye_point))
            ##cast_ray(ray,sphere_list)

            colorOut = cast_ray(ray,sphere_list,color,light,eye_point)
            print (str(int(colorOut.r*255)) + " " + str(int(colorOut.g*255)) + " " + str(int(colorOut.b*255)))







if __name__ == '__main__':
    main()
