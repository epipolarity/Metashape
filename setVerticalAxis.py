import Metashape

def set_ortho_vertical_axis():
    chunk = Metashape.app.document.chunk
    markers = chunk.markers

    # Check if a marker is selected
    marker = None
    for m in markers:
        if m.selected:
            marker = m
            break

    if marker:
        # Rename the current marker to "ortho_origin"
        marker.label = "ortho_origin"

        # Create a new marker with the same X and Y values as the current marker, but with the Z value increased by 2
        new_marker = chunk.addMarker()
        new_marker.reference.location = Metashape.Vector((marker.reference.location[0], marker.reference.location[1], marker.reference.location[2] + 2))

        # Name the new marker "ortho_z"
        new_marker.label = "ortho_z"

    else:
        # If no marker is selected, display a message
        print("No marker is selected!")

Metashape.app.addMenuItem("Custom Functions/Set Ortho Vertical Axis", set_ortho_vertical_axis)