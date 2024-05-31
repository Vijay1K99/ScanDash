# Nmap Dashboard

This project is a Django-based application that visualizes Nmap scan results in a user-friendly dashboard. The dashboard presents the output in the form of graphs, pie charts, and tables.

The project is designed to work with a cron job that runs the Nmap command at regular intervals, producing an XML output file that is then utilized by this Django project.

## Features

- Visualize Nmap results in a user-friendly dashboard
- Data representation in the form of graphs, pie charts, and tables
- Automatic updates via cron job

![User Signup - Google Chrome 31-05-2024 23_21_00](https://github.com/Vijay1K99/ScanDash/assets/139844971/85e7aea5-59e6-4498-8053-fbead4f241e0)

![User Signup - Google Chrome 31-05-2024 23_21_32](https://github.com/Vijay1K99/ScanDash/assets/139844971/2262fe21-579e-402c-8e31-754df6fbeed9)

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.6+
- Django 3.2+
- Nmap

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/your_username_/Project-Name.git
   ```
2. Install Python packages
   ```sh
   pip install -r requirements.txt
   ```
3. Run the Django server
   ```sh
   python manage.py runserver
   ```

### Setting up the cron job

To set up the cron job that will run the Nmap command at regular intervals, you can use the `crontab` command in Unix-based systems.

1. Open the crontab file for editing
   ```sh
   crontab -e
   ```
2. Add the following line to run the Nmap command every hour (change the command and timing as needed)
   ```sh
   0 * * * * /path/to/nmap -oX /path/to/output.xml target
   ```

## Usage

Once everything is set up, you can navigate to the Django server's address in your web browser to view the Nmap results dashboard. The dashboard will automatically update at the interval set in your cron job.

## Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are greatly appreciated.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Contact

Your Email - kumarvj448@gmail.com
Project Link: [https://github.com/your_username/repo_name](https://github.com/Vijay1K99/ScanDash)

## Acknowledgements

- [Nmap](https://nmap.org/)
- [Django](https://www.djangoproject.com/)
- [Crontab](https://man7.org/linux/man-pages/man5/crontab.5.html)





