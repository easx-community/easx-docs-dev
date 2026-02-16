# Introduction 

EAS is a service providing a secure platform for the exchange of insurer values between Swiss pension funds.
Any pension fund can easily connect to the EAS REST APIs to send and receive the insurer values from or to any other connected pension fund.

# Architecture

There are multiple options of connecting to EAS:

![User Architecture Diagram](./User_Architecture_v0.1_cropped.png)

1. Connecting directly to the EAS service

   This approach is the easiest and quickest to get up and running, but does not provide full end-to-end security.

2. Connecting using the EAS Client

   This is our **suggested option**, balancing simplicity, maintainabiliy and security.
   
   Using this approach a full end-to-end encryption can be utilized, ensuring highest levels of security.
   It requires either an installation of a component (EAS Client) or an instance of a docker image available 
   in the [docker hub](https://hub.docker.com/r/easx/client) running on your servers or in your cloud.
   Updates and improvements are maintained by the EASX team.

4. Implementing the client features in your application

   This approach can also provide a secure end-to-end encryption. But it means implementing and maintaining the custom code,
   covering the EAS Clients functionalities, in your own application by yourself.

In all options the provided REST APIs that the pension fund's system needs to call are almost the same, except for authentication parameters.

## APIs

For accessing EASX from a pension fund system two REST APIs are provided: Hub API, Directory API

You can find more information in the [introduction to the APIs](APIs.md).

# Getting Started

To try out and get up and running checkout the [Getting Started](Getting-Started.md) page.

# Resources

- *Portal* - [https://portal.easx.ch](https://portal.easx.ch) - main entry point and registration
- *Documentation Test Environment* - [https://docs-test.easx.ch](https://docs-test.easx.ch) - Documentation for the version running in the *Test* environment
- *Documentation Production Environment* - [https://docs.easx.ch](https://docs.easx.ch) - Documentation for the version running in the *Production* environment
- *EASX API* - [https://api.easx.ch/api](https://api.easx.ch/api) - Root for all APIs on the EASX Server
- *EAS Client Docker* - [https://hub.docker.com/r/easx/client](https://hub.docker.com/r/easx/client) - EAS Client docker image on Docker Hub 


---

Contact [support@easx.ch](mailto:support@easx.ch) with any questions or issues.
