# Auto Insight
This dockerized app provides a visualization of the relationships between different numerical characteristics of various car models. The primary goal of this application is to enable better understanding and analysis of car features using scatter plot visualization.

# Description
Users can select two numerical columns from a PostgreSQL database table titled "auto". This table consists of eight columns, each depicting various characteristics of several car models. Upon selection, the application generates a scatter plot with one variable on the x-axis and the other on the y-axis. This graphical representation allows users to observe and analyze the relationship between the chosen variables. Non-numerical values within the dataset are not selectable, ensuring the validity and reliability of the visualization.

# What was done
Connected to PostgresSQL database containing a table auto with 8 columns reporting the characteristics of several car models. Using Python Plotly Dash and Docker, i created a micro dockerized webapp that allows to select with a selector 2 numerical columns (out of 7) from the table and visualize on the right the corresponding scatter plot (x: variable 1, y: variable 2). Non-numerical values are ignored. The dockerized app is then deployed on the AWS cloud computing platform.
