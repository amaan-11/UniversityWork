class Publication:

    def __init__(self,name):
        self.name=name


class Book(Publication):

    def __init__(self,name,author,page_count):
        super().__init__(name)
        self.author=author
        self.page_count=page_count

    def print_information(self):
        print(f"{self.name} was written by {self.author} and is {self.page_count} pages long")

class Magazine(Publication):

    def __init__(self,name,chief_editor):
        super().__init__(name)
        self.chief_editor=chief_editor

    def print_information(self):
        print(f"{self.name} was written by {self.chief_editor}")


DonaldDuck=Magazine("Donald Duck","Aki Hyppä")
DonaldDuck.print_information()
CompartmentNoSix=Book("Compartment Np. 6","Rosa Liksom",192)
CompartmentNoSix.print_information()