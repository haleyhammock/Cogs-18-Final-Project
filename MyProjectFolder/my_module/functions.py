from my_module.schedule import *
import pandas as pd

GREETINGS_IN = ['hello', 'Hello']

GREETINGS_OUT = ['Let\'s get started on creating your class scedule!']

GOODBYE_IN = ['bye', 'Bye']

GOODBYE_OUT = ['Here is your schedule! ']

CLASS_DEPARTMENTS = ['AAS', 'AESE', 'AIP', 'ANAR', 'ANBI', 'ANES', 'ANSC', 'ANTH', 'AUD', 'AWP', 'BENG', 'BGGN', 
                     'BGJC', 'BGRD', 'BGSE', 'BIBC', 'BICD', 'BIEB', 'BILD', 'BIMM', 'BIOM', 'BIPN', 'BISP', 
                     'BNFO', 'CAT', 'CCS', 'CENG', 'CGS', 'CHEM', 'CHIN', 'CLAS', 'CLIN', 'CLRE', 'CLSS', 'CMM', 
                     'COGR', 'COGS', 'COMM', 'CONT', 'CSE', 'CSS', 'DDPM', 'DERM', 'DOC', 'DSC', 'DSE', 'DSGN', 
                     'EAP', 'ECE', 'ECON', 'EDS', 'EMED', 'ENG', 'ENVR', 'ERC', 'ESYS', 'ETHN', 'ETIM', 'EXPR', 
                     'FILM', 'FMPH', 'FPM', 'GLBH', 'GMST', 'GPCO', 'GPEC', 'GPGN', 'GPIM', 'GPLA', 'GPPA', 
                     'GPPS', 'HDP', 'HDS', 'HIAF', 'HIEA', 'HIEU', 'HIGL', 'HIGR', 'HILA', 'HILD', 'HINE', 
                     'HISC', 'HITO', 'HIUS', 'HLAW', 'HMNR', 'HUM', 'ICAM', 'ICEP', 'INTL', 'IRLA', 'JAPN', 
                     'JUDA', 'JWSP', 'LATI', 'LAWS', 'LHCO', 'LIAB', 'LIDS', 'LIEO', 'LIFR', 'LIGM', 'LIGN', 
                     'LIHI', 'LIHL', 'LIIT', 'LIPO', 'LISL', 'LISP', 'LTAF', 'LTAM', 'LTCH', 'LTCO', 'LTCS', 
                     'LTEA', 'LTEN', 'LTEU', 'LTFR', 'LTGK', 'LTGM', 'LTIT', 'LTKO', 'LTLA', 'LTRU', 'LTSP', 
                     'LTTH', 'LTWL', 'LTWR', 'MAE', 'MATH', 'MATS', 'MBC', 'MCWP', 'MDE', 'MED', 'MGT', 
                     'MGTA', 'MGTF', 'MGTP', 'MMW', 'MSED', 'MSP', 'MUIR', 'MUS', 'NANO', 'NEU', 'NEUG', 
                     'OPTH', 'ORTH', 'PATH', 'PEDS', 'PHAR', 'PHIL', 'PHYS', 'POLI', 'PSY', 'PSYC', 'RAD', 
                     'RELI', 'REV', 'RMAS', 'RMED', 'SE', 'SIO', 'SIOB', 'SIOC', 'SIOG', 'SOCD', 'SOCE', 
                     'SOCG', 'SOCI', 'SOCL', 'SOMC', 'SOMI', 'SPPS', 'SURG', 'SXTH', 'TDAC', 'TDDE', 'TDDM', 
                     'TDDR', 'TDGE', 'TDGR', 'TDHD', 'TDHT', 'TDMV', 'TDPF', 'TDPR', 'TDPW', 'TDTR', 'TMC', 
                     'TWS', 'UROL', 'USP', 'VIS', 'WARR', 'WCWP', 'WES']

CLASS_DEPARTMENTS_PROMPT = 'Please enter the class code! Ex: COGS'

CLASS_NUMBER = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 
                26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 
                49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 
                72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 
                95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 
                115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 
                134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 
                153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 
                172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 
                191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 
                210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 
                229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 
                248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266, 
                267, 268, 269, 270, 271, 272, 273, 274, 275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 
                286, 287, 288, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299]

CLASS_NUMBER_PROMPT = 'Please enter the class number! Ex: 18'

LEVEL = ['Lower Division', 'Upper Division', 'Graduate']

LEVEL_PROMPT = 'Please enter the level of the class! Ex: Lower Division'

CREDITS = [1, 2, 3, 4, 5, 6, 8, 9]

CREDITS_PROMPT = 'Please enter the number of credits this class is worth! Ex: 4'

DAYS_OF_WEEK = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

DAYS_OF_WEEK_PROMPT = 'Please enter the days of the week this class is on! Ex: Monday Wednesday Friday'

START_TIME = ['8', '9', '10', '11', '12', '1', '2', '3', '4', '5', '6', '9:30', '12:30', '3:30', '6:30']

START_TIME_PROMPT = 'Please enter the time the class starts at! Ex: 9'

QUESTION = 'I\'m not good at answering questions! Please contact academic advising for further help!'

class_list = []
number_list = []
credit_list = []
level_list = []
days_list = []
time_list = []


# This function was used from A3
def prepare_text(input_string):
    
    out_list = input_string.split()
    
    return out_list

# This function was used from A3
def is_question(input_string):
    
    if '?' in input_string:
        output = True
    else:
        output = False
    
    return output

# This function was adapted from A3
def is_in_list(element, in_list):
    
    if element in in_list:
        return True
    
    else:
        return False

