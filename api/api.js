const   express =   require('express')
const { rootCertificates } = require('tls')
const   path    =   require('path')



// Configuración inicial del servidor. Trabajo en progreso.

const   app =   express()


app.get('/',(req,res) => {
    const   filepath    =   path.join(__dirname,'..','frontend','index.html');
    res.sendFile(filepath);
})

app.listen(3000)
console.log(`server on port ${3000}`)