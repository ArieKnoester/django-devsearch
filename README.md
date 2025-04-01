# django-devsearch

Work in progress

A course project introducing the basics of Django. UIkit and static elements were provided by the course.

## TODOs:
- Instructor neglected some edge cases in Review Form handling:
  - ~~If an admin deletes a review from the admin page, vote counts are not updated.~~
  - Needs error handling so that an unauthenticated user can not submit a project review.

- After handling admin deleted reviews, logic is needed in Project model's update_votes method so that 
division by zero is avoided for projects that have no votes.