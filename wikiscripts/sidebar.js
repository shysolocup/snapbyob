const fs = require('fs');
// const fetch = require('node-fetch');
const childproc = require("child_process");
const exec = childproc.exec;
const spawn = childproc.spawn;
const os = require('os');

const getArgs = () =>
  process.argv.reduce((args, arg) => {
    // long arg
    if (arg.slice(0, 2) === "--") {
      const longArg = arg.split("=");
      const longArgFlag = longArg[0].slice(2);
      const longArgValue = longArg.length > 1 ? longArg[1] : true;
      args[longArgFlag] = longArgValue;
    }
    // flags
    else if (arg[0] === "-") {
      const flags = arg.slice(1).split("");
      flags.forEach((flag) => {
        args[flag] = true;
      });
    }
    return args;
  }, {});

const args = getArgs();
const username = args.username;
const useremail = args.useremail;
const commitmsg = args.commitmsg;

console.log(username);
console.log(useremail);
console.log(commitmsg);

console.log('test');

let base = require('./base.json');

let tree = `${base}/tree/main/wiki`;
let blob = `${base}/blob/main/wiki`

let basedir = __dirname.replace("wikiscripts", "");
let dir = `${basedir}wiki/_Sidebar.md`;

let jsoncontent = require('./sidebar.json');
let start = fs.readFileSync(`${__dirname}/sidebar_start.txt`, 'utf8');

let content = start.split("\n");
let wiki = `${basedir}/wiki/`

for (let [n, stuff] of Object.entries(jsoncontent)) {
  let ext = [
    "<details>",
    "",
    `<summary> <b> <a href="${wiki}${n}">🛈</a> ${n} </b> </summary>`,
    "",
    "<br>",
    ""
  ];

  ext.forEach( e => content.push(e) );

  stuff.methods.forEach( (v, i) => {
    var thing = (i == 0) ? "<table>" : "";
    var url = `${wiki}${n}.${v}()`;

    if (v.constructor === Array) {
      url = `${wiki}${v[1]}`;
      v = v[0];
    }

    let ext = [
      `> ${thing} <tr> <td>`, 
      ">",
      `> <b> [🛈](${url}) ${v}() </b>`,
      ">",
      "> </tr> </td>",
      ""
    ];

    ext.forEach( e => content.push(e) );
  });

  stuff.properties.forEach( (v, i) => {
    thing = (i == 0) ? "<table>" : "";

    let ext = [
      `> ${thing} <tr> <td>`, 
      ">",
      `> <b> [🛈](${wiki}${n}.${v}) ${v} </b>`,
      ">",
      "> </tr> </td>",
      ""
    ];

    if (i == 0) {
      [ ">", "> </tr> </td> </table>"].forEach( e => ext.unshift(e));
    }
 
    ext.forEach( e => content.push(e) );
  });

  let end = [
    "> </tr> </td> </table>",
    "",
    "<br>",
    "",
    "</details>",
    ""
  ];

  end.forEach( e => content.push(e) );
}


content.push("<br>");


content = content.join("\n");


fs.writeFileSync(dir, content)


console.log(fs.readFileSync(dir, 'utf8'));


const platform = os.platform();
const pytext = (platform.includes("win")) ? "py" : "python";

const pythonProcess = spawn(pytext, [ `${__dirname}/sidebar.py`, dir, username, useremail, commitmsg, base ]);

pythonProcess.stdout.on('data', (data) => {
  console.log(data.toString());
});

pythonProcess.stderr.on('data', (data) => {
  let err = data.toString();
  
  console.log(`ERR!: ${err}`);
  
  /*if (!err.toLowerCase().includes("date")) {
    throw err;
  }*/
});