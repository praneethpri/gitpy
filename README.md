# GitPy

GitPy is a python script to add, commit and push to github with a single command.

It runs following commands one by one.

```bash
git add .
```
```bash
git commit -am "<Commit Message>"
```
```bash 
git push
```

### Usage

##### Prerequisits

Python 3 needs to be installed.
There are no other depedencies.

1) clone the repository.
2) make a bash alias,

```bash
echo "alias gitpy='python ~/path/to/script/gitpy.py'" >> ~/.bashrc
```
replace the ```~/path/to/script``` with the correct path.

3) source the bashrc.

```bash
source ~/.bashrc
```

4) run ```gitpy``` in the terminal

5) When prompted write a commit message. (quotes are not necessary.)

