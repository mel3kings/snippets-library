osascript <<EOD
tell application "iTerm"
    tell current window
        -- create tab to run api
        create tab with default profile

        tell current session
            split vertically with default profile
        end tell

        tell last session of current tab
            split horizontally with default profile
        end tell

        tell first session of current tab
          write text "echo 'server...'"
          write text "cd $1"
          write text "pwd"
          write text "chmod 775 ./server-env.sh"
          write text "./server-env.sh"
          write text "source ./server-env.sh"
          write text "cat ./server-env.sh"
          write text "echo $gqlURI"
          write text "echo gqlURI"
          write text "conda activate simulation"
          write text "conda env list"
          write text "cd ./server"
          write text "pip install -r requirements.txt"
          write text "make install"
        end tell

        tell second session of current tab
          write text "echo 'frontend...'"
          write text "cd $1"
          write text "cd ./packages/frontend; npm install; npm run start"
        end tell

        tell third session of current tab
          write text "echo 'db...'"
          write text "docker logs --follow db"
        end tell
    end tell
end tell

EOD