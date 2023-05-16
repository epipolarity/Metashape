import Metashape

def clean_up():

    depth_maps = 0
    depth_maps_chunks = 0
    orthophotos_chunks = 0

    app = Metashape.app
    for chunk in app.document.chunks:
        print(f"Checking chunk '{chunk.label}'")
        if chunk.depth_maps_sets:
            for dm_set in chunk.depth_maps_sets:
                depth_maps += len(dm_set.items())
                dm_set.clear()
            depth_maps_chunks += 1
        for ortho in chunk.orthomosaics:
            if ortho:
                ortho.removeOrthophotos()
                orthophotos_chunks += 1

    if depth_maps + depth_maps_chunks + orthophotos_chunks > 0:
        message = f"{depth_maps} Depth Maps removed from {depth_maps_chunks} chunk(s)\nOrthophotos removed from 'up to' {orthophotos_chunks} chunk(s)\n\nSave Project now?"
        if app.getBool(label=message):
            app.document.save()
    else:
        app.messageBox("No depth maps or orthomosaics found")
            
Metashape.app.addMenuItem("Custom Functions/Clean Up Project for Archive", clean_up)