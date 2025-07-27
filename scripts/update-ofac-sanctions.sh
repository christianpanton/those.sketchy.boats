#!/bin/sh

echo "# Unitied States Office of Foreign Assets Control" > ../src/sanctions/us-ofac-sdn.imo
echo "# IMO placed on the Specially Designated Nationals (SDN) List" >> ../src/sanctions/us-ofac-sdn.imo

curl -L https://sanctionslistservice.ofac.treas.gov/api/PublicationPreview/exports/SDN.CSV \
    | grep "Vessel Registration Identification IMO" \
    | sed  -E 's/.*IMO ([0-9]{7}).*/\1/' \
    | grep -E '^[0-9]{7}$' \
    | sort \
    | uniq >> ../src/sanctions/us-ofac-sdn.imo