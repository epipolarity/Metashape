import Metashape
import math

def buildOrthos():

	app = Metashape.app

	front = Metashape.Matrix([[1, 0, 0, 0],[0, 0, 1, 0],[0, -1, 0, 0],[0, 0, 0, 1]])
	back = Metashape.Matrix([[-1, 0, 0, 0],[0, 0, 1, 0],[0, 1, 0, 0],[0, 0, 0, 1]])
	left = Metashape.Matrix([[0, -1, 0, 0],[0, 0, 1, 0],[-1, 0, 0, 0],[0, 0, 0, 1]])
	right = Metashape.Matrix([[0, 1, 0, 0],[0, 0, 1, 0],[1, 0, 0, 0],[0, 0, 0, 1]])
	top = Metashape.Matrix([[1, 0, 0, 0],[0, 1, 0, 0],[0, 0, 1, 0],[0, 0, 0, 1]])
	bottom = Metashape.Matrix([[-1, 0, 0, 0],[0, -1, 0, 0],[0, 0, -1, 0],[0, 0, 0, 1]])
	
	userProj = app.getString("Specify ortho projection plane (f=front, b=back, r=right, l=left, t=top, bo=bottom, c=by chunk)","")

	proj = Metashape.OrthoProjection()
	proj.type = Metashape.OrthoProjection.Type.Planar

	if (userProj==None):
		return
	elif (userProj=="f"):
		proj.matrix = front
	elif (userProj=="b"):
		proj.matrix = back
	elif (userProj=="r"):
		proj.matrix = right
	elif (userProj=="l"):
		proj.matrix = left
	elif (userProj=="t"):
		proj.matrix = top
	elif (userProj=="bo"):
		proj.matrix = bottom
	elif not (userProj == "c"):
		return
	
	for chunk in app.document.chunks:
		if chunk.enabled:
			if (userProj == "c"):
				if (chunk.label.lower().find("(top)") > -1):
					proj.matrix = top
				elif (chunk.label.lower().find("(bottom)") > -1):
					proj.matrix = bottom
				elif (chunk.label.lower().find("(back)") > -1):
					proj.matrix = back
				elif (chunk.label.lower().find("(right)") > -1):
					proj.matrix = right
				elif (chunk.label.lower().find("(left)") > -1):
					proj.matrix = left
				else:
					proj.matrix = front
					
			proj.crs = chunk.crs
			
			chunk.buildOrthomosaic(projection=proj,surface_data=Metashape.DataSource.ModelData,blending_mode=Metashape.BlendingMode.MosaicBlending)
			app.document.save()

Metashape.app.addMenuItem("Custom Functions/Build Orthomosaics in Enabled Chunks", buildOrthos)