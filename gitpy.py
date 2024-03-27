import subprocess, os, sys

cwd = os.getcwd()
os.chdir(cwd)
result = subprocess.run(['git', 'add', '.'], capture_output=True, text=True)
print(f'\033[93m{result.stdout}\033[0m')
print('''
git added                   \033[92mDone!\033[0m
      ''')
print('''
git commit
      ''')
commit_message = input('Commit Message : ')
commit_string_array = ['git', 'commit', '-am']
commit_message_formatted = f'"{commit_message}"'
commit_string_array.append(commit_message_formatted)
command_2 = subprocess.run(commit_string_array, capture_output=True, text=True)
print(f'\033[93m{command_2.stdout}\033[0m')
print('''
git commited                \033[92mDone!\033[0m
      ''')
command_3 = subprocess.run(['git', 'push'], capture_output=True, text=True)
print(f'\033[93m{command_3.stdout}\033[0m')
print('''
git pushed                  \033[92mDone!\033[0m
      ''')
