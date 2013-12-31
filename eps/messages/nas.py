'''
Created on 31 Ara 2013

@author: Abdulmecit Ozdemir
'''

def nasSecurityCommand(protocolDiscriminator, headerType, messageIdentity, securityAlgorithms, identifier, spareHalfOctet, replayedUESecurityCapabilities):
    return (
            "nas",
            {
            "messageType": {
            "procedureCode": "nasSecurityCommand",
            "typeOfMessage": "initiatingMessage"               
            },
            "protocolDiscriminator" : protocolDiscriminator, 
            "headerType" : headerType, 
            "messageIdentity" : messageIdentity, 
            "securityAlgorithms" : securityAlgorithms, 
            "identifier" : identifier, 
            "spareHalfOctet" : spareHalfOctet, 
            "replayedUESecurityCapabilities" : replayedUESecurityCapabilities
            } 
            
    )

def nasSecurityComplete(protocolDiscriminator, headerType, messageIdentity):
    return(
            "nas",
            {
            "messageType": {
            "procedureCode": "nasSecurityCommand",
            "typeOfMessage": "successfullOutcome"               
            },
            "protocolDiscriminator" : protocolDiscriminator,
            "headerType" : headerType,
            "messageIdentity" : messageIdentity
            }
           
    )
    
def nasSecurityReject(protocolDiscriminator, headerType, messageIdentity, EMMCause):
    return(
           "nas",
            {
            "messageType": {
            "procedureCode": "nasSecurityCommand",
            "typeOfMessage": "unsuccessfullOutcome"               
            },
            "protocolDiscriminator" : protocolDiscriminator,
            "headerType" : headerType,
            "messageIdentity" : messageIdentity,
            "EMMCause" : EMMCause
            }
           
           
    )    
