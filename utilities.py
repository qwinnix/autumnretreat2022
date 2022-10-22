################################################################################

import numpy

################################################################################

FACEMESH_LOWER_LIP_OUTER = frozenset( [
    (61, 146), (146, 91), (91, 181), (181, 84), (84, 17),
    (17, 314), (314, 405), (405, 321), (321, 375), (375, 291)
] )

FACEMESH_LOWER_LIP_INNER = frozenset( [
    (78, 95), (95, 88), (88, 178), (178, 87), (87, 14),
    (14, 317), (317, 402), (402, 318), (318, 324), (324, 308)
] )

FACEMESH_LOWER_LIP = frozenset( [
    (61, 146), (146, 91), (91, 181), (181, 84), (84, 17), (17, 314),
    (314, 405), (405, 321), (321, 375), (375, 291), (291, 308),
    (308, 324), (324, 318), (318, 402), (402, 317), (317, 14),
    (14, 87), (87, 178), (178, 88), (88, 95), (95, 78), (78, 61)
] )

FACEMESH_UPPER_LIP_INNER = frozenset( [
    (78, 191), (191, 80), (80, 81), (81, 82), (82, 13),
    (13, 312), (312, 311), (311, 310), (310, 415), (415, 308)
] )

FACEMESH_UPPER_LIP_OUTER = frozenset( [
    (61, 185), (185, 40), (40, 39), (39, 37), (37, 0),
    (0, 267), (267, 269), (269, 270), (270, 409), (409, 291)
] )

FACEMESH_UPPER_LIP = frozenset( [
    (78, 191), (191, 80), (80, 81), (81, 82), (82, 13), (13, 312),
    (312, 311), (311, 310), (310, 415), (415, 308), (308, 291),
    (291, 409), (409, 270), (270, 269), (269, 267), (267, 0),
    (0, 37), (37, 39), (39, 40), (40, 185), (185, 61), (61, 78)
] )

FACEMESH_LEFT_EYEBROW = frozenset( [
    (276, 283), (283, 282), (282, 295), (295, 285), (285, 336),
    (336, 296), (296, 334) , (334, 293), (293, 300), (300, 276)
] )

def getpoints ( pairs ):

    return list( numpy.array( list( pairs ) ).flatten() )

def getorderedpoints ( pairs ):

    pointpairs = list( pairs )
    points = [ pointpairs[ 0 ][ 0 ] , pointpairs[ 0 ][ 1 ] ]
    uniquepoints = len( getpoints( pairs ) )

    while len( points ) < uniquepoints:
        new = None
        for i , pair in enumerate( pointpairs ):
            if pair[ 0 ] == points[ -1 ]:
                new = pointpairs.pop( i )[ 1 ]
                break
            if pair[ 1 ] == points[ -1 ]:
                new = pointpairs.pop( i )[ 0 ]
                break
        if new is not None:
            points.append( new )
        else:
            points.append( points[ 0 ] )

    return points

def convertlandmarks ( landmarks , width , height ):

    pixels = []
    for ids , landmark in enumerate( landmarks ):
        pixels.append( (
            landmark.x * width ,
            landmark.y * height
        ) )
    return pixels

def createmask ( points ):

    pass
