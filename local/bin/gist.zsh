#!/bin/zsh

function json_quote {
  node -e "console.log(JSON.stringify(fs.readFileSync('$1').toString()))"
}

github_gist_token=$(cat ~/.github-gist-token)
file=$1
quoted_file_contents=$(json_quote $file)
file_name=$(basename $file)
description=${2:-$file_name}

printf -v json '{
  "public": true,
  "description": "%s",
  "files": { "%s": { "content": %s } }
}' $description $file_name $quoted_file_contents

response=$(mktemp)

>$response curl --silent                       \
  -H "Authorization: token $github_gist_token" \
  -X POST                                      \
  -d "$json"                                   \
  "https://api.github.com/gists"

echo "yooooou got it, champ!"

node -e "
  console.log(JSON.parse(
    require('fs')
      .readFileSync(process.argv[1])
      .toString()
  ).html_url)
" $response
