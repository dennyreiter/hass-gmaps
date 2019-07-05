# Home Assistant GMAPS
The Home Assistant Google Maps Device Tracker, updated to use LocationSharingLib 4.0.1
## Installation
1. Copy the `gmaps` folder to the `custom_components` folder in your Home Assistant configuration directory.
2. Add the following code in your `configuration.yaml` file, or modify your google_maps configuration:
```
device_tracker:
  - platform: gmaps
    username: YOUR_USERNAME
```
## Configuration
| key              | required | type    | usage
|------------------|----------|---------|-----------------------------------------------------------------------------------|
| platform         | true     | string  | 'gmaps'                                                                           |
| username         | true     | string  | The email address for the Google account that has access to your shared location. |
| max_gps_accuracy | false    | float   | filter false GPS reports. Defaults to 100km                                       |
| scan_interval    | false    | float   | The minumum number of seconds between queries. Defaults to 60 seconds             |

