class Intern:
    def __init__(self, name = "My name? I'm nobody, an intern, I have no name."):
        self.Name = name

    def __str__(self):
        return self.Name

    class Coffee:
        def __str__(self):
            return "This is the worst coffee you ever tasted."
    
    def make_coffee(self):
        return self.Coffee()

    def work(self):
        raise Exception("I'm just an intern, I can't do that...")


def test():
    inter1 = Intern()
    Mark = Intern('Mark')
    print(inter1)
    print(Mark)
    print(inter1.Coffee())
    print(inter1.make_coffee())
    try : 
        print(inter1.work())
    except Exception as e:
        print(e)
    

if __name__ == "__main__":
    test()
