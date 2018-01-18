class Kangaroo(object):

    def __init__(self):
        self.pouch_contents = []

    def put_in_pouch(self,thing):
        self.pouch_contents.append(thing)

    def __str__(self):
        return "I have {} in my pouch".format(self.pouch_contents)

    def __repr__(self):
        return "Kangaroo <{}>".format(self.pouch_contents)

if __name__ == '__main__':
    kanga = Kangaroo()
    kanga.put_in_pouch("one")
    kanga.put_in_pouch("two")
    roo = Kangaroo()
    roo.put_in_pouch("three")
    roo.put_in_pouch("four")
    kanga.put_in_pouch(roo)
    print(kanga, roo)

