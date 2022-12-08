import Metashape
import os

def groupByPath():

	for chunk in Metashape.app.document.chunks:
	
		groupLabels = []
		groups = []
	
		if chunk.enabled:
		
			for cam in chunk.cameras:
			
				dirName = os.path.split(os.path.split(cam.photo.path)[0])[1]
				
				if (dirName not in groupLabels):
					groupLabels.append(dirName)
					g1 = chunk.addCameraGroup()
					g1.label = dirName
					g1.type = Metashape.CameraGroup.Type.Folder
					groups.append(g1)
					
				grpIdx = groupLabels.index(dirName)
				cam.group = groups[grpIdx]
				
Metashape.app.addMenuItem("Custom Functions/Group photos by path", groupByPath)