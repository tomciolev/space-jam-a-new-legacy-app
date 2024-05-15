import csv

# The name of the player is in the second column (index 1).
NAME_INDEX = 1

# The PER of the player is in the 10th column (index 9).
PER_INDEX = 9

# There are only 15 players that we are reading in.
COUNT = 15

# Open the game_stats.csv file.
with open('game_stats.csv') as csv_file:
    # Use the CSV reader and confirm the delimeter is a comma.
    csv_reader = csv.reader(csv_file, delimiter=',')

    # Initialize the counter and empty lists.
    character_count = 0
    names = []
    pers = []
    urls = []

    # Loop through each row in the CSV file.
    for row in csv_reader:
        # Ignore the first row since that is the header.
        if character_count == 0:
            character_count += 1
        # Only take data from the first 15 because we only need the player's initial PER, not for each quarter.
        elif character_count <= COUNT:
            # The name of the player is in the second column (at index 1).
            names.append(row[NAME_INDEX])

            # The image file of the player is their name with no spaces or period and all lowercase.
            urls.append("https://sjanlassets.blob.core.windows.net/assets/" + row[NAME_INDEX].replace(" ","").replace(".","").lower()+".png")

            # The PER of the player is in the 10th row (at index 9).
            pers.append(row[PER_INDEX])

            # Increment the counter so we only get one set of data for each player.
            character_count += 1
        else:
            break

# Create a players.json file if it isn't already created and open it.
# The parameter "w" will overwrite the file if anything is in it.
f = open("players.json", "w")

# Write the opening bracket of the JSON object to the file.
f.write("[\n")

# Iterate over all of the players.
for index in range(0,COUNT):
    # Write the opening bracket of the first player object to the file.
    f.write("\t{\n")

    # Write the name, PER, and image url, with their labels, to the file.
    f.write("\t\t\"name\": \""+names[index]+"\",\n")
    f.write("\t\t\"per\": \""+pers[index]+"\",\n")
    f.write("\t\t\"imgUrl\": \""+urls[index]+"\"\n")
    f.write("\t},\n")

    # Write the opening bracket of the Yosemite Sam object to the file.
f.write("\t{\n")

# Write his name, PER (0), and image url, with the data labels, to the file.
f.write("\t\t\"name\": \"Yosemite Sam\",\n")
f.write("\t\t\"per\": \"0\",\n")
f.write("\t\t\"imgUrl\": \"https://sjanlassets.blob.core.windows.net/assets/yosemitesam.png\"\n")

# Since he is the last of the Tune Squad, don't include a comma after closing his object.
f.write("\t}\n")

# Write the closing bracket to the JSON object to the file.
f.write("]")

# Close the file.
f.close()