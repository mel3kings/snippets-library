const fetch = require("node-fetch");
const fs = require("fs");
const index = 1;
const fileStream = fs.createWriteStream(`./resources/response${index}.txt`);
const suburbs = fs.readFileSync(`./resources/suburbs.txt`).toString().split(`\n`);
suburbs.forEach((suburb, i) => {
    setTimeout(() => {
        console.log(`Fetching ${suburb}`)
        if (suburb !== '') {
            fetch(`https://geocode.arcgis.com/arcgis/rest/services/World/GeocodeServer/findAddressCandidates?f=pjson&SingleLine=${suburb}`)
                .then((response) => response.json(), console.log)
                .then((response) => {
                    console.log(`Received response for ${suburb}`)
                    const [candidate] = response.candidates;
                    const {location} = candidate;
                    fileStream.write(`latitude=${location.y}, longitude=${location.x},
                     suburb_name='${suburb.substring(0, suburb.indexOf(','))}';\n`)
                }).catch(ex => console.log(ex))
        }
    }, 1000 * i);
})