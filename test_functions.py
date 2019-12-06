from my_module.functions import *

def converter_testing():
    """Tests the number_converter function
    
    Parameters
    ----------
    None
    
    Returns
    -------
    Nothing
    """
    
    assert number_converter('1') == 1
    assert number_converter('5') == 5
    
def level_testing():
    """Tests the level_of_class function
    
    Parameters
    ----------
    None
    
    Returns
    -------
    Nothing
    """
    
    assert level_of_class(18) == 'Lower Division'
    assert level_of_class(101) == 'Upper Division'
    assert level_of_class(200) == 'Graduate'
       
    
def difficulty_testing():
    """Test the difficulty_of_quarter function
    
    Parameters
    ----------
    None
    
    Returns
    -------
    Nothing
    """
    
    assert difficulty_of_quarter(8) == 'Your quarter is going to be easy!'
    assert difficulty_of_quarter(14) == 'Your quarter is going to be average.'
    assert difficulty_of_quarter(20) == 'You are going to have a rough quarter.'