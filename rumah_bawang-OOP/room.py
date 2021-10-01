class Room():
    def __init__(self, roomName):
        self.name = roomName
        self.desc = None
        self.linked_room = {}
        self.character = None

    def set_character(self, character):
        self.character = character

    def get_char(self):
        return self.character

    def get_name(self):
        return self.name

    def set_desc(self, roomDesc):
        self.desc = roomDesc

    def get_desc(self):
        return self.desc

    def describe(self):
        print(self.desc)

    def link_room(self, room_to_link, direction):
        self.linked_room[direction] = room_to_link

    def get_info(self):
        print("Ruang",self.get_name())
        print("-"*25)
        print(self.get_desc())
        for direction in self.linked_room:
            room = self.linked_room[direction]
            print("Ruang", room.get_name(), "ada di sebelah", direction)

    def move(self, direction):
        if direction in self.linked_room:
            return self.linked_room[direction]
        else:
            print("Kamu tidak bisa pergi kearah sana, tidak ada pintu disana.")
            return self
