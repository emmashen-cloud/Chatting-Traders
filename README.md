# Chatting-Traders
In the attached file, there are four tables that describe users in a ForEx trading system and their communications via direct messages and forum-style discussion boards. The file 'users.tsv' contains unique user ids and account creation dates. The file messages.tsv contains unique message ids, send dates, sender ids (consistent with those in 'users.tsv'), and message types. The file 'discussions.tsv' contains unique discussion ids, creation dates, creator ids (consistent with those in 'users.tsv'), and discussion categories. The file 'discussion_posts.tsv' contain unique post ids, discussion ids (consistent with those in 'discussions.tsv'), and creator ids (consistent with those in 'users.tsv').

All files are TAB-separated. All times in the tables are expressed in milliseconds, starting on midnight, January 1, 1970. You shall convert the times to days (24hr).

You shall produce the following deliverables:

Simple descriptive statistics:
How many users are in the database? Deliverable: A number. 
What is the time span of the database? Deliverable: The difference between the largest and the smallest timestamps in the database, a number. 
How many messages of each type have been sent? Deliverable: A pie chart. 
How many discussions of each type have been started? Deliverable: A pie chart. 
How many discussion posts have been posted? Deliverable: A number.
Activity range is the time between the first and the last message (in ANY category) sent by the same user. What is the distribution of activity ranges? Deliverable: a histogram. 
Message activity delay is the time between user account creation and sending the first user message in a specific category. What is the distribution of message activity delays in EACH category? Deliverable: a histogram for each category (ideally all histograms shall be in the same chart, semi-transparent, with legend).
What is the distribution of discussion categories by the number of posts? What is the most popular category? Deliverable: a pie chart, with the most popular category highlighted.
Post activity delay is the time between user account creation and posting the first discussion message. What is the distribution of post activity delays in the most popular category? Deliverable: a histogram. Note: The most popular category shall be carried over from the previous question.
A box plot with whiskers that shows all appropriate statistics for message activity delays in EACH category, post activity delays, and activity ranges.
Finally, you shall write a short report that summarizes your findings in plain English language (for someone who knows neither CS nor Stats).

You shall be able to produce all deliverables in one program by applying appropriate transformations to one DataFrame, assembled from the four tabular files (however, two- and three-way merges shall work, too). The Y axis of all histograms shall be on the logarithmic scale.

You shall use Pandas. You shall not use CSV readers or any low-level Python tools to read files. You shall not use any loops or list comprehensions over table rows. (Loops over columns may be allowed, if necessary.)

