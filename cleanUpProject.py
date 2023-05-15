import Metashape

def clean_up():

    depth_maps = 0
    depth_maps_chunks = 0
    orthophotos_chunks = 0

    app = Metashape.app
    for chunk in app.document.chunks:
        if chunk.depth_maps:
            depth_maps += len(chunk.depth_maps.items())
            chunk.depth_maps = None
            depth_maps_chunks += 1
        for ortho in chunk.orthomosaics:
            ortho.removeOrthophotos()
            orthophotos_chunks += 1

    if depth_maps + depth_maps_chunks + orthophotos_chunks > 0:
        message = f"{depth_maps} Depth Maps removed from {depth_maps_chunks} chunk(s)\nOrthophotos removed from 'up to' {orthophotos_chunks} chunk(s)\n\nSave Project now?"
        if app.getBool(label=message):
            app.document.save()
    else:
        app.messageBox("No depth maps or orthomosaics found")
            
Metashape.app.addMenuItem("Custom Functions/Clean Up Project for Archive", clean_up)