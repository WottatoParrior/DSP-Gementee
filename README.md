# DSP-Gementee
This is a repo Team C-5 uses for version control and documentation regarding the Data Systems Project with the Gementee.



Info as to how to use git repos



1. Run git pull to get all the new changes from new branch
2. Run git checkout -b "Name of your branch"
3. Do your work on the branch
4. Run git add .
5. Run git commit -m "Name of the commit"
6. Run git push
7. Copy and paste the line the error will give you.
8. Create new pull request for your branch
9. Alert us that you have uploaded a new branch
10. Review the branch
11. Merge the branch


If there is something here that is missing let me know so I can add it :)



# Usage

The correct way is to setup a virtual enviornment and install all the dependencies there, so everyone
who uses this project runs the same dependencies and to prevent clashes with current installations.
To do that:

python3 -m venv .venv

source .venv/bin/activate # linux
.\.venv/scripts/activate # windows

pip install -r requirements.txt
