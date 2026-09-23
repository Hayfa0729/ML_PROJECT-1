from setuptools import find_packages,setup 

def get_Requirements(file_path:str)->list[str]:
    '''
    This function will return the list of requirements
    '''
    with open(file_path) as file_obj:
        Requirements = file_obj.readlines()
        Requirements = [req.replace("\n","") for req in Requirements]
        
        if "-e ." in Requirements:
            Requirements.remove("-e .")
    
    return Requirements

setup(
    name = "ML_PROJECT-1",
    version = "0.0.1",
    author = "Hayfa",
    author_email = "amberhayfa18@gmail.com",
    packages = find_packages(),
    install_requires = get_Requirements('Requirements.txt')
)
