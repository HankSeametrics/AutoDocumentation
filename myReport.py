#----------------------------------------------------------------------
# Report template class
''' author: Henry Beck '''
# date: 07/16/2019
# email: hbeck@seametrics.com
#----------------------------------------------------------------------


#----------------------------------------------------------------------
# Revision Log
#
# Rev   Date        Author  Description    
#----------------------------------------------------------------------
'''

    1   2019/07/16    HTB     (1) Initial Release
   
'''
#----------------------------------------------------------------------
# MODULES
#----------------------------------------------------------------------
import docx
import datetime

class Report():
    Header="Issue Report:"
    def __init__(self, Bench, User):
        report = Document()
        report.add_heading(self.Header)
        
