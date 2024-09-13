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


/*fetch(`https://api.github.com/user/${username}`, {
  "headers": {
    "User-Agent": "request",
    "Authorization": `Bearer ${token}`,
    "X-GitHub-Api-Version": "2022-11-28"
  }
}).then(res => {
  console.log(res);
});*/

console.log('test');

let base = "https://github.com/shysolocup/snapbyob";

let tree = `${base}/tree/main/wiki`;
let blob = `${base}/blob/main/wiki`

let basedir = __dirname.replace("wikiscripts", "");
let logrefdir = `${basedir}wiki/_Sidebar.md`;

let jsoncontent = require('./sidebar.json');
let start = fs.readFileSync(`${__dirname}/sidebar_start.txt`, 'utf8');

let content = start.split("\n");

console.log(content);

/*

let content = [

  "# LogRef",
  "this is where log references are for easier navigation<br>",
  '<img height=22 src="https://github.com/Rats-United/HOME-update-log/actions/workflows/logref.yml/badge.svg" alt="publish">'

];

groups.forEach((group, gi) => {
  let groupdir = `${dir}/${group}`;
  let treelink = `${tree}/${ group.split(" ").join("%20") }`;
  let bloblink = `${blob}/${ group.split(" ").join("%20") }`;
  let logs = fs.readdirSync(groupdir);

  content.push(`### [${group}](${treelink}) (#${gi})`);
  
  logs.forEach((log, li) => {
    let logbloblink = `${bloblink}/${ log.split(" ").join("%20") }`;
    let logdir = `${groupdir}/${ log }`;
    
    let filecontent = fs.readFileSync(logdir, 'utf8');
    let csplit = filecontent.split(/[\r\n]+/);

    var name;

    csplit.forEach(c => {
      if (c.match(/^# /)) {
        name = c.replace("# ", "").trim();
      }
    });

    if (!name) {
      name = log.replace(".md", "");
    };
    
    content.push(`${li+1}. ${name} [(${ log })](${ logbloblink }) `)
  });
});


content = content.join("\n\n");

fs.writeFileSync(logrefdir, content)


console.log(fs.readFileSync(logrefdir, 'utf8'));


const platform = os.platform();
const pytext = (platform.includes("win")) ? "py" : "python";

const pythonProcess = spawn(pytext, [ `${__dirname}/logref.py`, username, useremail, commitmsg, base ]);

pythonProcess.stdout.on('data', (data) => {
  console.log(data.toString());
});

pythonProcess.stderr.on('data', (data) => {
  let err = data.toString();
  
  console.log(`ERR!: ${err}`);
  
  if (!err.toLowerCase().includes("date")) {
    throw err;
  }
});
*/