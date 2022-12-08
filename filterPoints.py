import Metashape
    

def filters_to_str(point_filters):
    filter_str = ""
    for f in point_filters:
        filter_str += f['name'] + ": " + str(f['value']) + "\n"        
    return filter_str
    
def get_filter_values(point_filters):
    for f in point_filters:
        if type(f['value']) == int:
            f['value'] = app.getInt(f['name'] + ' (0 = disabled)', f['value'])
        elif type(f['value']) == float:
            f['value'] = app.getFloat(f['name'] + ' (0.0 = disabled)', f['value'])
        if f['value'] < 0:
            f['value'] = 0

def filter_active_chunks():

    point_filters = [
        {'type': Metashape.PointCloud.Filter.ReprojectionError, 'value': 0.5, 'name': 'Reprojection Error'},
        {'type': Metashape.PointCloud.Filter.ReconstructionUncertainty, 'value': 100.0, 'name': 'Reconstruction Uncertainty'},
        {'type': Metashape.PointCloud.Filter.ImageCount, 'value': 0, 'name': 'Image Count'},
        {'type': Metashape.PointCloud.Filter.ProjectionAccuracy, 'value': 10.0, 'name': 'Projection Accuracy'}
        ]
        
    app = Metashape.app
    doc = app.document

    prompt_string = "Use defaults? \n\n{}".format(filters_to_str(point_filters))
    if not app.getBool(prompt_string):
        get_filter_values(point_filters)

    point_filter = Metashape.PointCloud.Filter()

    for chunk in doc.chunks:
        if chunk.enabled:
            doc.chunk = chunk
                
            for f in point_filters:
                if f['value'] > 0:
                    point_filter.init(chunk, criterion = f['type'])
                    point_filter.removePoints(f['value'])
            chunk.optimizeCameras()
            
Metashape.app.addMenuItem("Custom Functions/Filter and Optimise Enabled Chunks", filter_active_chunks)