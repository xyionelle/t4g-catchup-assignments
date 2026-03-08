# Git Conflict Notes

## What is a Git Conflict?

A git conflict happens when two people edit the same part of a file and Git cannot automatically decide which version to keep when merging.

## Steps to Resolve a Git Conflict

1. Git will show conflict markers inside the file.
2. Open the file and look for <<<<<<< HEAD.
3. Compare both versions of the changes.
4. Decide which version to keep (or combine them).
5. Remove the conflict markers.
6. Save the file.
7. Stage the file using git add.
8. Commit the resolved changes.

## Reflection

From the class simulation, I learned that communication is very important when working in teams. Conflicts happen when people change the same code, so it is important to review changes carefully before merging.
## Why Git Conflicts Happen

Git conflicts usually happen when multiple developers work on the same file or branch at the same time without pulling the latest changes.
