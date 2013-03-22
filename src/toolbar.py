from PySide.QtCore import *
from PySide.QtGui import *
from models import *
import time
import os
import icons


class Toolbar(QToolBar):
    '''
    Initialize the main toolbar for the facepager-too that provides the central interface and functions.
    '''
    def __init__(self,parent=None,mainWindow=None):
        super(Toolbar,self).__init__(parent)
        self.mainWindow=mainWindow
        self.setToolButtonStyle(Qt.ToolButtonTextBesideIcon);
        self.setIconSize(QSize(24,24))
        
        self.addActions(self.mainWindow.actions.basicActions.actions())        
        self.addSeparator()
        self.addActions(self.mainWindow.actions.databaseActions.actions())
        
        self.addSeparator()
        self.addAction(self.mainWindow.actions.actionExpandAll)        
        self.addAction(self.mainWindow.actions.actionCollapseAll)
        self.addAction(self.mainWindow.actions.actionHelp)
        

        

            
    

            
    

