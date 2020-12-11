var fs=require("fs");
let input = fs.readFileSync("./input.txt" ).toString().split("\n").map(x=>parseInt(x));
input.filter(x=> input.find(y => y==2020-x)!=undefined).reduce((prod,acc)=> prod*acc, 1);
input.filter(x=> input.find(y => y==2020-x-(input.filter(z => z==2020-x-y)[0]))!=undefined).reduce((prod,acc)=> prod*acc, 1);