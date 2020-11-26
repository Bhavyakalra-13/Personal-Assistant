const py = require("python-shell")
const path=required("path")

let options={
    scriptPath:path.join(__dirname,'../'),

}
let output=new py('main.py',options)
output.on('msg',function(msg){
    swal(msg)
})