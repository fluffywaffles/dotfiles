# Printing on verdure

`lpoptions` sets the defaults for `green-office`, a driverless IPP
Everywhere queue for the Brother MFC-J1410DW. The queue is set up by
hand from the sequence below, adapted to the machine, rather than by a
script: the script it replaces hardcoded a device URI, a PPD path and a
USB serial, and rotted.

1. Install `cups`, `cups-filters`, `ghostscript` and `nss-mdns` from
   `extra`. The printer accepts no PDF, so `ghostscript` is required,
   though `cups-filters` declares it optional.
2. Enable `avahi-daemon` and `cups.socket`.
3. Put mDNS ahead of `resolve` in `/etc/nsswitch.conf`, so avahi
   answers for `.local`:

   ```
   hosts: mymachines mdns_minimal [NOTFOUND=return] resolve [!UNAVAIL=return] files myhostname dns
   ```

4. Ask the printer what it speaks. `ipp-everywhere` in its
   `ipp-features-supported` means no vendor driver is needed:

   ```zsh
   ipptool -tv ipp://BRWACF23CAE3880.local/ipp/print get-printer-attributes.test
   ```

5. Create the queue:

   ```zsh
   sudo lpadmin -p green-office -E -m everywhere -D 'Brother MFC-J1410DW' \
     -v ipp://BRWACF23CAE3880.local:631/ipp/print
   ```

6. `rcup` links `lpoptions` to `~/.cups/lpoptions`, which makes
   `green-office` the default destination, duplex and greyscale.

The queue names the printer's role, and `-D` names the model, so new
hardware takes over the queue's name rather than a new name reaching
every print dialog.

The URI addresses the printer by its mDNS name, so a new DHCP lease
doesn't break printing. mDNS never crosses a router: a machine reaching
the printer from another subnet, VLAN or guest SSID needs its IP
address, held by a DHCP reservation. macOS finds the printer through
Bonjour with no setup.

Port 9100 is closed, so a raw socket queue is not an option. No AUR
package carries this model's vendor driver; if one is ever needed,
adapt the `brother-dcp-j1360dw` PKGBUILD, which parameterises the model
and carries the same upstream driver. `brlaser` covers only laser
printers.

`lpoptions` lives under `host-verdure/` because each line names a queue
and the format has no include, so a shared copy would bind every
machine to this queue.
