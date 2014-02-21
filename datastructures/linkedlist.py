class LinkedList():
    elembefore=None
    elemafter=None
    value=None
    def __init__(self, value):
        self.value=value
    def insertbefore(self, before):
        '''insert an element before this one'''
        before.elembefore=self.elembefore
        before.after=self
        self.elembefore=before
    def insertafter(self, after):
        '''insert an element before this one'''
        after.elemafter=self.elemafter
        after.before=self
        self.elemafter=after
    def remove(self):
        '''insert an element before this one'''
        self.elemafter.elembefore=self.elembefore
        self.elembefore.elemafter=self.elemafter
        self.elembefore=self.elemafter=None

