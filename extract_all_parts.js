const fs = require('fs');
const pdf = require('pdf-parse');

const files = [
    '/Users/joeyzou/Code/OpenSource/sie-study/SIE Exam 20252026 For Dummies/part2 basic security investments.pdf',
    '/Users/joeyzou/Code/OpenSource/sie-study/SIE Exam 20252026 For Dummies/part3 more complex securities.pdf',
    '/Users/joeyzou/Code/OpenSource/sie-study/SIE Exam 20252026 For Dummies/part4 client needs and rules.pdf'
];

async function extractAll() {
    for (const file of files) {
        console.log(`Processing ${file}...`);
        try {
            const dataBuffer = fs.readFileSync(file);
            const data = await pdf(dataBuffer);
            const txtPath = file.replace('.pdf', '_extracted.txt');
            fs.writeFileSync(txtPath, data.text);
            console.log(`Saved to ${txtPath}`);
        } catch (e) {
            console.error(`Error processing ${file}:`, e);
        }
    }
}

extractAll();
