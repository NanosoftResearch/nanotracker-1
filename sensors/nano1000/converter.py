
import binascii


########################################################################
class MessageConverter:
    """Collection of static methods etc which can be used to convert messages to CAN like hex values"""

    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        
    def DateConvert(thisDate):
        
        return "not implemented"
    
    def TempConvert(tempVal):
        
        #below values taken from the CAN_MessageDefinitions
        resolution = 0.03125 
        offset = -40

        #apply offset and resolution, then get hex value
        retStr = MessageConverter.ConvertNumberToHex(tempVal,resolution,offset,4)
        
        return retStr

    def ConvertNumberToHex(numb, resolution, offset, hexValueCount):        

        numb += (offset * -1)
        numb = numb / resolution
        hexVals = hex(int(numb))
        hexStr =  hexVals.replace('0x','')       
        retStr = '{0}{1}'.format( '0' * (hexValueCount - len(hexStr)),hexStr)

        return retStr


x = MessageConverter.TempConvert(25)    
print(x)


    
        
        
    
    


