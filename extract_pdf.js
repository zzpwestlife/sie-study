const fs = require('fs');
const pdf = require('pdf-parse');

let dataBuffer = fs.readFileSync('/Users/joeyzou/Code/OpenSource/sie-study/SIE Exam 20252026 For Dummies/part4 client needs and rules.pdf');

pdf(dataBuffer).then(function(data) {
    fs.writeFileSync('/Users/joeyzou/Code/OpenSource/sie-study/SIE Exam 20252026 For Dummies/part4_extracted.txt', data.text);
});
