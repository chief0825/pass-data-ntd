import express from "express"
const app = express()

app.get('/test/get_data', function (req, res) {
  res.send('Hello Node')
})

app.listen(3000)
