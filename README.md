# Car Registration System
This is a simple car registration system written in Python using PySide6 based on a requirement from Gama Academy's Inclusão Tech program.

The system allows users to register cars and search for cars by ID, brand, model, and year. The system also has a view to show the last car registered.

## Requirements
To run the system, you need to have PySide6 and Python 3 installed on your computer.

## Installation
You can install PySide6 using pip:

```
pip install PySide6
```

## Usage
To run the system, run the car_registration.py file:

```
python car_registration.py
```

The main window of the system will be displayed. From here, you can click on the buttons to navigate to different parts of the system.

### Registering a Car

To register a car, click on the "Register Cars" button. The registration form will be displayed, where you can enter the car details such as brand, model, and year. The ID of the car will be generated automatically based on the number of cars registered. If there are no cars registered, the ID will be 1.

### Searching for a Car

To search for a car, click on the "Search Cars" button. You can select the search field (ID, brand, model, or year) and enter the search value. The system will display the results in a table.

### Viewing the Last Car Registered

To view the last car registered, click on the "Last Registrations" button. The system will display the last car registered in a table.

### Contributing

Contributions are welcome! If you find a bug or have a suggestion for improvement, please open an issue or submit a pull request.

### License

This project is licensed under the MIT License.