# django-google-photos

A web application for synchronising and backing up Google Photos accounts and media, implemented as a django package.

## Overview

A simple web interface to securely and privately synchronise and visualise the state of a Google Photos account (or several ones), 
and easily download and backup media (photos and videos) from these accounts (along with its meta data such as albums etc.) to various destinations.

Privacy and security is built in as a primary feature.

Visualise, search and manage meta data about your media (albums, sharing, geo-locations, etc.), and eventually update it back to the Google Photos account. 

Using a simple login mechanism to access your Google Photos account, easily list your media and back it up to various destinations such as:

- a local folder on a hard drive
- a folder in a Google Drive account
- Amazon S3
- Azure Storage
- and more

## (Initial) motivation

Unfortunately Google [has announced](https://support.google.com/photos/answer/9316089) that your Google Photos no longer sync to your Google Drive.

Personally, I was using this feature to automatically backup all my photos from my Google account to a local hard drive, using a Raspberry Pi at home.
The idea was to simply use [rclone](https://rclone.org/) to synchronise a Google Drive folder with a hard drive folder. [You can read more about this setup on my personal website](https://bastienbourdon.com/2017/home-backup/).

However this is no longer possible, as Google now refuses to sync your Photos in your Drive account.

While researching a workaround, I found out there is a good Google Photos REST API, using OAuth 2 and good standards and documentation.

I decided to develop a web interface that I could run from a personal server or my Raspberry Pi at home, for regularly and automatically synchronising and backing up the state of Photos accounts.
This would be a good replacement for my former (no longer supported) solution.

I realised this could make a good Django Package that other people could use in other contexts, such as web applications that rely on a Google Photos account.

## Dependencies

Python 3.5 or later, Django 2, Django REST Framework v3, SQLite, and optionally various other packages for backup destinations (Amazon S3, Azure Storage, Google Drive, etc.)

## Installation

This app will be implemented as a regular django package, and available to install via a regular `pip install`.

More on that as the project progresses.

## Configuration

Your app will require a Google Photos Library API credentials. You need to us the Google Cloud Console to create such credentials for your app.
1. Login to https://console.developers.google.com/apis/
2. Create a new Project or use an existing one
3. Navigate to Library, and search for Photos: enable the [Photos Library API](https://console.developers.google.com/apis/library/photoslibrary.googleapis.com)
4. Click Create Credentials and follow the steps
5. Download/copy the resulting client ID and client secret

- Define the backup destinations in settings
- Login to your Google Account and authorise this app to read your data
- Define a backup schedule (daily, weekly, etc,)
- ... more details to come

## Planned features

- Security and privacy from the start
- Support for multiple Google Photos accounts
- List, view, and download all the media and its meta data from the Google Photos accounts
- Search and filter media by various criteria
- Visualise activity on the account
- Backup (synchronise) the media and meta data to a various range of destinations
   - a local folder on a hard drive
   - a folder in a Google Drive account
   - an mazon S3 container
   - an Azure Storage container
   - ... and potentially more based on user demand
- Visualise the state of the backups
- Send email alerts when storage is too low or when other events happen

## Integration

This django package can easily be added to any other django project that requires accessing a Google Photos account.

## Contributing

I welcome any help and ideas! 
This app has the potential to be expanded and maintained for many use cases I could not think of.
You are welcome to propose feature ideas and help implementing relevant improvements and new functionality.

Moreover there is always room for better documentation and clarity, or more test coverage.

If you would like to contribute:

1. Fork it (https://github.com/Bastien-Brd/django-google-photos/fork)
2. Create your feature branch (git checkout -b feature/fooBar)
3. Commit your changes (git commit -am 'Add some fooBar')
4. Push to the branch (git push origin feature/fooBar)
5. Create a new Pull Request

## License

Distributed under the GNU GPLv3 license. [See the license](https://github.com/Bastien-Brd/django-google-photos/blob/master/LICENSE) for more information.
