import os

class Duck:
    def __init__(self, path):
        self.path = os.path.abspath(path)
    
    def move_duck(self):
        # Implementation of duck's movement logic
        pass
    
    def see_world(self):
        print(f"Moving in {self.path}")

def main():
    project_path = os.path.join(os.getcwd(), 'FlappyBird')
    duck = Duck(project_path)
    duck.move_duck()
    duck.see_world()

if __name__ == "__main__":
    main()