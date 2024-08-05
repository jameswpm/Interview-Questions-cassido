"""
Write a function that converts between metric and imperial units.
Break up the units into millimeters, centimeters, and meters for metric,
and into inches and feet for imperial, up to 2 decimal places.
"""

import sys

def convert_metric_2_imperial(number, unit):
    if unit == "m":
        # meters to inches
        to_inches = number * 39.3701        
    if unit == "cm":
        to_inches = number * 0.3937008
    if unit == "mm":
         to_inches = number * 0.03937008

    if to_inches > 12:
        # split into ft and in
        ft = to_inches // 12
        in_ = to_inches % 12
        print(f'{ft}ft {in_:.2f}in')
    else:
        print(f'{to_inches:.2f}ft')

def convert_imperial_2_metric(number, unit):
    if unit == "ft":
        to_milimeters = number * 304.8  
    if unit == "in":
        to_milimeters = number * 25.4

    if to_milimeters > 10:
        # split into m, cm and mm
        cm = to_milimeters // 10
        mm = to_milimeters % 10
        if cm > 100:
            # milimetters
            m = cm // 100
            cm = cm % 100
            print(f'{m}m {cm:.2f}cm {mm:.2f}mm')
        else:
            print(f'{m}m {cm:.2f}cm')
    else:
        print(f'{to_milimeters:.2f}m')       

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python <script>.py <number> <unit>.")
       
    number = sys.argv[1].strip()
    unit = sys.argv[2].strip()
    print(number, unit)

    if unit in ("m", "cm", "mm"):
        convert_metric_2_imperial(float(number), unit)
    elif unit in ("in", "ft"):
        convert_imperial_2_metric(float(number), unit)
    else:
        print("I don't know that one.")