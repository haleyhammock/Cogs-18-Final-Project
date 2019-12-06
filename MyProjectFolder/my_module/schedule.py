from my_module.functions import *

def make_schedule():
    """Holds all the functions that create the schedule
    
    Parameters
    ----------
    None
    
    Returns
    -------
    Nothing
    """
    
    my_schedule = True
    
    while my_schedule:
        total_credits = 0
    
        ucsd_classes()
                    
        ucsd_class_numbers()
    
        ucsd_credits()
    
        ucsd_class_days()
        
        ucsd_class_times()
        
        ending = False
        
        while not ending:
            
            ending_input = input('If you want to quit press q or else hit n ' + ':\t')
            # endcoding 'q' to exit out of the chatbot
            if ending_input == 'q':
                my_schedule = False
                ending = True
            # if user want to continue 'n' is pressed 
            elif ending_input == 'n':
                ending = True
                continue
            else:
                print('Something is wrong. Enter in n or q.')
                
    printing_schedule()
    