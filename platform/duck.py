import os

class Duck:
    """Duck (class)."""
    def __init__(self, path):
        """Init.

        Args: path.
        """
        self.path = os.path.abspath(path)

    def move_duck(self):
        # Implementation of duck's movement logic
        """Move duck (function)."""
        pass

    def see_world(self):
        """See world (function)."""
        print(f"Moving in {self.path}")

def main():
    """Main (function)."""
    project_path = os.path.join(os.getcwd(), 'FlappyBird')
    duck = Duck(project_path)
    duck.move_duck()
    duck.see_world()

if __name__ == "__main__":
    main()