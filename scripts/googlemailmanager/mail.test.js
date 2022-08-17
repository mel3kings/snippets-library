const {shouldDeleteEmail} = require("./mail");
const {deleteEmails} = require("./constants");


describe('should delete emails if is part of the delete email', () => {
    it('should return true', () => {
        const sample = "propertytree@propertytree.com"
        expect(shouldDeleteEmail(deleteEmails, sample)).toBeTruthy()
    });

    it('should not return false if email is not included', () => {
        const sample = "meltatlonghari3@gmail.com"
        expect(shouldDeleteEmail(deleteEmails, sample)).toBeFalsy()
    });


    it('should delete if from is a substring sender', () => {
        const email = 'hello@stackshare.io';
        expect(deleteEmails.includes(email)).toBeTruthy()
        const sender = "HELLO <hello@stackshare.io>"
        expect(shouldDeleteEmail(deleteEmails, sender)).toBeTruthy()
    });

    it('should not delete if not part of', () => {
        const tempDeleteEmails = ["goodbye@stackshare.io"]
        const email = 'dontdelete@stackshare.io';
        expect(tempDeleteEmails.includes(email)).toBeFalsy()
        const sender = "dontdelete <dontdelete@stackshare.io>"
        expect(shouldDeleteEmail(tempDeleteEmails, sender)).toBeFalsy()
    });

    it('should delete email from telstra', () => {
        const email = 'Telstra <noreply@messages.telstra.com>';
        expect(deleteEmails.includes(email)).toBeFalsy()
        const sender = "Telstra <noreply@messages.telstra.com>"
        expect(shouldDeleteEmail(deleteEmails, sender)).toBeTruthy()

    });

});