import sys
import shutil
from pathlib import Path

# Directory containing example function files
FUNCTIONS_DIR = Path(__file__).parent / "examples"
# Destination directory for copied files
FILE_DIR_DEST = Path("/home/ec2-user/projects/modal/scratch")

def copy_function_file(function_name: str, dest_name: str = None) -> None:
    """
    Copy a function file from the functions directory to the destination directory.
    Raises an error if the destination file already exists.
    
    Args:
        function_name (str): Name of the function file (without .py extension)
        dest_name (str, optional): Desired name for the destination file (without .py extension)
    """
    # Ensure destination directory exists
    FILE_DIR_DEST.mkdir(exist_ok=True)
    
    # Construct source and destination paths
    source_file = FUNCTIONS_DIR / f"{function_name}.py"
    dest_file = FILE_DIR_DEST / f"{dest_name or function_name}.py"
    
    if not source_file.exists():
        print(f"Error: Function file '{function_name}.py' not found in {FUNCTIONS_DIR}")
        sys.exit(1)
        
    if dest_file.exists():
        print(f"Error: Destination file '{dest_file}' already exists")
        sys.exit(1)
        
    try:
        shutil.copy2(source_file, dest_file)
        print(f"Successfully copied {function_name}.py to {FILE_DIR_DEST}")
    except Exception as e:
        print(f"Error copying file: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) not in [2, 3]:
        print("Usage: python copy.py <function_name> [dest_name]")
        print("Example: python copy.py sb")
        print("Example: python copy.py sb new_name")
        sys.exit(1)
        
    function_name = sys.argv[1]
    dest_name = sys.argv[2] if len(sys.argv) == 3 else None
    copy_function_file(function_name, dest_name)
