# Py-Builder 1.0 Questions
## What is Py-Builder?
Py-Builder is a lightweight python3 application (3.13.0 to be more exact). It uses one package which might not be installed which is **yaml or PyYaml**. The software itself without any add-on yaml packages is only **24k (24 kilobytes)!** but it requires PyYaml which is about **3-5 MB (megabyte)** so it's a total of about **3-5.024 mb**. Py-Builder uses ymal files to make templates. Like imagine you create a Python template you want to use, in this case, you can use Py-Builder and write that template using our ymal file syntax. Now whenever you run the program it automatically loads in a  template like files and folders.

## How can I install Py-Builder?
To install Py-Builder, start by cloning the branch with the version you want. Every version has its branch. Now, you will need to run a few commands. Before you run the commands given below, please go into the py-builder directory. Now, run these in the command prompt. 

          sudo chmod +x installer
          sudo chcon -t systemd_unit_file_t pybuilder.service
          sudo chmod +x py-builder/cmd-adjust-pybuilder.sh
          sudo ./install.sh
and now you have successfully set up Py-Builder.

## Is it safe and how do I know?
Yes, it's safe. You can check the source code to see. It might raise some flags but it isn't. You can even modify the source code if you feel it's unsafe.

# Py-Builder 1.0 Instructions
Now let's get to the instructions on how to use Py-builder.
## 1) Scripting Packages
To write a Package you will first need to make a file called package_name_here.yaml (replace package_name_here with the package name you want when the app is run). Next, you will need  to use this template: 
```yaml
Type: "dir"
Commands: "NEW_DIR src  %$thisstringisonlyusedforslpittingandnotanythingelseoritwillerror$% NEW_FILE main.py WITHIN src %$thisstringisonlyusedforslpittingandnotanythingelseoritwillerror$% NEW_FILE error.txt"
```
Here you will see a  few keywords inside the commands they are `NEW_FILE` which makes a new file (the name is set to the  string after the keyword) then we have `NEW_DIR` this makes a new folder (same with the file the name is set to the string after the keyword. And lastly `WITHIN` is very simple it just goes into a folder like here the src folder then executes the command. If you want it to be a  folder inside a folder inside a folder then it would be like this `first_folder/second_folder/third_folder`

**Important Notice: It automatically changes the dir to the work dir (which is py-builder name_of_work_dir_here package_name_here) so if you make a  new dir called src  imagine the work dir is exe it would put it inside the exe folder but this doesn't apply to WITHIN, because WITHIN only runs the command and exits back to the main work dir**

## 2) Commands
