from collections import defaultdict

votes = ["pasta","pasta","pasta","pasta","pasta","paratha","paratha","paratha"]

count_votes = defaultdict(int)

for vote in votes:
    count_votes[vote] += 1

sorted_votes = sorted(count_votes.items(), key=lambda kv: kv[1], reverse=True)
if len(sorted_votes) > 1:
    if sorted_votes[1][1] == sorted_votes[0][1]:
        print('NOTA')
    else:
        print(sorted_votes[0][0])