popit.capati is a set of tests of business rules to test integrity
of Sinar's Malaysian popit database entries.

Examples of tests include:

- Total number of MP Posts must be 222
- Must have only one MP holding a post at any time.
- Show posts that are not held by anyone (should not be unless
  byelection)
- Possibly double check against another public list such as official
  site.

The tests are in dicapati.py
You run them by running capati.py

If the capati passes, then janji dicapati.
