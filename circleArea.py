Python 3.9.0 (v3.9.0:9cf6752276, Oct  5 2020, 11:29:23) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> import math
>>> import sys
>>> radius = float(input( "Enter radius in feet : " ))
Enter radius in feet : 3
>>> area = math.pi * radius * radius
>>> sys.stdout.write("The radius you provided was " + format(radius,'.2f') +
                " feet and the area is about " + format(area,'.2f') + " sq feet" )

The radius you provided was 3.00 feet and the area is about 28.27 sq feet73
>>> import math
>>> import sys
>>> radius = float(input( "Enter radius in feet : " ))
Enter radius in feet : 8
>>> area = math.pi * radius * radius
>>> print("The radius you provided was " + format(radius,'.2f') +
                " feet and the area is about " + format(area,'.2f') + " sq feet" )
The radius you provided was 8.00 feet and the area is about 201.06 sq feet
>>> 