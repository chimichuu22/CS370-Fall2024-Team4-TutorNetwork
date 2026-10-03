# Our Project Overview (Tutor-Network)

The Tutoring Network is a campus-based application that connects students with tutors. Students can search for tutors based on courses, and send tutoring requests. Tutors can create profiles, list the subjects they tutor, and accept or decline tutoring requests.

## Must Have Features

1. User registration and login
2. Student and tutor profiles
3. Tutors can list their subjects in their profile
4. Students can search for their tutors based on course
5. Students can send request to tutor
6. Tutor can accept the request or decline
7. Store the session information in a database
8. Student and tutor both can logout

## Nice-to-have Features

1. Student feedback and tutor ratings
2. Online or in-person session preference
3. Tutor availability schedules
4. Viewing previous session information
5. Filter tutors by their availability

## User story-1: (Search for tutors)

**As a student, I want to search for tutors by course so that I can find someone who can help me with that class.**

### Story beats and cost estimates

1. Create a search input box for searching based on the subject - 5
2. Read tutor information from the database - 8
3. Display matching tutors - 3
4. Display “No tutor found”, if not found in the database - 2

## User story-2: (Requesting a tutor session)

**As a student, I want to send a tutoring request to a tutor so that I can schedule help with a course.**

### Story beats and cost estimates

1. Add a button to request a tutor session. - 1
2. Save the request in the database. - 12
3. Set the initial request as pending - 8
4. Allow the tutor to view the request - 8
5. Allow the tutor to accept or decline the request - 3
6. Update and display the request status - 12
