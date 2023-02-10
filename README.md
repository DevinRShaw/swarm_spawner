# Swarm Spawner

This code generates bot information such as name, email, and password. The information generated can be saved to a csv file.

## Dependencies

- random
- string
- pandas

## Functions

### `generate_random_name`
This function generates a random first and last name from the given list of names.

### `generate_random_email`
This function generates a random email based on the first and last name and a specified domain name.

### `generate_random_password`
This function generates a random password of a specified length (default is 8).

### `save_to_csv`
This function saves the bot information to a csv file with a specified filename.

### `spawn_bot_info`
This function generates bot information for a specified number of bots and a specified domain name.

## Application 
This is intended to be used as a part of a larger project to automatically make accounts using the csv created by this program
