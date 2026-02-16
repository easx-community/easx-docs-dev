The EAS Client encapsulates all important functionalities for accessing EASX. It provides handling
all the security features and compatibility features needed to ensure an end-to-end encrpytion.

# Deployment

The EAS Client is provided in deployment in two different ways:

## Executable file
The binary executable file is available for download on the [EASX portal](https://portal.easx.ch) when
signed in. Different variants for Windows, Linux or MacOS are provided.

The EAS Client is a self-contained, single-file application and no other dependencies need to be deployed.
It can be placed in a directory and configured as explained in [settings](Settings.md).

## Docker image

The EAS Client is also provided as a [docker image](https://hub.docker.com/r/easx/client) on the docker hub.
This allows easily deploying and managing access to EASX. Configuration can be easily done and allows
using a secure key repository (i.e. Azure Key Vault).

For an example of using the EAS Client as a docker instance deployed as a Azure App Service, see [Deploy to Azure](Deploy-To-Azure.md).

# Functionality

After setting up the EAS Client (both Windows, Linux and MacOS are supported), you can utilize it in one of the following ways:

1. Command line scripts.

Find a list of all supported commands documented under [EAS Client commands](Commands.md). For example, to get all incoming documents into a folder, you will have to run the client like `EASClient.exe --receive "incoming folder"`. The client will also handle all additional actions, like sending receipts, automatically.

To send a document, you'll have to copy it into the specified folder, and run the send command `EASClient.exe --send "outgoing folder"`.

Just like in direct approach, it is possible to create a simple batch/shell script and configure it to run every few hours using Windows Task Scheduler or a cron job. With just a few simple commands, you will get the highest level of security.

Note: Command line scripts are only available when the EAS Client is deployed as an executable file, not docker instance.

1. Client API request.

In case you'd like to integrate EAS API into your application, but you don't want to implement encryption, signing and validations yourself, consider using this approach. After running EAS Client in host mode, it will launch a local instance of EAS API that does not require any security.

This way, you will send a simple unencrypted http requests to the local client URL. The client will then validate your request, generate signature, encrypt the payload, attach required subscription headers, attach the client certificate, specify default UID and finally send the request to remote EAS API. Upon receiving the response, the client will validate signature, decrypt the payload and return the decrypted response.

Just like in direct approach, it is possible to create a simple batch/shell script and configure it to run every few hours using Windows Task Scheduler or a cron job. And in case you'd like to integrate it in your application, there is an OpenAPI Specification to facilitate the process.

3. Client GUI

In case you'd like to perform document exchange manually, view the logs, change EAS Client settings or experiment with local API, consider using this approach. After running EAS Client in host mode, it will launch a local instance of EAS client GUI. It allows you to access all the features of EAS Client from your browser. After navigating to a specified local URL, you will be able to send, view and manage documents, receipts, access client directory, logs, etc. GUI also includes Swagger and Open API Specification, so it can be used to try out the local API.

This approach might work for you in case you would like to perform all the actions manually. For example, you can just create a shortcut to launch EAS Client in hosted mode. Then, you'll just launch the shortcut, open an Incoming Documents web page in your browser, and download a document without having to deal with encryptions or commands whatsoever.
