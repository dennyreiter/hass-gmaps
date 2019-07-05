# Home Assistant GMAPS
The Home Assistant Google Maps Device Tracker, updated to use LocationSharingLib 4.0.1
The is a mostly drop-in replacement for the google_maps component, using the newer 4.0.1 Location Sharing Lib from @costasf ( https://github.com/costastf/locationsharinglib )
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

.google_maps_location_sharing.cookies.your_username_gmail_com

## Configuration
| key              | required | type    | usage
|------------------|----------|---------|-----------------------------------------------------------------------------------|
| platform         | true     | string  | 'gmaps'                                                                           |
| username         | true     | string  | The email address for the Google account that has access to your shared location. |
| max_gps_accuracy | false    | float   | filter false GPS reports. Defaults to 100km                                       |
| scan_interval    | false    | float   | The minumum number of seconds between queries. Defaults to 60 seconds             |

