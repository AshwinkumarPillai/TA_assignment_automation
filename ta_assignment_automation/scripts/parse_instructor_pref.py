"""
__author__ = "Ashwinkumar Ajithkumar Pillai"
__date__ = 3/12/24
__version__ = "1.0"
__license__ = "MIT style license file"
"""

from ..utils.csvToDict import read_csv_to_dict
from ..utils.dictionaryToJsonFile import write_dict_to_json

def parseInstructorPref(input_file_path:str ="input_files/Instr_Pref_old.csv", output_file_path:str ="output_files/ins_pref.json") -> None:

    """
    This function parses the Instructor preference and store that in a json file
    # TODO - Why CSCI4 and CSCI 6

    Arguments
    ----------
    input_file_path: str
        the path to the instructor preference CSV file
    output_file_path: str
        the path of the json file to store the instructor prefrence data
        
    Returned Values
    ----------
    None

    """

    pref_data = read_csv_to_dict(input_file_path)

    # Map ta by email to a dictonary
    # CSCI4050Saleh: {
    #  course_no: "CSCI4050",
    #   ins_lname: "Saleh",
    #   pref1: "email1"
    #   pref2: "email2"
    # }
    # 

    inst_pref = {}

    for row in pref_data:
        if row["Email"] and row["pref"] and not row["pref"].strip() == "---":
            ins_course_list = [p.strip() for p in row["pref"].split(";")]

            ta_email = row["Email"]

            for ins_course in ins_course_list:
                if len(ins_course) > 0 and ins_course[0] != '':
                    course_no = "CSCI"+ins_course.split("/")[1]
                    ins_lname = ins_course.split("/")[0].split("(")[0]
                    pref_num = ins_course.split("/")[0].split("(")[1][0]

                    ins_pref_key = course_no + ins_lname
                    ins_pref_grad_key = "CSCI6" + course_no[1:] + ins_lname

                    if ins_pref_key not in inst_pref:
                        inst_pref[ins_pref_key] = {}
                    if course_no[0] == '4':
                        inst_pref[ins_pref_grad_key] = {}

                    inst_pref[ins_pref_key]["ins_lname"] = ins_lname
                    inst_pref[ins_pref_key]["pref" + pref_num] = ta_email
                    inst_pref[ins_pref_key]["course_no"] = course_no

                    if course_no[0] == '4':
                        inst_pref[ins_pref_grad_key]["ins_lname"] = ins_lname
                        inst_pref[ins_pref_grad_key]["pref" + pref_num] = ta_email
                        inst_pref[ins_pref_grad_key]["course_no"] = "CSCI6" + course_no[1:]

    # Saving Course Data to output file
    print("Writing Ins Pref Data to JSON file: ", output_file_path)
    print("Total preferences added: ", len(inst_pref))
    write_dict_to_json(inst_pref, output_file_path)