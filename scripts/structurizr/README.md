# Start
- Run command with subdirectory:
```docker run -it --rm -p 8080:8080 -v /Users/melchor_tatlonghari/workspace/snippets-library/scripts/structurizr/leapx:/usr/local/structurizr structurizr/lite```

- have a workspace.dsl ready in project folder


## Base Code
```
workspace "SystemLandscape" ""{
    model {
        team = person "Team" "Us" "Customer"
        frontEnd = softwareSystem "Front End React" "Base web app" "Front End"
      
        team -> frontEnd "submits websit url"
      

    }

    views {
        systemlandscape "SystemLandscape" {
            include *
            autoLayout
        }


        styles {
            element "Customer"{
                shape Person
            }
            element "Front End" {
                shape WebBrowser
            }            
            element "Database" {
                shape Cylinder
            }
	    element "Software System" {
                background #1168bd
                color #ffffff
            }
        }
    }
}

```


# Shapes
- Box
- RoundedBox
- Diamond
- Circle
- Ellipse
- Hexagon
- Folder
- Cylinder
- Pipe
- WebBrowser
- MobileDevicePortrait 
- Component
- Person
- Robot