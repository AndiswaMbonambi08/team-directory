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

## Reflection

1. What made a commit high value in this project
The commits I kept separate were things like adding the script, adding the data file, adding the search function, and setting up the gitignore. Each one did one clear thing, so if something broke later I could look back and know exactly which commit caused it. One thing I bundled together instead of splitting up was the small edit to app.py where I only added one comment line at the top. I did not make that its own giant explanation, I just committed it with a short message, because it was such a small change that splitting it further would not help anyone understand the project better.

2. My merge vs rebase choice
For the conflict task in Part 3, I used a merge, not a rebase. I chose this because I wanted the conflict and how I fixed it to actually stay visible in my history, the same way I said in Question 2. If I had used a rebase there instead, it would have looked like the conflict never happened, and that is not what the task wanted me to show.

3. The rejected push
When I edited README.md directly on GitHub and then tried to push a small local commit without pulling first, my push got rejected. Git told me the remote had a commit I did not have locally yet. I used git pull --rebase instead of forcing the push through, because forcing it would have overwritten the change I made on GitHub and lost that work completely. Pull --rebase pulled down that missing commit first, then placed my local commit on top of it, so nothing got lost and there was no fake merge commit either.

4. Other things I learned 
was that rebase can also cause a conflict, not just a merge. I thought conflicts only happened when merging two branches, but when I rebased my branch onto main, git still could not automatically combine the changes because the same part of README.md was edited in both places.

Something I also noticed about myself while doing this assignment is that in the beginning I forgot to keep updating NOTES.md as I went along. I only wrote the Part 1 answers at the start and then got caught up in the terminal commands, so I had to go back later and add things like the diff observations and the merge notes after I had already done those steps instead of writing them down right away. Next time I would try to update NOTES.md straight after each task instead of leaving it for later.

I also ran into a few small mistakes along the way that were not really about git itself, like typing commands with a missing space, using bash style commands like cat and touch in PowerShell where they do not work, and getting stuck in the git config pager and the vim editor without knowing how to exit them. These were not really git problems, but they taught me that the terminal itself has its own rules I still need to get more comfortable with.

## Stretch A: Interactive rebase cleanup
I made 3 small messy commits on a branch called stretch-a-cleanup, with vague messages like wip and fix typo. Using git rebase -i HEAD~3, I squashed all 3 into one clean commit with a proper message. Before, git log showed 3 separate small commits, after the rebase it showed just 1 commit combining all the changes. This made the history much easier to read since a reviewer would not need to look at 3 tiny steps that were really just one small fix.

## Stretch B: Pre-commit hook
I added a pre-commit hook at .git/hooks/pre-commit that checks if .env is staged before allowing a commit. To test it, I force-added .env with git add -f .env and tried to commit. The hook blocked the commit and printed my custom message, "Blocked: .env is staged, remove it before committing", instead of letting the commit go through. I then removed .env from staging with git restore --staged .env, and afterward it was ignored normally again.

## Stretch C: Pull request workflow
Instead of merging feature/pr-demo locally, I pushed it to GitHub and opened an actual Pull Request, then used the Squash and merge option instead of a normal merge. Looking at git log --oneline --all --graph afterward, this showed up as one single clean commit on main, with no diamond shape and no separate merge commit, unlike Task 4 to 7 where a real merge created a visible diamond in the graph. Squash and merge is useful when you want a clean history and do not care about seeing every small commit from the feature branch, but you lose the detailed step by step history of what happened on that branch.

## Assignment 1.2

### Question 1 — Why fork, not branch, this time?

In 1.1 I had write access to my own repo, so branching directly made sense. This time I don't have write access to my partner's repo, so I can't push a branch there directly — GitHub would just reject it. Forking gives me my own copy of their repo where I do have write access, and lets me open a Pull Request from my copy back into theirs. If I tried to clone their repo and push a branch straight to it, the push would fail with a permissions error, since I'm not a collaborator on it.

### Question 2 — PR description: bad vs. good

Bad version:

"added search"

Good version:

What: Added a Search-TeamMembersByRole function to team.ps1 that lets a user search team members by role.
Why: The directory only supported searching by name. Teams often need to find everyone in a given role (e.g. all Backend Developers), so this fills a real gap.
How to verify: Run .\team.ps1, enter a role like "Developer" when prompted, and confirm it prints only matching entries.

The second version is easier to review because it tells the reviewer exactly what changed, why it was needed, and how to test it themselves — they don't have to reverse-engineer the intent from the code alone.

### Question 3 — Triaging review comments

A blocking comment is something that must be fixed before merge — a bug, a missing case, or something that would break for other users. A nit/suggestion is a preference that doesn't affect correctness, like naming or formatting — nice to have, not required. A question is the reviewer asking for clarification, not necessarily asking for a change.

My rule: if the comment points out something that would cause incorrect behavior or a real gap, I treat it as blocking. If it's about style, naming, or "could also do it this way," I treat it as a nit. If it's phrased as "why did you..." or "what happens if...", I treat it as a question until it's clear whether they expect a change.

### Question 4 — When fetch beats pull

After my partner's PR is merged into my repo, before pulling I'd run git fetch and check origin/main first, rather than pulling straight away. This lets me see exactly what changed and confirm the merge commit is there with my partner's name as the author, before it touches my local main. If I just ran pull blindly, I'd merge it in immediately without ever having looked at what I was about to bring in — fine most of the time, but risky if there's ever a conflict or something unexpected upstream.

### Reflections

**What you contributed, and why:** I added a Search-TeamMembersByRole function to my partner's team.ps1, letting a user search team members by role instead of only by name. I judged this genuinely useful rather than trivial because the existing tool only supported name search, and finding everyone in a given role (e.g. all Backend Developers) is a common real need as a team grows.

**A comment you received that changed your code:** My partner left a blocking comment on my PR pointing out a duplicate/incomplete "## Assignemnt 1.2" section in my NOTES.md, caused by a merge from main that pulled in her own answers alongside mine. I fixed it by deleting the duplicate section and pushing a follow-up commit, keeping only my original complete answers.

**A comment you gave that you stand by:** On my partner's PR, I left a blocking comment on her get_entries() function, noting that it would throw an unhandled exception if team.txt was missing or unreadable, and suggested wrapping it in a try/except with a clear error message instead. I stand by this because a real user hitting a missing file shouldn't see a raw traceback — that's a genuine reliability gap, not a style preference.

**Fetch vs. pull, in practice:** In my original 1.1 folder, I ran git fetch before pulling and saw origin/main sitting one commit ahead of my local main. Checking the commit before pulling showed it was authored by mathabomohapi99-crypto, not me — concrete proof the contribution came from outside my own machine. Only after confirming that did I run git pull, which fast-forwarded cleanly. This made the value of fetch-before-pull real rather than theoretical: I actually saw what was about to change before it touched my branch, instead of trusting a blind pull.

**Note on process:** I initially merged my partner's PR into my repo before completing my review, which reversed the intended order. I recovered by adding blocking and nit comments to the merged PR afterward, submitted as a "Comment" review since "Request changes" isn't available on a merged PR. Going forward, I'll wait to submit my review before clicking merge.