# django-devsearch

Work in progress

A course project introducing the basics of Django. UIkit and static elements were provided by the course.

## TODOs:
- Instructor neglected some edge cases in Review Form handling:
  - ~~If an admin deletes a review from the admin page, vote counts are not updated.~~
  - ~~Hide the Review Form is the user is anonymous~~

- After handling admin deleted reviews, logic is needed in Project model's update_votes method so that 
division by zero is avoided for projects that have no votes.
- Ensure a user cannot vote on their own projects
