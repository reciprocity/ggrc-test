'''
Created on Jul 20, 2013

@author: diana.tzinov

'''

from Elements import Elements

class GRCObject(object):
    elem = Elements()
    """
    program_elements = {
                        "title":elem.object_title,
                        "owner":elem.object_owner, 
                        "url":elem.object_url, 
                        "code":elem.object_code, 
                        "organization":elem.object_organization, 
                        "scope":elem.object_scope}
                        
                        
    program_values = {
                      'title':"",  
                      'owner':"testrecip@gmail.com", 
                      'url': "http://www.google.com", 
                      'code':"PCI", 
                      'organization': "ORG", 
                      'scope': ""}
    """
    
    program_elements = {
                        "title":elem.object_title,    
                        "description":elem.object_description,
                        "url":elem.object_url,
                        } 
 
    
    
    program_values = {
                      'title':"",  
                      "description":"",
                      'url': "http://www.google.com", 
                      }
    
    contract_elements = {
                        "title":elem.object_title,    
                        "description":elem.object_description,
                        "url":elem.object_url,
                        } 
 
    
    
    contract_values = {
                      'title':"",  
                      "description":"",
                      'url': "http://www.google.com", 
                      }
    
    control_elements = {
                        "title":elem.object_title,    
                        "description":elem.object_description,
                        "url":elem.object_url,
                        } 
 
    
    
    control_values = {
                      'title':"",  
                      "description":"",
                      'url': "http://www.google.com", 
                      }
        
    policy_elements = {
                        "title":elem.object_title,  
                        "description":elem.object_description,   
                        "url":elem.object_url,
                        } 
 
    
    
    policy_values = {
                      'title':"",  
                      "description":"",
                      'url': "http://www.google.com", 
                      }
    
    regulation_elements = {
                        "title":elem.object_title,    
                        "description":elem.object_description,
                        "url":elem.object_url,
                        } 
 
    
    
    regulation_values = {
                      'title':"",  
                      "description":"",
                      'url': "http://www.google.com", 
                      }
    
    """
    
    
    
    policy_elements = {
                        "title":elem.object_title,  
                        "owner":elem.object_owner, 
                        "url":elem.object_url, 
                        "code":elem.object_code, 
                        "kind":elem.object_kind
                       }
    policy_values = {
                      'title':"",  
                      'owner':"testrecip@gmail.com", 
                      'url': "http://www.google.com", 
                      'code':"PCI", 
                      'kind': "Company Policy"}
    
    regulation_elements = {
                        "title":elem.object_title,  
                        "owner":elem.object_owner, 
                        "url":elem.object_url, 
                        "code":elem.object_code 
                       }
    regulation_values = {
                      'title':"",  
                      'owner':"testrecip@gmail.com", 
                      'url': "http://www.google.com", 
                      'code':"PCI"}
    
    contract_elements = {
                        "title":elem.object_title,  
                        "owner":elem.object_owner, 
                        "url":elem.object_url, 
                        "code":elem.object_code 
                       }
    contract_values = {
                      'title':"",  
                      'owner':"testrecip@gmail.com", 
                      'url': "http://www.google.com", 
                      'code':"PCI"}
    
    
    regulation = []
    contract =[]
    

    """