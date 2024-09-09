class Scripts:

    def __init__(self, proj):
        self.project = proj;

    def insert(self, ref, *args):

        global block;
        block = self.project.blocks;

        if type(ref) == str:

            refs = ref.split(".");
            for r in refs:
                block = block[r];

        elif type(ref) == list:

            for r in refs:
                block = block[r];


5