class LetterShape:
    faces: list[str]
    
    def __init__(self, *faces) -> None:
        self.faces = list(faces)
    
    def get_face_index(self, sub_string: str) -> int:
        for index, face in enumerate(self.faces):
            if sub_string in face:
                return index
            
    def is_valid(self, *strings: str) -> bool:
        last_end_char = None
        for string in strings:
            if (last_end_char != None) and (string[0] != last_end_char):
                return False
            last_face_index = None
            for letter in string:
                curr_face_index = self.get_face_index(letter)
                if (curr_face_index == None) or (curr_face_index == last_face_index):
                    return False
                last_face_index = curr_face_index
            last_end_char = string[-1]
        return True

    def get_remainder(self, *strings: str) -> bool:
        letters = ""
        for face in self.faces:
            letters += face
        for string in strings:
            for letter in string:
                letters = letters.replace(letter, "")
        return letters