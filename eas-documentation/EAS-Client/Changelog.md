This document contains all changes made to EAS Client application.

### 0.9.2 - 2022-12-19

- Migrate from .Net 5 to .Net 7;
- Implement an ability to support document migration and validation for new FZL-Schemas without updating to new client versions;

### 0.9.1.1 - 2022-10-10

- Fixed: senderId ignored for retrieving override configuration when signing before sending

### 0.9.1 - 2022-04-11

- Implement ability to upload certificates and private keys and storage them as base64 string;
- Implement ability to secure configuration;
- Implement ability to edit settings in JSON editor;

### 0.9.0 - 2022-04-04

- Implement ability to validate outgoing and incoming documents;
- Implement ability to migrate a document to a specific version;
- Automatically send failed receipts when use command `--recieve folderName`;
- Update favicons with a new logo;
- Improve a configuration section;

### 0.8.8.3 - 2022-03-22

- Implement ability to renew a private/public key;
- Implement ability to renew a certificate;

### 0.8.8.2 - 2022-03-17

- Fix bug:  Anyone can send to BVG Exchange participant with wrong Sender UID;

### 0.8.8.1 - 2022-03-10

- Fix bug: Swagger not working in docker EASClient;

### 0.8.8 - 2022-02-08

- WEB GUI: improve styling for different themes;
- Support FZL V1.5;
- Support configuring mutliple subscriptionkey/privatekeys on EAS Client;
- Allow user to switch participant shown in EAS Client;
- Improve API error handling;

### 0.8.7 - 2021-12-24

- WEB GUI: improve registration flow;
- WEB GUI: implement field validation for registration page;
- WEB GUI: imrpove notification;
- Fix bug with fetching IDs from .xml file
- Move toggle for changing theme to the navigation bar.
- --generatekeys name - fix unexpected errors.
- Implement urls according to current environment.

### 0.8.6 - 2021-11-24

- WEB GUI: registration 

### 0.8.5 - 2021-08-18

- Support of multiple platforms and architectures
- Use Client Certificates from storage, in addition to file system
- Web GUI: dark mode
- Web GUI: preview buttons in lists

### 0.8.4 - 2021-08-06

- Web GUI: document and receipt management
- Web GUI: participants overview
- Web GUI: document logs with graphical previews for new operations
- Web GUI: client settings
- `--debug` parameter
- `--host` command does not print verbose logs by default
- New API endpoint `https://api.easx.ch`

### 0.8.0 - 2021-06-06

- Initial release
