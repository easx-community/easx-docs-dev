Two APIs provide all the operations a pension fund system needs to access EASX:

# EAS Hub API

The actual REST API providing all the features needed to send and receive insurer values (documents).

It contains the following resources:
- `in-documents`: Handles the FZL data (pension transfer documents) that the caller has received.
- `out-documents`: Allows the caller to send FZL data (pension transfer documents) to other participants.
- `receipts`: Provides handling of receipts received for documents the caller previously sent. 
- `logs`: Provides logging information relevant to the caller.

For detailed documentation of the available operations check out the [Hub API details](https://portal.easx.ch/api-details#api=60d2f0460d4f28337a74fca8) on the EASX Portal.

# EAS Directory API

This REST API allows retrieving the information on all participants reachable using EAS.

It contains the following resources:
- `participants`: Provides information on all participants in the EASX system.
- `me`: Provides information about the caller.

For detailed documentation of the available operations check out the [Directory API details](https://portal.easx.ch/api-details#api=60d2f0fa6fb64e25dfd12323) on the EASX Portal.
