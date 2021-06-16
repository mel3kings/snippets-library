const fs = require('fs');
const readline = require('readline');
const {google} = require('googleapis');


const SCOPES = ['https://www.googleapis.com/auth/gmail.readonly'];
const TOKEN_PATH = 'token.json';


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
function authorize(credentials, callback) {
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
function getNewToken(oAuth2Client, callback) {
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

async function getEmailSender(gmail, first) {
    try {
        const mailDetails = await gmail.users.messages.get({
            userId: 'me',
            id: first,
        })
        const headers = mailDetails.data.payload.headers;
        const from = headers.filter(it => it.name === 'From').map(it => it.value);
        console.log(from);
        return from;
    } catch (e) {
        console.error(e);
    }
}

async function processEmails(auth, nextPageToken) {
    const gmail = google.gmail({version: 'v1', auth});
    const response = await gmail.users.messages.list({
        userId: 'me',
        includeSpamTrash: false,
        maxResults: 10,
        labelIds: 'INBOX',
        pageToken: nextPageToken
    });
    if (response.status !== 200) {
        return "";
    }

    const messages = response.data.messages;
    for (const it of messages) {
        const id = it.id
        const from = await getEmailSender(gmail, id);
        console.log(`sender is ${from}`);
    }
    const nextPage = response.data.nextPageToken
    if(nextPageToken !== ''){
        await snooze(1000)
        await processEmails(auth, nextPage)
    }
}

const snooze = ms => new Promise(resolve => setTimeout(resolve, ms));
