import fbx
from PIL import Image
import sys

filepath = r'cubeMan.fbx'

validTextureDimensions = [ (256, 256), (512, 512) ]
#validTextureDimensions = [ (256, 256), (512, 512), (1024, 1024) ]

manager = fbx.FbxManager.Create()

importer = fbx.FbxImporter.Create( manager, 'myImporter' )

status = importer.Initialize( filepath )

if status == False:
    print 'FbxImporter initialization failed.'
    print 'Error: %s' % importer.GetLastErrorString()
    sys.exit()


scene = fbx.FbxScene.Create( manager, 'myScene' )

importer.Import( scene )

importer.Destroy()

textureArray = fbx.FbxTextureArray()

scene.FillTextureArray( textureArray )

invalidTextures = {}

for i in range( 0, textureArray.GetCount() ):
    
    texture = textureArray.GetAt( i )
    
    if texture.ClassId == fbx.FbxFileTexture.ClassId:
        
        textureFilename = texture.GetFileName()
        
        image = Image.open( textureFilename )
        
        width, height = image.size
        
        if (width, height) not in validTextureDimensions:
            
            invalidTextures[ textureFilename ] = (width, height)
            
            print 'Invalid dimensions (%sx%s) - %s\n' % (width, height, textureFilename )

#----------------------- PART 2 -----------------------# 

def findTexturesOnNodes( node, textureDictionary, currentPath = [] ):
    
    currentPath.append( node.GetName() )
    
    #print 'Path: %s' % currentPath
    
    for materialIndex in range( 0, node.GetMaterialCount() ):
        
        material = node.GetMaterial( materialIndex )
        
        #print '\tMaterial: %s' % material.GetName()
        
        for propertyIndex in range( 0, fbx.FbxLayerElement.sTypeTextureCount() ):
            
            property = material.FindProperty( fbx.FbxLayerElement.sTextureChannelNames( propertyIndex ) )
            
            #if property.GetName() != '':
                
                #print '\t\tProperty: %s' % property.GetName()
            
            for textureIndex in range( 0, property.GetSrcObjectCount( fbx.FbxFileTexture.ClassId ) ):
                
                texture = property.GetSrcObject( fbx.FbxFileTexture.ClassId, textureIndex )
                
                #print '\t\t\tTexture: %s' % texture.GetFileName()
                
                textureFilename = texture.GetFileName()
                
                if textureFilename in textureDictionary.keys():
                    
                    width, height = textureDictionary[ textureFilename ]
                    
                    print 'Texture (%sx%s) found at: %s > %s > %s > "%s"' % (width, height, currentPath, material.GetName(),
                                                                             property.GetName(), textureFilename )
    
    #print ''
    
    for i in range( 0, node.GetChildCount() ):
        
        findTexturesOnNodes( node.GetChild( i ), textureDictionary, currentPath )
    
    currentPath.pop()

findTexturesOnNodes( scene.GetRootNode(), invalidTextures )
    
    
    
    
    
    
    





