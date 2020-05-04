const hljs = require("highlight.js")

const highlight = (language, code) => {
  if (language) {
    try {
      return hljs.highlight(language, code).value
    } catch (err) {}
  }

  return hljs.highlightAuto(code).value
}

const readline = require("readline")

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
  terminal: false
})

rl.on('line', line => {
  if (!line) {
    rl.close()
    return
  }

  const { language, code } = JSON.parse(line)
  console.log(JSON.stringify(highlight(language, code)))
})
