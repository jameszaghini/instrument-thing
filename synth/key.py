import mido


class Key:
    def __init__(self, note, down_id, up_id):
        self.note = note
        self.down_id = down_id
        self.up_id = up_id

        self.is_down = False
        self.play = False

        self.message = mido.Message("note_on", note=note)

    def process(self, value):
        if value == self.down_id:
            if not self.is_down:
                self.play = True
            self.is_down = True
        elif value == self.up_id:
            self.is_down = False
