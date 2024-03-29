# Home Assistant GMAPS

**THIS IS NOW DEPRECATED AS IT HAS BEEN INTEGRATED INTO HOME ASSISTANT AS OF 0.97**

The Home Assistant Google Maps Device Tracker, updated to use LocationSharingLib 4.0.1
This is a mostly drop-in replacement for the google_maps component, using the newer 4.0.1 Location Sharing Lib from [@costasf](https://github.com/costastf).
The biggest change is that you now have to fetch the cookie yourself and put it into your configuration directory.  To get the cookie, see https://github.com/costastf/mapscookiegettercli.

## Installation
1. Copy the `gmaps` folder to the `custom_components` folder in your Home Assistant configuration directory:
```
/home/homeassistant/
├── .homeassistant
│   ├── custom_components
│   │   └── gmaps

```
2. Add the following code in your `configuration.yaml` file, or modify your google_maps configuration:
```
device_tracker:
  - platform: gmaps
    username: YOUR_USERNAME
```
(The password is no longer used since you authenticate on your own when creating the cookie.)

3. Get the cookie using the [mapscookiegetter](https://github.com/costastf/mapscookiegettercli).  It will create a file named **location_sharing.cookies** which needs to be renamed and moved to your configuration directory. You might also be able to use the [cookies.txt Chrome extenstion](https://chrome.google.com/webstore/detail/cookiestxt/njabckikapfpffapmjgojcnbfjonfjfg), but I have not tried it. 

4. Rename the file using a slugified version of the username (email address) in the configuration. For example, if the username is example@gmail.com:

**.google_maps_location_sharing.cookies.example_gmail_com**

If you have been using the google_maps component, you already have a file by this name and you can just copy the new cookie over it.


## Configuration
| key              | required | type    | usage
|------------------|----------|---------|-----------------------------------------------------------------------------------|
| platform         | true     | string  | 'gmaps'                                                                           |
| username         | true     | string  | The email address for the Google account that has access to your shared location. |
| max_gps_accuracy | false    | float   | filter false GPS reports. Defaults to 100km                                       |
| scan_interval    | false    | float   | The minimum number of seconds between queries. Defaults to 60 seconds             |

The reason for the new scan_interval configuration variable is that checking every 30 seconds seemed to be irritating Google's servers which would then start rejecting my queries.
## Resources
[mapscookiegettercli](https://github.com/costastf/mapscookiegettercli)

[locationsharinglib](https://github.com/costastf/locationsharinglib)

[HASS google_maps component](https://www.home-assistant.io/components/google_maps/)
