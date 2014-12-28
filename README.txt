==================================================

 R E A D M E . T X T 

 Introduction to the Python FBX SDK

 Autodesk Scripting and SDK Learning Channel

==================================================


Instructions on how to work with the provided Python scripts (in Windows):


  1. Create a folder at C:\Autodesk, and copy the cubeMan.fbx file into it.


  2. Ensure you have Python 2.6 or Python 3.1 installed.
     [URL: http://www.python.org/download/releases/2.6/] or [URL: http://www.python.org/download/releases/3.1/]


     2.1. Set your PATH environment variable to point to the installed "Python" folder, for example: C:\Python26.

	  To do this, click on the Start menu, type "env" and press Enter. In the User variables section, if
          the "PATH" variable does not exist, press "New", otherwise select the "PATH" variable and press "Edit".

              > "New": The "Variable name" should be PATH and the "Variable value" should be for example: C:\Python26.

              > "Edit": Append the location, for example: C:\Python26, to the "Variable value" field.


  3. Ensure you have the Python FBX SDK installed on your computer, and that you have copied
     the appropriate lib/<Python_version> files into you matching Python installation's Lib/site-packages folder.     
     [URL: http://usa.autodesk.com/adsk/servlet/pc/item?siteID=123112&id=10775847]


  4. Ensure you have the Python Imaging Library installed. We use this in our Python script to open a .png file.
     [URL: http://www.pythonware.com/products/pil/]


  5. Run the provided .py files in Python. To do this from the command line:


    5.1. In the folder that you extracted the Python scripts, hold CTRL+SHIFT and Right-click in an empty space
         and select "Open command window here".


    5.2. In the command line window, type "python fbxTextureChecker-p1.py" to test the script for part 1. This will
         only work if you have set your PATH environment variable in step 2.1.

         > If successful, the following message should be printed:
           
           "Invalid dimensions (1024x1024) - C:\Autodesk\cubeMan.fbx/hat.png"


    5.3. Type "python fbxTextureChecker-p2.py" to test the script for part 2. This will only work if you have set your
         PATH environment variable in step 2.1.

         > If successful, the following message should be printed:

           "Invalid dimensions (1024x1024) - C:\Autodesk\cubeMan.fbx/hat.png
            
            Texture (1024x1024) found at: [u'RootNode', u'chest', u'head', u'hat'] > hatMat > DiffuseColor > "C:\Autodesk\cubeMan.fbm/hat.png" "



