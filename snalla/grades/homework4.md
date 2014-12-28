homework4 Feedback
==================

Commit graded: 67408ef811b0ade4c3393931da04113e22e81b18

### Version control - Git (10/10)

### Iterative development (17/30)
+ -3, The user pages does not seem to be based on your Grumblr
    design. All pages of a web app should have a unified look and feel.

+ -10, Posting a grumbl crashes the application, and nothing works anymore
    afterwards.

### ORM usage (25/30)
+ -3, You should not get all instances of a model and manually filter it with a
    loop. This is very inefficient compared to using Django’s built in filtering
    (generally O(n) vs O(log n)).

+ -1, We suggest using a OneToOneField to a user because there should only be
    one instance of this object per user. Selecting the correct relation is
    important for database performance.

+ -1, Its unnecessary to have both a followers and following relation, they both
    represent the same information

### Coverage of technologies (22/40)
+ -8, No Django forms apart from examples used.

+ -10, Email address confirmation for new users was not implemented.

### Validation (15/20)
+ -5, URL parameters are user input and must be properly validated. Your site
    crashes when navigating to the profile of a non-existing user. Consider
    raising a HTTP 404 error if a given URL parameter is invalid. This may be
    useful:
    https://docs.djangoproject.com/en/1.7/topics/http/shortcuts/#get-object-or-404

### Design (0/0)
+ -0, You may want to consider breaking views.py into several files grouped by
    functionality

### Additional feedback

---

#### Total score (89/130)

---

Graded by: Bailey Forrest (bcforres@andrew.cmu.edu)
https://github.com/CMU-Web-Application-Development/snalla/blob/master/grades/homework4.md
