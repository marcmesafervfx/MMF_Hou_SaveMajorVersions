def saveMajorVersion():
    actualpath = hou.hipFile.path()
    actualfile = hou.hipFile.basename()
    lic = str(hou.licenseCategory())
    
    if 'Commercial' in lic: file = '.hip'
    elif 'Indie' in lic: file = '.hiplc'
    elif 'Education' in lic or 'Apprentice': file = '.hipnc'
    
    removeext = actualpath.replace(file, '')
    removeextbase = actualfile.replace(file, '')
    
    try:
        origver = removeextbase.split("_t")
        origtake = removeextbase[-5:]
        if not len(origver) > 1:
            raise
        v = origver[-2]
        
        ver = v[-3:]
        newver = str(int(ver)+1)
        newver = newver.zfill(3)
        
        prever = 'v' + ver
        newver = 'v' + newver
        
        newpath = actualpath.replace(prever, newver)
        newpath = newpath.replace(origtake, "_t000")
        hou.hipFile.save(newpath, True)
    
    except:
        clean = removeext + '_v000_t000.hip'
        hou.hipFile.save(clean, True) 

saveMajorVersion()
