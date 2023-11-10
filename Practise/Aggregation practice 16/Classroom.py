class Classroom:
    def __init__(self,building,room_no):
        self.building = building
        self.room_no = room_no

    def __str__(self):
        return f'Building: {self.building}\tRoom no: {self.room_no}'