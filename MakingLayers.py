import rhinoscriptsyntax as rs
import Rhino.Geometry as geo
import math

def Run():
    
    
    # get string of layers
    
    rs.AddLayer("00 - Setup")
    rs.AddLayer("01 - Primary Structure")
    rs.AddLayer("02 - Secondary Structure")
    rs.AddLayer("03 - Thermal Layer")
    rs.AddLayer("04 - Envelope")
    rs.AddLayer("05 - Interior Linings")
    rs.AddLayer("06 - Elements")
    rs.AddLayer("07 - Annotation")
    rs.AddLayer("08 - Equipment")
    rs.AddLayer("09 - Site")
    rs.AddLayer("10 - DWG")
    rs.AddLayer("11 - Hatch")
    rs.AddLayer("99 - Electrical")
    rs.AddLayer("99 - Hydraulic")


if __name__=="__main__":
    Run()