def number_converter(string_number):
    """Returns an integer value of a string that is a number
    
    Parameters
    ----------
    string_string : string
        String of number to convert
        
    Returns
    -------
    converted_number : int
        int of string that was converted
    """
    
    converted_number = int(string_number)
    
    return converted_number

# Finds out the level of class 
def level_of_class(class_number):
    """Finds what level of class is entered.
    
    Parameters
    ----------
    class_number : int
        Class code
        
    Returns
    -------
    string
        String containing the level of the class.
    """
    
    if 1 <= class_number <= 99:
        return 'Lower Division'
    elif 100 <= class_number <= 199:
        return 'Upper Division'
    else:
        return 'Graduate'
    
# Finds out how difficult their quarter will be
def difficulty_of_quarter(credit_amount):
    """Finds out how difficult quarter will be based on number of credits.
    
    Parameters
    ----------
    credit_amount : int
        Number of credits taken
        
    Returns
    -------
    string
        String containing how difficult quarter will be.
    """
    
    if credit_amount <= 12:
        return 'Your quarter is going to be easy!'
    elif 12 < credit_amount <= 16:
        return 'Your quarter is going to be average.'
    else:
        return 'You are going to have a rough quarter.'
    

def ucsd_classes():
    """Stores the class into a schedule
    
    Parameters
    ----------
    None
    
    Returns
    -------
    Nothing
    """
    
    class_correct = False
    
    while not class_correct:
        
        class_department = input( 'Add a class class! '+ CLASS_DEPARTMENTS_PROMPT + ':\t')
        class_department_uppercase = class_department.upper()
        
        # checking if class is a UCSD class
        if is_in_list(class_department_uppercase, CLASS_DEPARTMENTS) == True:
            class_correct = True
            class_list.append(class_department_uppercase)
        else:
            print('Something is wrong. Either it is entered in the wrong way or it isn\'t a class.')

def ucsd_class_numbers():
    """Stores the class code into a schedule
    
    Parameters
    ----------
    None
    
    Returns
    -------
    Nothing
    """
    
    class_number_correct = False
    
    while not class_number_correct:
        try_class_number = True
        
        while try_class_number:
            
            # if input is not number program doesn't crash
            try:
                class_number = int(input(CLASS_NUMBER_PROMPT + ':\t'))
                try_class_number = False
            except ValueError:
                print('Type a number.')
            
        converted_number = number_converter(class_number)
        
        # sees if number is a valid class code
        if is_in_list(converted_number, CLASS_NUMBER) == True:
            class_number_correct = True
            number_list.append(converted_number)
        else:
            print('Something is wrong. Either it is entered in the wrong way or it isn\'t a class number.')
    
    level = level_of_class(converted_number)
    level_list.append(level)

def ucsd_credits():
    """Stores the number of credits into a schedule
    
    Parameters
    ----------
    None
    
    Returns
    -------
    Nothing
    """
    
    class_credit_correct = False
    
    while not class_credit_correct:
        
        try_credit = True
        
        while try_credit:
            
            # makes sure input won't crash program
            try:
                class_credit = int(input(CREDITS_PROMPT + ':\t'))
                try_credit = False
            except ValueError:
                print('Type a number')
            
        converted_credit = number_converter(class_credit)
        
        # seeing if credit is valid
        if is_in_list(converted_credit, CREDITS) == True:
            class_credit_correct = True
            credit_list.append(converted_credit)
        else:
            print('Something is wrong. Either it is entered in the wrong way or it isn\'t a valid credit amount.')
            
def ucsd_class_days():
    """Stores the days the class is on into a schedule
    
    Parameters
    ----------
    None
    
    Returns
    -------
    Nothing
    """
    
    class_days_correct = False
    
    while not class_days_correct:
                
        class_days = input(DAYS_OF_WEEK_PROMPT + ':\t')
        class_days_parsed = prepare_text(class_days)
        list_of_days = []
        
        for element in class_days_parsed:
            upper_element = element.capitalize()
            
            # making sure it is a correct day of the week
            if is_in_list(upper_element, DAYS_OF_WEEK) == True:
                list_of_days.append(upper_element)
                parsed_upper = class_days_parsed[-1].capitalize()
                
                # finding end of list of days when looping through
                if upper_element == parsed_upper:
                    class_days_correct = True 
            else:
                print('Something is wrong. Either it is entered in the wrong way or it isn\'t a day of the week.')
    
    days_list.append(list_of_days)
    
def ucsd_class_times():
    """Stores the time the class is at into a schedule
    
    Parameters
    ----------
    None
    
    Returns
    -------
    Nothing
    """
    class_time_correct = False
    while not class_time_correct:
                
        class_time = input(START_TIME_PROMPT + ':\t')
        
        # seeing if class time is a correct time
        if is_in_list(class_time, START_TIME) == True:
            class_time_correct = True
            time_list.append(class_time)
        else:
            print('Something is wrong. Either it is entered in the wrong way or it isn\'t a time for a class.')

def printing_schedule():
    """Prints the finalized schedule
    
    Parameters
    ----------
    None
    
    Returns
    -------
    Nothing
    """
    print('\n')  
    print('\n') 
    # creating the schedule in the respective categories
    schedule_dict = {'Time': time_list, 'Days': days_list, 'Class': class_list, 'Code': number_list, 
                        'Level': level_list, 'Credits': credit_list}
    df = pd.DataFrame(schedule_dict, columns = ['Time', 'Days', 'Class', 'Code', 'Level', 'Credits'])
    print(df)
    
    print('\n')  
    print('\n')
    
    counter_difficulty = 0
    
    # counting the total number of credits
    for element in credit_list:
        counter_difficulty += element
    
    # determining difficulty of quarter
    difficulty = difficulty_of_quarter(counter_difficulty)
    print(difficulty)