import mysql from 'mysql2/promise'

const   API_KEY =   'bfac41a99e9218be42962d57307771c5' //TMDB api, de aqui planeo llenar las tablas de la  db.

//template para conectar la db
mysql.createPool({
    host: '',
    user:'',
    password:'',
    database:''
})