# Central Park Squirrel Census Data Analysis Project

## Overview
This project analyzes the 2018 Central Park Squirrel Census dataset to gain insights into the squirrel population in Central Park. It uses Python programming language and various libraries such as Pandas, Matplotlib, and Seaborn for data analysis and visualization.

## Contents
- [Introduction](#introduction)
- [Dataset Information](#dataset-information)
- [Project Tasks](#project-tasks)
- [How to Use](#how-to-use)
- [Dependencies](#dependencies)
- [Author](#author)

## Introduction
The 2018 Central Park Squirrel Census dataset provides detailed information about squirrel sightings in Central Park, including location, age, fur color, and behavior. This project aims to explore the dataset, analyze patterns, and visualize findings to better understand the squirrel population dynamics.

## Dataset Information

The 2018 Central Park Squirrel Census dataset provides comprehensive information about squirrel sightings in Central Park, New York City. Below is a description of the columns present in the dataset:

- **X**: Longitude coordinate for squirrel sighting point.
- **Y**: Latitude coordinate for squirrel sighting point.
- **Unique Squirrel ID**: Identification tag for each squirrel sighting. The tag is comprised of "Hectare ID" + "Shift" + "Date" + "Hectare Squirrel Number."
- **Hectare**: ID tag derived from the hectare grid used to divide the park area. One axis that runs predominantly north-to-south is numerical (1-42), and the axis that runs predominantly east-to-west is roman characters (A-I).
- **Shift**: Value is either "AM" or "PM," indicating whether the sighting session occurred in the morning or late afternoon.
- **Date**: Concatenation of the sighting session day and month.
- **Hectare Squirrel Number**: Number within the chronological sequence of squirrel sightings for a discrete sighting session.
- **Age**: Value is either "Adult" or "Juvenile."
- **Primary Fur Color**: Value is either "Gray," "Cinnamon" or "Black."
- **Highlight Fur Color**: Discrete value or string values comprised of "Gray," "Cinnamon" or "Black."
- **Combination of Primary and Highlight Color**: A combination of the previous two columns; this column gives the total permutations of primary and highlight colors observed.
- **Color notes**: Sighters occasionally added commentary on the squirrel fur conditions. These notes are provided here.
- **Location**: Value is either "Ground Plane" or "Above Ground." Sighters were instructed to indicate the location of where the squirrel was when first sighted.
- **Above Ground Sighter Measurement**: For squirrel sightings on the ground plane, fields were populated with a value of “FALSE.”
- **Specific Location**: Sighters occasionally added commentary on the squirrel location. These notes are provided here.
- **Running**: Squirrel was seen running.
- **Chasing**: Squirrel was seen chasing another squirrel.
- **Climbing**: Squirrel was seen climbing a tree or other environmental landmark.
- **Eating**: Squirrel was seen eating.
- **Foraging**: Squirrel was seen foraging for food.
- **Other Activities**: Additional activities of the squirrel observed by the sighter.
- **Kuks**: Squirrel was heard kukking, a chirpy vocal communication used for a variety of reasons.
- **Quaas**: Squirrel was heard quaaing, an elongated vocal communication which can indicate the presence of a ground predator such as a dog.
- **Moans**: Squirrel was heard moaning, a high-pitched vocal communication which can indicate the presence of an air predator such as a hawk.
- **Tail flags**: Squirrel was seen flagging its tail. Flagging is a whipping motion used to exaggerate squirrel's size and confuse rivals or predators. Looks as if the squirrel is scribbling with tail into the air.
- **Tail twitches**: Squirrel was seen twitching its tail. Looks like a wave running through the tail, like a breakdancer doing the arm wave. Often used to communicate interest, curiosity.
- **Approaches**: Squirrel was seen approaching human, seeking food.
- **Indifferent**: Squirrel was indifferent to human presence.
- **Runs from**: Squirrel was seen running from humans, seeing them as a threat.
- **Other Interactions**: Sighter notes on other types of interactions between squirrels and humans.
- **Lat/Long**: Latitude and longitude coordinates of the squirrel sighting point.

This dataset offers a comprehensive view of squirrel behavior, demographics, and interactions within the Central Park environment.

## Project Tasks
1. Display basic information about the dataset.
2. Display the first few rows of the dataset.
3. Perform summary statistics.
4. Visualize the distribution of fur colors.
5. Visualize the distribution of age categories.
6. Explore behavior patterns.
7. Visualize the distribution of behavior.
8. Geographic visualization (if latitude/longitude data is available).
9. Analyze age and color relationship.
10. Conduct correlation analysis.

## How to Use
To use this project:
1. Clone the repository to your local machine.
2. Install the required dependencies listed in the `requirements.txt` file.
3. Run the Python scripts provided in the repository to perform analysis and generate visualizations.

## Dependencies
- Python 3.x
- Pandas
- Matplotlib
- Seaborn

## Author
Utkarsh Saini
