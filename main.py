import os

def main():
    # Define the path to the Python files in the project directory
    project_path = os.path.join(os.getcwd(), 'FlappyBird')

    print(f"Running Flappy Bird with Python files from {project_path}")

if __name__ == "__main__":
    main()