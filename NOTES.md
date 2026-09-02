# NOTES.md - Team Directory

## Part 1: Written Decisions

### Question 1: What is worth its own commit?

Category A: things that deserve their own commit
- Adding a new file on its own. It makes it easy to see what that file added later.
- Adding a new feature. It shows clearly what changed in the tool.
- Setting up .gitignore. It protects the whole project so it deserves its own step.
- Changes to the README. Keeping it separate from code keeps the history easy to read.

Category B: things I would not commit alone
- Fixing a typo right after I just made that mistake in the same session. Making it its own commit would just add clutter for something so small.
- Formatting or spacing changes with no real change to the code. On its own it does not help anyone understand the project better.
If I split these out I would get a very clean rule of one change per commit, but I would lose a readable history, since the log would be full of tiny fixes that do not matter on their own.

Category C: what I chose to ignore
I ignored .env, which holds a fake API key, and any .log files. If .env was committed by mistake and someone found out later, it would need to be removed from the whole history, not just deleted once. That means rewriting history and everyone else on the project having to redo their local copy. The secret could also already be exposed before anyone notices.

### Question 2: Merge vs rebase
A merge keeps the real story of what happened. It shows that two branches existed at the same time and were joined together, including a merge commit for that. A rebase moves my commits so they sit on top of the newest main branch, which makes the history look like one straight line, but it hides that the work was actually done separately.

For my conflict task I used a merge, because I want to actually see the conflict and how I fixed it stay in the history, not get rewritten away.

### Question 3: Remote operations
- git push -u origin main: sends my commits to GitHub and links my local branch to the one on GitHub.
- git push: sends any new commits after that link is already set up.
- git push origin --delete branchname: removes a branch from GitHub.
- git pull --rebase: pulls down commits from GitHub that I do not have yet and puts mine on top.

One thing pushing cannot check for me is whether my code actually works or whether my commit message is telling the truth. It also cannot tell me if I accidentally added a file I should have ignored. A push can go through with no errors even if something is wrong.

### Question 4: Commit messages
a. "fixed stuff" is too vague. Better: "Fix crash when directory has no entries"
b. "Update index.js" does not say what changed. Better: "Add sorting to team member list"
c. "WIP" does not explain anything. Better: "Add draft search filter, not finished yet"
d. This one is already good, it explains the behaviour clearly, so I left it as is.
e. "asdasd" means nothing, it should describe the actual change made.
f. "Changed line 47 of notes.md" talks about a line number instead of what changed. Better: "Fix typo in setup instructions"

## Part 3, Task 2: What I saw with git diff
1. Before I staged team.txt for the first time, git diff showed nothing at all. That is because the file was brand new and git was not tracking it yet, so there was nothing to compare.
2. Before I staged the change to app.py where I made it read team.txt, git diff showed the exact lines I added(a blank line), then the code that opens team.txt and prints its contents. The old line with just the print statement was marked as removed and re-added because a newline was missing at the end of the file.

## Task 4: Merge result
When I merged feature/add-search into main, git said Fast-forward. I knew this because main had not changed since I created the branch, so git could just move the main pointer forward without needing a separate merge commit.

## Task 7: What caused the conflict
The conflict happened because I edited the same line of README.md on two different branches at the same time, once on conflict-branch and once directly on main. Git could not automatically decide which version was correct since both changed the exact same line. I looked at both versions and picked the wording that made the most sense for the final README, then removed the conflict markers and completed the merge.

## Task 9: Merge vs rebase graph
Comparing the two graphs in git log --oneline --all --graph, the merge from Task 4 to 7 shows a diamond shape, since main and the feature branch both had separate commits that later joined back together. The rebase in Task 9 shows a straight line instead, since rebase moved my branch's commits to sit right on top of main's latest commit before merging.

I would use a merge when I want the real history of parallel work to stay visible, for example in a shared team branch. I would use a rebase when I want a clean, simple history for a small personal feature branch that nobody else is working on.

## Part 4: The rejected push
When I tried to push after making a direct edit on GitHub's website, my push was rejected because the remote had a commit I did not have locally. I used git pull --rebase instead of force-pushing, because force-pushing would have overwritten the commit I made on GitHub and lost that work. Pull --rebase instead fetched that commit, then replayed my local commit on top of it, so both changes stayed in history without losing anything or creating a fake merge.