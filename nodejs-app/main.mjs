import fs from 'node:fs'

fs.appendFile('my-file.txt', 'File was created by Node.js', (err) => {
    if (err) throw err
    console.log('File store!')
})

setTimeout(() => console.log('The end'), 30000)