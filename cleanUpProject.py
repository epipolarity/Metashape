import Metashape

def clean_up():

    depth_maps = 0
    orthomosaics = 0
    key_points = 0
    dense_clouds = 0

    app = Metashape.app
    for chunk in app.document.chunks:
        print(f"Checking chunk '{chunk.label}'")
        if chunk.depth_maps_sets:
            for dm_set in chunk.depth_maps_sets:
                depth_maps += len(dm_set.items())
                dm_set.clear()
        for ortho in chunk.orthomosaics:
            if ortho:
                ortho.removeOrthophotos()
                orthomosaics += 1
        if chunk.tie_points:
            chunk.tie_points.removeKeypoints()
            key_points += 1
        if chunk.point_clouds:
            for pc in chunk.point_clouds:
                if pc:
                    pc.clear()
                    dense_clouds += 1

    if depth_maps + orthomosaics + key_points + dense_clouds > 0:
        message = f"{depth_maps} Depth Maps removed\nOrthophotos removed from 'up to' {orthomosaics} orthomosaics\n" + \
                  f"Key points removed from 'up to' {key_points} chunks\n{dense_clouds} dense clouds removed\n\nSave Project now?"
        if app.getBool(label=message):
            app.document.save()
    else:
        app.messageBox("Nothing to clean up")
            
Metashape.app.addMenuItem("Custom Functions/Clean Up Project for Archive", clean_up)