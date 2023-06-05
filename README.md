# Metashape Python Scripts

Place these files in

    C:\Users\<username>\AppData\Local\Agisoft\Metashape Pro\scripts\
    
and they will be added to a 'Custom Functions' menu each time you start Metashape

## bBox2Coords.py

**Tested  in Metashape 1.8**

Align the bounding box/region to the current chunk local coordinate system in all enabled chunks

based on this code: https://www.agisoft.com/forum/index.php?topic=3045.msg16048#msg16048


## buildOrthos.py

**Tested in Metashape 1.7**

Build Orthomosaics in all enabled chunks, prompting the user for the local coordinates planar projection to use (top, bottom, front, back, left, right).

If different projections are required in different chunks, these can be specified by including the desired projection in parentheses within the respective chunk label (name), and selecting 'c' (by chunk) when prompted for the projection.

Orthomosaics are generated from the model surface at the default resolution.

based on information from here: https://www.agisoft.com/forum/index.php?topic=1322.msg15758#msg15758


## filterPoints.py

**Tested in Metashape 1.8**

Perform gradual selection on all enabled chunks, deleting points below the specified thresholds and then optimising with default parameters.

Default parameters are the ones I use most of the time.

User is prompted to change the values if they wish. Setting a value of 0 disables that filter.

based on this code: https://agisoft.freshdesk.com/support/solutions/articles/31000154629-how-to-select-fixed-percent-of-the-points-gradual-selection-using-python

and this snippet from the 1.5.0 python api pdf: https://www.agisoft.com/pdf/metashape_python_api_1_5_0.pdf

    chunk = Metashape.app.document.chunk # active chunk
    threshold = 0.5
    f = Metashape.PointCloud.Filter()
    f.init(chunk, criterion = Metashape.PointCloud.Filter.ReprojectionError)
    f.selectPoints(threshold)


## groupPhotosByPath.py

**Tested in Metashape 1.7**

Create camera groups in each enabled chunk, and name them according to the name of the directory in which the respective image files reside.


## cleanUpProject.py

**Tested in Metashape 2.0**

Remove depth maps, dense clouds, orthophotos (not orthomosaics), key points from a list of projects to be acrhived.


## setVerticalAxis.py

**Tested in Metashape 2.0**

Renames the currently selected marker to "ortho_origin" and creates a new marker 2 'units' directly above it with the name "ortho_z". You can then create a marker at any location in your desired x-axis and name this "ortho_x" and use these three markers in the generate orthomosaic dialog using 'vertical' marker alignment method to generate a repeatably oriented orthomosaic. requires 'up direction' is already established in coordinate system.
