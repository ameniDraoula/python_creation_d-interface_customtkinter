
import customtkinter
import tkinter
import university_data
class Student:
    pass
class licence_student(Student):
    pass
class Prof:

   # une liste de 4 professeur 
 professeurs = ['yohan Amar', 'Marie Martin', 'Pierre Durand', 'Lucie Dubois']

   # creation d'un dectionnnaire de 4 professuer
 professeurs = {
    'yohan Amar': {
        'age': 45,
        'matière': 'mathématiques',
        'ville': 'Paris'
    },
    'Marie Martin': {
        'age': 38,
        'matière': 'français',
        'ville': 'Lyon'
    },
    'Pierre Durand': {
        'age': 53,
        'matière': 'histoire',
        'ville': 'Marseille'
    },
    'Lucie Dubois': {
        'age': 41,
        'matière': 'physique',
        'ville': 'Toulouse'
    }
}






 def __init__(self , name_p , age_p , payee_p ,courses: list=[] , autres_univ): # courses: list=[] objet facultatif 
       self.courses=courses
 def set_give_cources(self  , is_giving_courses:bool):
        if (is_giving_courses):
             self.is_giving_courses=True
 def get_give_cources(self ):
        return True
       

professeur1= Prof( autres_univ=[])
class user:
    pass
class Univercity_App:
    app_version=2.5
    app_name ="univercity app"

    def __init__(self , full_screen_arg:bool =False) :
        self.full_screen = full_screen_arg
        def initialization(self , class_name):
            self.class_name = class_name
            if (self.class_name =="Student"):
                self.new_student_class=Student()
                def quit_app(self):
                    pass
