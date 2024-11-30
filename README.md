# Py-Builder 1.0 Questions & Instructions
## What is Py-Builder?
Py-Builder is a light-weight python3 application (3.13.0 to be more exact). It uses one package which might not be installed which is **yaml or PyYaml**. The software itself without any add-on yaml packages is only **24k (24 killobytes)!** but it requires PyYaml which is about **3-5 mb (megabyte)** so its a total of about **3-5.024 mb**. Py-Builder uses ymal files to make templates. Like imagine you make a python template that you want to use, in this case you can use Py-Builder and write that template using our ymal file syntax. Now whenever you run the program it automatically loads in a  template like files and folders.

## How can I install Py-Builder?
To install Py-Builder start with cloning the branch which has the version you want. Every version has its own branch. Now you will need to run a few commands. Before you run the commands given below please go into the py-builder directory. Now run these in the command prompt. 

          sudo chmod +x installer
          sudo chcon -t systemd_unit_file_t pybuilder.service
          sudo chmod +x py-builder/cmd-adjust-pybuilder.sh
          sudo ./install.sh
and now you have successfuly setup Py-Builder.
