import os
import csv

election_csv = os.path.join(r"C:\Users\aajanaku\OneDrive - Above the Treeline, Inc\Desktop\Resource", "election_data.csv")
output_file = "election_results.txt"

candidate_counts = {}
ballot_counts = {}

# Open and read csv
with open(election_csv) as csv_file:
    reader = csv.reader(csv_file, delimiter=",")

    csv_header = next(reader)

    for row in reader:
        candidate = row[2]
        if candidate in candidate_counts:
            candidate_counts[candidate] += 1
        else:
            candidate_counts[candidate] = 1

        # Count the unique ballots using a dictionary
        ballot_id = row[0]
        if ballot_id in ballot_counts:
            ballot_counts[ballot_id] += 1
        else:
            ballot_counts[ballot_id] = 1

# Calculate total ballot count
total_ballots = len(ballot_counts)

# Open the output file in write mode
with open(output_file, "w") as f:
    # Write the total ballot count
    f.write(f"Total Votes: {total_ballots}\n")

    # Write vote counts and percentages for each candidate
    for candidate, count in candidate_counts.items():
        percentage = (count / total_ballots) * 100
        f.write(f"{candidate}: {count} ({percentage:.2f}%)\n")

    # Determine and write the winner
    winner = max(candidate_counts, key=candidate_counts.get)
    f.write(f"Winner: {winner}\n")

# Print a message indicating the results were written to the file
print("Election results written to the file:", output_file)
