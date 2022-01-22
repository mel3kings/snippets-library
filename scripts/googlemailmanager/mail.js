const fs = require('fs');
const readline = require('readline');
const {google} = require('googleapis');

const SCOPES = ['https://www.googleapis.com/auth/gmail.modify'];
const TOKEN_PATH = 'token.json';
const emailMap = new Map();
let totalNumber = 0;

fs.readFile('credentials.json', (err, content) => {
    if (err) return console.log('Error loading client secret file:', err);
    authorize(JSON.parse(content), processEmails);
});

/**
 * Create an OAuth2 client with the given credentials, and then execute the
 * given callback function.
 * @param {Object} credentials The authorization client credentials.
 * @param {function} callback The callback to call with the authorized client.
 */
const authorize = (credentials, callback) => {
    const {client_secret, client_id, redirect_uris} = credentials.web;
    const oAuth2Client = new google.auth.OAuth2(
        client_id, client_secret, redirect_uris[0]);

    // Check if we have previously stored a token.
    fs.readFile(TOKEN_PATH, (err, token) => {
        if (err) return getNewToken(oAuth2Client, callback);
        oAuth2Client.setCredentials(JSON.parse(token));
        callback(oAuth2Client);
    });
}

/**
 * Get and store new token after prompting for user authorization, and then
 * execute the given callback with the authorized OAuth2 client.
 * @param {google.auth.OAuth2} oAuth2Client The OAuth2 client to get token for.
 * @param {getEventsCallback} callback The callback for the authorized client.
 */
const getNewToken = (oAuth2Client, callback) => {
    const authUrl = oAuth2Client.generateAuthUrl({
        access_type: 'offline',
        scope: SCOPES,
    });
    console.log('Authorize this app by visiting this url:', authUrl);
    const rl = readline.createInterface({
        input: process.stdin,
        output: process.stdout,
    });
    rl.question('Enter the code from that page here: ', (code) => {
        rl.close();
        oAuth2Client.getToken(code, (err, token) => {
            if (err) return console.error('Error retrieving access token', err);
            oAuth2Client.setCredentials(token);
            fs.writeFile(TOKEN_PATH, JSON.stringify(token), (err) => {
                if (err) return console.error(err);
                console.log('Token stored to', TOKEN_PATH);
            });
            callback(oAuth2Client);
        });
    });
}

// array of emails to be deleted
const deleteEmails = ["foo@foo.com"]

const processEmails = async (auth, nextPageToken) => {
    const gmail = google.gmail({version: 'v1', auth});
    const response = await gmail.users.messages.list({
        userId: 'me',
        includeSpamTrash: false,
        maxResults: 1000,
        pageToken: nextPageToken
    });
    if (response.status !== 200) {
        return "";
    }
    const messages = response.data.messages;
    await Promise.all(messages.map(async (it) => {
        totalNumber++;
        const id = it.id
        const from = await getEmailSender(gmail, id);
        if (deleteEmails.includes(from)) {
            await deleteEmail(from, gmail, id);
        } else {
            if (emailMap.has(from)) {
                let count = emailMap.get(from);
                emailMap.set(from, ++count);
            } else {
                emailMap.set(from, 1);
            }
        }
    }))

    const nextPage = response.data.nextPageToken
    if (nextPageToken !== '' && nextPage !== undefined) {
        await snooze(200)
        await writeToFile(nextPage)
        console.log(`======nextPageToken, processed: ${totalNumber} `, nextPageToken);
        await processEmails(auth, nextPage)
    }
}

const getEmailSender = async (gmail, first) => {
    try {
        const mailDetails = await gmail.users.messages.get({
            userId: 'me',
            id: first,
        })
        const headers = mailDetails.data.payload.headers;
        const from = headers.filter(it => it.name === 'From').map(it => it.value);

        return from[0];
    } catch (e) {
        console.error(e);
    }
}


async function deleteEmail(from, gmail, first) {
    console.log("DELETING FROM:" + from);
    const deleted = await gmail.users.messages.trash({
        userId: 'me',
        id: first,
    })
    console.log("DELETING FROM:" + from + " " + deleted.data);
}

const writeToFile = async (nextPage) => {
    const fileStream = fs.createWriteStream(`./resources/response${totalNumber}_${nextPage}.txt`);
    console.log('======emailMap', emailMap);
    for (const [key, value] of emailMap) {
        fileStream.write(`${key}: ${value}\n`)
    }
    console.log("done writing");
    fileStream.close();
}

const snooze = ms => new Promise(resolve => setTimeout(resolve, ms));
