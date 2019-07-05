"""Support for Google Maps location sharing."""
from datetime import timedelta
import logging

import voluptuous as vol

from homeassistant.components.device_tracker import (
    PLATFORM_SCHEMA, SOURCE_TYPE_GPS)
from homeassistant.const import (
    ATTR_ID, CONF_USERNAME, ATTR_BATTERY_CHARGING,
    ATTR_BATTERY_LEVEL)
import homeassistant.helpers.config_validation as cv
from homeassistant.helpers.event import track_time_interval
from homeassistant.helpers.typing import ConfigType
from homeassistant.util import slugify, dt as dt_util

_LOGGER = logging.getLogger(__name__)

ATTR_ADDRESS = 'address'
ATTR_FULL_NAME = 'full_name'
ATTR_LAST_SEEN = 'last_seen'
ATTR_NICKNAME = 'nickname'

CONF_MAX_GPS_ACCURACY = 'max_gps_accuracy'
CONF_SCAN_INTERVAL = 'scan_interval'

CREDENTIALS_FILE = '.google_maps_location_sharing.cookies'

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend({
    vol.Required(CONF_USERNAME): cv.string,
    vol.Optional(CONF_MAX_GPS_ACCURACY, default=100000): vol.Coerce(float),
    vol.Optional(CONF_SCAN_INTERVAL, default=60): vol.Coerce(float),
})


def setup_scanner(hass, config: ConfigType, see, discovery_info=None):
    """Set up the Google Maps Location sharing scanner."""
    scanner = GoogleMapsScanner(hass, config, see)
    return scanner.success_init


class GoogleMapsScanner:
    """Representation of an Google Maps location sharing account."""

    def __init__(self, hass, config: ConfigType, see) -> None:
        """Initialize the scanner."""
        from locationsharinglib import Service
        from locationsharinglib.locationsharinglibexceptions import \
            InvalidCookies

        self.see = see
        self.username = config[CONF_USERNAME]
        self.max_gps_accuracy = config[CONF_MAX_GPS_ACCURACY]
        self.scan_interval = timedelta(seconds=config[CONF_SCAN_INTERVAL])

        try:
            credfile = "{}.{}".format(hass.config.path(CREDENTIALS_FILE),
                                      slugify(self.username))
            self.service = Service(credfile, self.username)
            self._update_info()

            track_time_interval(
                hass, self._update_info, self.scan_interval)

            self.success_init = True

        except InvalidCookies:
            _LOGGER.error("You have specified invalid login credentials")
            self.success_init = False

    def _update_info(self, now=None):
        for person in self.service.get_all_people():
            try:
                dev_id = 'google_maps_{0}'.format(slugify(person.id))
            except TypeError:
                _LOGGER.warning("No location(s) shared with this account")
                return

            if self.max_gps_accuracy is not None and \
                    person.accuracy > self.max_gps_accuracy:
                _LOGGER.info("Ignoring %s update because expected GPS "
                             "accuracy %s is not met: %s",
                             person.nickname, self.max_gps_accuracy,
                             person.accuracy)
                continue

            attrs = {
                ATTR_ADDRESS: person.address,
                ATTR_FULL_NAME: person.full_name,
                ATTR_ID: person.id,
                ATTR_LAST_SEEN: dt_util.as_utc(person.datetime),
                ATTR_NICKNAME: person.nickname,
                ATTR_BATTERY_CHARGING: person.charging,
                ATTR_BATTERY_LEVEL: person.battery_level
            }
            self.see(
                dev_id=dev_id,
                gps=(person.latitude, person.longitude),
                picture=person.picture_url,
                source_type=SOURCE_TYPE_GPS,
                gps_accuracy=person.accuracy,
                attributes=attrs,
            )
