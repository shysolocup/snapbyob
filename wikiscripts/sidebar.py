import sys
import os

logrefdir = sys.argv[1]
username = sys.argv[2];
useremail = sys.argv[3];
commitmsg = sys.argv[4];
repolink = sys.argv[5];


print(username, useremail, commitmsg, repolink);


commands = [
    'echo os is running',  
    'git add {0}'.format(logrefdir),
    'git commit -m "{0} & Updated wiki" {1}'.format(commitmsg, logrefdir),
    'git push',
    'git status'
];

#if token and token != "undefined":
  #  commands.insert(1, 'git remote set_url origin https://{username}:{token}@${reponame}.git'.format(username=username, token=token, reponame=reponame));

if username != "undefined" and useremail != "undefined":
    commands.insert(1, 'git config --global user.name {0}'.format(username));
    commands.insert(1, 'git config --global user.email {0}'.format(useremail));
    

for command in commands:
    print(command);
    os.system(command);


sys.stdout.flush()