# Py-Builder 1.0 Questions
## What is Py-Builder?
Py-Builder is a lightweight python3 application (3.13.0 to be more exact). It uses one package which might not be installed which is **yaml or PyYaml**. The software itself without any add-on yaml packages is only **24k (24 kilobytes)!** but it requires PyYaml which is about **3-5 MB (megabyte)** so it's a total of about **3-5.024 mb**. Py-Builder uses ymal files to make templates. Like imagine you create a Python template you want to use, in this case, you can use Py-Builder and write that template using our ymal file syntax. Now whenever you run the program it automatically loads in a  template like files and folders.

## How can I install Py-Builder?
To install Py-Builder, start by cloning the branch with the version you want. Every version has its own branch. Now, you will need to run a few commands. Before you run the commands given below, please go into the py-builder directory. Now, run these in the command prompt. 

          sudo chmod +x installer
          sudo chcon -t systemd_unit_file_t pybuilder.service
          sudo chmod +x py-builder/cmd-adjust-pybuilder.sh
          sudo ./install.sh
and now you have successfully setup Py-Builder.

## Is it safe and how do I know?
Yes, it's safe. You can check the source code to see. It might raise some flags but it isn't. You can even modify the source code if you feel it's unsafe.

# Py-Builder 1.0 Instructions
Now lets get to the instructions of how to use Py-builder.
