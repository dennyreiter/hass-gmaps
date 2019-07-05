# Home Assistant GMAPS
The Home Assistant Google Maps Device Tracker, updated to use LocationSharingLib 4.0.1
The is a mostly drop-in replacement for the google_maps component, using the newer 4.0.1 Location Sharing Lib from [@costasf](https://github.com/costastf)
The biggest change is that you now have to fetch the cookie yourself and put it into your configuration directory.  To get the cookie, see https://github.com/costastf/mapscookiegettercli.

## Installation
1. Copy the `gmaps` folder to the `custom_components` folder in your Home Assistant configuration directory.
2. Add the following code in your `configuration.yaml` file, or modify your google_maps configuration:
```
device_tracker:
  - platform: gmaps
    username: YOUR_USERNAME
```
Get the cookie using the mapscookiegetter.  It will create a file named location_sharing.cookies which needs to be renamed and moved to your configuration directory.  Rename the file using a slugified version of your username (email address) like this:

**.google_maps_location_sharing.cookies.your_username_gmail_com**

If you have been using the google_maps component, you already have this file and you can just copy the new cookie over it.


## Configuration
| key              | required | type    | usage
|------------------|----------|---------|-----------------------------------------------------------------------------------|
| platform         | true     | string  | 'gmaps'                                                                           |
| username         | true     | string  | The email address for the Google account that has access to your shared location. |
| max_gps_accuracy | false    | float   | filter false GPS reports. Defaults to 100km                                       |
| scan_interval    | false    | float   | The minumum number of seconds between queries. Defaults to 60 seconds             |

The reason for the new scan_interval configuration variable is that checking every 30 seconds seemed to be irritating Google's servers which would then start rejecting my queries.
## Resources
[mapscookiegettercli](https://github.com/costastf/mapscookiegettercli)

[locationsharinglib](https://github.com/costastf/locationsharinglib)

[HASS google_maps component](https://www.home-assistant.io/components/google_maps/)
